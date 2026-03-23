 import pandas as pd

def classify_by_quantiles(
    series: pd.Series,
    q_low: float,
    q_high: float,
    labels: dict,
) -> pd.Series:
    lo = series.quantile(q_low)
    hi = series.quantile(q_high)

    def _lab(x: float) -> str:
        if x <= lo:
            return labels["low"]
        if x <= hi:
            return labels["medium"]
        return labels["high"]

    return series.apply(_lab)
