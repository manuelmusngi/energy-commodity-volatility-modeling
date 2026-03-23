import numpy as np
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error

def oos_forecast(
    model,
    X: pd.DataFrame,
    y: pd.Series,
    cv_splits: int,
) -> tuple[pd.Series, list[float]]:
    tscv = TimeSeriesSplit(n_splits=cv_splits)
    preds = pd.Series(index=y.index, dtype=float)
    rmses: list[float] = []

    for tr, te in tscv.split(X):
        Xtr, Xte = X.iloc[tr], X.iloc[te]
        ytr, yte = y.iloc[tr], y.iloc[te]

        model.fit(Xtr, ytr)
        p = model.predict(Xte)
        preds.iloc[te] = p

        rmse = mean_squared_error(yte, p, squared=False)
        rmses.append(float(rmse))

    return preds, rmses
