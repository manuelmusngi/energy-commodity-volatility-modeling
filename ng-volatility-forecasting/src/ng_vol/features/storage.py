import pandas as pd

def add_storage_surprise(
    df: pd.DataFrame,
    storage_col: str,
    change_days: int,
    rolling_mean_years: int,
    surprise_name: str,
) -> pd.DataFrame:
    out = df.copy()
    out["storage_change"] = out[storage_col].diff(change_days)
    out["storage_change_roll_mean"] = out["storage_change"].rolling(rolling_mean_years * 52).mean()
    out[surprise_name] = out["storage_change"] - out["storage_change_roll_mean"]
    return out
