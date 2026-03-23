from pathlib import Path
import pandas as pd

from ng_vol.config.loader import load_all_configs
from ng_vol.io.ingestion import load_prices, load_curve, load_storage, load_fundamentals, load_weather
from ng_vol.io.validation import require_columns, require_datetime_index, require_sorted_index
from ng_vol.preprocessing.align import build_daily_panel

from ng_vol.features.volatility import add_realized_vol_features
from ng_vol.features.curve import add_curve_slopes
from ng_vol.features.storage import add_storage_surprise
from ng_vol.features.weather import add_weather_anomalies

from ng_vol.models.har import HARModel
from ng_vol.models.tree import RFVolModel
from ng_vol.forecasting.engine import oos_forecast

from ng_vol.regimes.classifier import classify_by_quantiles

def run(config_dir: Path, save_outputs: bool = True) -> dict:
    cfg = load_all_configs(config_dir)

    raw_dir = Path(cfg["data"]["paths"]["raw_dir"])
    out_dir = Path(cfg["data"]["paths"]["processed_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)

    # --- Load
    prices = load_prices(raw_dir, cfg["data"]["schema"]["prices"], cfg["data"]["files"]["prices"])
    curve = load_curve(raw_dir, cfg["data"]["schema"]["futures_curve"], cfg["data"]["files"]["futures_curve"])
    storage = load_storage(raw_dir, cfg["data"]["schema"]["storage"], cfg["data"]["files"]["storage"])
    funds = load_fundamentals(raw_dir, cfg["data"]["schema"]["fundamentals"], cfg["data"]["files"]["fundamentals"])
    weather = load_weather(raw_dir, cfg["data"]["schema"]["weather"], cfg["data"]["files"]["weather"])

    # --- Validate (minimal)
    for name, df in [("prices", prices), ("curve", curve), ("storage", storage), ("fundamentals", funds), ("weather", weather)]:
        require_datetime_index(df, name)
        require_sorted_index(df, name)

    require_columns(prices, [cfg["data"]["schema"]["prices"]["spot"]], "prices")

    # --- Align
    panel = build_daily_panel(prices, curve, storage, funds, weather)

    # --- Features
    spot_col = cfg["data"]["schema"]["prices"]["spot"]
    panel = add_realized_vol_features(
        panel,
        spot_col=spot_col,
        windows=cfg["features"]["volatility"]["windows"],
        ann_factor=cfg["features"]["volatility"]["annualization_factor"],
    )

    if cfg["features"]["curve"]["enable"]:
        panel = add_curve_slopes(panel, cfg["features"]["curve"]["slopes"])

    if cfg["features"]["storage"]["enable"]:
        panel = add_storage_surprise(
            panel,
            storage_col=cfg["data"]["schema"]["storage"]["storage"],
            change_days=cfg["features"]["storage"]["change_days"],
            rolling_mean_years=cfg["features"]["storage"]["rolling_mean_years"],
            surprise_name=cfg["features"]["storage"]["surprise_name"],
        )

    if cfg["features"]["weather"]["enable"]:
        panel = add_weather_anomalies(
            panel,
            hdd_col=cfg["data"]["schema"]["weather"]["hdd"],
            anomaly_days=cfg["features"]["weather"]["anomaly_days"],
        )

    # --- Target
    horizon = cfg["features"]["targets"]["horizon_days"]
    target_col = cfg["features"]["targets"]["target_column"]
    panel[target_col] = panel["rv_10d"].shift(-horizon)

    panel = panel.dropna()

    # --- Model selection
    model_cfg = cfg["models"]["models"]
    train_cfg = cfg["models"]["training"]
    cv_splits = int(train_cfg["cv_splits"])

    feature_cols = [c for c in panel.columns if c not in [target_col]]
    X_all = panel[feature_cols]
    y = panel[target_col]

    outputs: dict = {"features_path": out_dir / "features_panel.parquet"}

    # --- HAR
    forecasts = {}
    metrics = {}

    if model_cfg["har"]["enabled"]:
        har_feats = [f for f in model_cfg["har"]["features"] if f in panel.columns]
        har = HARModel()
        preds, rmses = oos_forecast(har, panel[har_feats], y, cv_splits=cv_splits)
        forecasts["har"] = preds
        metrics["har_rmse_mean"] = sum(rmses) / len(rmses)

    # --- RF
    if model_cfg["random_forest"]["enabled"]:
        rf_feats = feature_cols if model_cfg["random_forest"]["features"] == "all" else model_cfg["random_forest"]["features"]
        rf = RFVolModel(**model_cfg["random_forest"]["params"])
        preds, rmses = oos_forecast(rf, panel[rf_feats], y, cv_splits=cv_splits)
        forecasts["rf"] = preds
        metrics["rf_rmse_mean"] = sum(rmses) / len(rmses)

    # --- Choose primary forecast (prefer RF if enabled)
    primary_name = "rf" if "rf" in forecasts else "har"
    pred = forecasts[primary_name].dropna()

    # --- Regimes + hedge bias
    bt = cfg["backtest"]
    reg = bt["regimes"]
    labels = reg["labels"]
    regimes = classify_by_quantiles(
        pred,
        q_low=float(reg["quantiles"]["low"]),
        q_high=float(reg["quantiles"]["high"]),
        labels=labels,
    )

    hedge_map = bt["hedge_bias"]["mapping"]
    hedge_bias = regimes.map(hedge_map)

    forecasts_df = pd.DataFrame({"pred_rv": pred, "realized_rv": y.loc[pred.index]})
    regimes_df = pd.DataFrame({"vol_regime": regimes, "hedge_bias": hedge_bias})

    if save_outputs:
        panel.to_parquet(outputs["features_path"])
        (out_dir / "forecasts.parquet").write_bytes(forecasts_df.to_parquet())
        (out_dir / "regimes.parquet").write_bytes(regimes_df.to_parquet())

    outputs.update({
        "forecasts_path": out_dir / "forecasts.parquet",
        "regimes_path": out_dir / "regimes.parquet",
        "primary_model": primary_name,
        "metrics": metrics,
    })
    return outputs
