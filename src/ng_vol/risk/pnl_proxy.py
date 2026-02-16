import numpy as np

def pnl_proxy(prices):
    return np.log(prices).diff()
