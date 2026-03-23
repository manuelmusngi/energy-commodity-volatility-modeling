import pandas as pd

def add_curve_slopes(df: pd.DataFrame, slopes: list[dict]) -> pd.DataFrame:
    out = df.copy()
    for s in slopes:
        out[s["name"]] = out[s["long"]] - out[s["short"]]
    return out
