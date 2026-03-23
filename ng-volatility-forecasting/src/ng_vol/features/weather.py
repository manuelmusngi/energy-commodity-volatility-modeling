import pandas as pd

def add_weather_anomalies(df: pd.DataFrame, hdd_col: str, anomaly_days: int) -> pd.DataFrame:
    out = df.copy()
    if hdd_col in out.columns:
        out["hdd_anom"] = out[hdd_col] - out[hdd_col].rolling(anomaly_days).mean()
    return out
