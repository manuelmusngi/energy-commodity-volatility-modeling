import pandas as pd
from ng_vol.features.volatility import add_realized_vol_features

def test_add_realized_vol_features_creates_columns():
    df = pd.DataFrame({"spot": [3.0, 3.1, 3.05, 3.2, 3.15]}, index=pd.date_range("2024-01-01", periods=5))
    out = add_realized_vol_features(df, "spot", windows=[2], ann_factor=252)
    assert "rv_2d" in out.columns
