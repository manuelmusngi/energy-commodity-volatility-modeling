import numpy as np
import pandas as pd

def realized_vol(price: pd.Series, window: int, ann_factor: int = 252) -> pd.Series:
    r = np.log(price).diff()
    return r.rolling(window).std() * np.sqrt(ann_factor)

def add_realized_vol_features(df: pd.DataFrame, spot_col: str, windows: list[int], ann_factor: int) -> pd.DataFrame:
    out = df.copy()
    for w in windows:
        out[f"rv_{w}d"] = realized_vol(out[spot_col], w, ann_factor)
    return out
