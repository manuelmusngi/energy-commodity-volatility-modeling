import numpy as np
import pandas as pd

def log_return(price: pd.Series) -> pd.Series:
    return np.log(price).diff()

def pnl_proxy(price: pd.Series, exposure_units: float = 1.0) -> pd.Series:
    return exposure_units * log_return(price)
