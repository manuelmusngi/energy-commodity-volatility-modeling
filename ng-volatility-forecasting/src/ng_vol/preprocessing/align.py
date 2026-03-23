import pandas as pd

def build_daily_panel(
    prices: pd.DataFrame,
    curve: pd.DataFrame,
    storage: pd.DataFrame,
    fundamentals: pd.DataFrame,
    weather: pd.DataFrame,
) -> pd.DataFrame:
    idx = prices.index
    panel = (
        prices
        .join(curve.reindex(idx).ffill(), how="left")
        .join(storage.reindex(idx).ffill(), how="left")
        .join(fundamentals.reindex(idx).ffill(), how="left")
        .join(weather.reindex(idx).ffill(), how="left")
    )
    return panel.dropna()
