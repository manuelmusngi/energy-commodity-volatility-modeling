from pathlib import Path
import pandas as pd

def _read_csv(path: Path, date_col: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=[date_col])
    df = df.sort_values(date_col).set_index(date_col)
    return df

def load_prices(raw_dir: Path, schema: dict, fname: str) -> pd.DataFrame:
    return _read_csv(raw_dir / fname, schema["date"])

def load_curve(raw_dir: Path, schema: dict, fname: str) -> pd.DataFrame:
    return _read_csv(raw_dir / fname, schema["date"])

def load_storage(raw_dir: Path, schema: dict, fname: str) -> pd.DataFrame:
    return _read_csv(raw_dir / fname, schema["date"])

def load_fundamentals(raw_dir: Path, schema: dict, fname: str) -> pd.DataFrame:
    return _read_csv(raw_dir / fname, schema["date"])

def load_weather(raw_dir: Path, schema: dict, fname: str) -> pd.DataFrame:
    return _read_csv(raw_dir / fname, schema["date"])
