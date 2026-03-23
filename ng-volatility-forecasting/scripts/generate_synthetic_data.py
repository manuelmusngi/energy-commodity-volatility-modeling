import numpy as np
import pandas as pd
from pathlib import Path

def main():
    data_dir = Path("data/raw")
    data_dir.mkdir(parents=True, exist_ok=True)

    np.random.seed(42)

    start, end = "2023-01-01", "2024-12-31"
    dates_daily = pd.date_range(start, end, freq="D")
    dates_weekly = pd.date_range(start, end, freq="W-FRI")

    t = np.arange(len(dates_daily))
    season = 0.5 * np.sin(2 * np.pi * t / 365)
    noise = np.random.normal(scale=0.08, size=len(dates_daily))
    spot = 3.5 + season + np.cumsum(noise) * 0.02
    spot = np.clip(spot, 1.5, 10.0)

    pd.DataFrame({"date": dates_daily, "spot": spot}).to_csv(data_dir / "ng_prices.csv", index=False)

    curve = pd.DataFrame({"date": dates_daily})
    for m in range(1, 13):
        curve[f"M{m}"] = spot + 0.02 * (m - 6) + np.random.normal(scale=0.03, size=len(dates_daily))
    curve.to_csv(data_dir / "ng_futures_curve.csv", index=False)

    tw = np.arange(len(dates_weekly))
    storage = 3000 + 400 * np.sin(2 * np.pi * (tw - 30) / 365) + np.random.normal(scale=30, size=len(dates_weekly))
    pd.DataFrame({"date": dates_weekly, "storage": storage}).to_csv(data_dir / "storage_eia_weekly.csv", index=False)

    prod = 98 + 0.3 * np.sin(2 * np.pi * tw / 365) + np.random.normal(scale=0.3, size=len(dates_weekly))
    demand = 110 + 5 * np.sin(2 * np.pi * (tw - 20) / 365) + np.random.normal(scale=1.0, size=len(dates_weekly))
    lng = 12 + 0.5 * np.sin(2 * np.pi * (tw - 10) / 365) + np.random.normal(scale=0.2, size=len(dates_weekly))
    pd.DataFrame({"date": dates_weekly, "prod": prod, "demand": demand, "lng_exports": lng}).to_csv(
        data_dir / "fundamentals_balances.csv", index=False
    )

    hdd = 25 + 15 * np.sin(2 * np.pi * (t - 15) / 365) + np.random.normal(scale=3, size=len(dates_daily))
    cdd = 10 + 15 * np.sin(2 * np.pi * (t - 200) / 365) + np.random.normal(scale=3, size=len(dates_daily))
    hdd = np.clip(hdd, 0, None)
    cdd = np.clip(cdd, 0, None)
    pd.DataFrame({"date": dates_daily, "hdd": hdd, "cdd": cdd}).to_csv(data_dir / "weather_degree_days.csv", index=False)

    print("Synthetic data generated in data/raw/")

if __name__ == "__main__":
    main()
