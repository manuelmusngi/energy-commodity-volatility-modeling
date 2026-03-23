import pandas as pd
import numpy as np

from ng_vol.models.har import HARModel
from ng_vol.models.tree import RFVolModel

def test_har_fit_predict_shapes():
    X = pd.DataFrame({"rv_5d": np.random.rand(50), "rv_10d": np.random.rand(50)})
    y = pd.Series(np.random.rand(50))
    m = HARModel().fit(X, y)
    p = m.predict(X.iloc[:10])
    assert p.shape == (10,)

def test_rf_fit_predict_shapes():
    X = pd.DataFrame({"a": np.random.rand(50), "b": np.random.rand(50)})
    y = pd.Series(np.random.rand(50))
    m = RFVolModel(n_estimators=10, max_depth=3, random_state=42).fit(X, y)
    p = m.predict(X.iloc[:10])
    assert p.shape == (10,)
