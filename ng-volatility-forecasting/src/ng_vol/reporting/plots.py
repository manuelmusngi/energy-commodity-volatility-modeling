import matplotlib.pyplot as plt
import pandas as pd

def plot_forecast_vs_realized(df: pd.DataFrame, pred_col: str, real_col: str, title: str = "") -> None:
    fig, ax = plt.subplots(figsize=(12, 4))
    df[pred_col].plot(ax=ax, label="forecast")
    df[real_col].plot(ax=ax, label="realized", alpha=0.7)
    ax.set_title(title or "Forecast vs realized")
    ax.legend()
    plt.show()
