import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from .base import VolModel

class RFVolModel(VolModel):
    def __init__(self, **params):
        self.model = RandomForestRegressor(**params)

    def fit(self, X: pd.DataFrame, y: pd.Series) -> "RFVolModel":
        self.model.fit(X, y)
        return self

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        return self.model.predict(X)
