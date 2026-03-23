import pandas as pd

def require_columns(df: pd.DataFrame, cols: list[str], name: str) -> None:
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise ValueError(f"{name}: missing columns {missing}")

def require_datetime_index(df: pd.DataFrame, name: str) -> None:
    if not isinstance(df.index, pd.DatetimeIndex):
        raise ValueError(f"{name}: index must be DatetimeIndex")

def require_sorted_index(df: pd.DataFrame, name: str) -> None:
    if not df.index.is_monotonic_increasing:
        raise ValueError(f"{name}: index must be sorted ascending")
