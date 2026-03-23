from pathlib import Path
import pandas as pd

from ng_vol.config.loader import load_all_configs
from ng_vol.io.ingestion import load_prices

def test_load_prices_has_datetime_index():
    cfg = load_all_configs(Path("config"))
    raw_dir = Path(cfg["data"]["paths"]["raw_dir"])
    schema = cfg["data"]["schema"]["prices"]
    fname = cfg["data"]["files"]["prices"]

    df = load_prices(raw_dir, schema, fname)
    assert isinstance(df.index, pd.DatetimeIndex)
    assert schema["spot"] in df.columns
