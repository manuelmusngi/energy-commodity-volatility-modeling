import numpy as np
import pandas as pd
import statsmodels.api as sm
from .base import VolModel

class HARModel(VolModel):
    def __init__(self):
        self._fit_res = None
        self._cols = None

    def fit(self, X: pd.DataFrame, y: pd.Series) -> "HARModel":
        self._cols = list(X.columns)
        Xc = sm.add_constant(X, has_constant="add")
        self._fit_res = sm.OLS(y, Xc, missing="drop").fit()
        return self

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        X = X[self._cols]
        Xc = sm.add_constant(X, has_constant="add")
        return self._fit_res.predict(Xc).to_numpy()
