import requests
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

EIA_API_KEY = "YOUR_EIA_API_KEY"   # <-- insert your key here

# -----------------------------
# Helper: GET request wrapper
# -----------------------------
def fetch_json(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.json()

# -----------------------------
# 1. Henry Hub Spot Prices
# -----------------------------
def download_henry_hub_spot():
    url = (
        f"https://api.eia.gov/v2/natural-gas/pri/fut/data/"
        f"?api_key={EIA_API_KEY}&frequency=daily&data[0]=value"
        f"&facets[series][]=NG.RNGWHHD.D"
    )
    js = fetch_json(url)
    df = pd.DataFrame(js["response"]["data"])
    df = df.rename(columns={"period": "date", "value": "spot"})
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    df.to_csv(DATA_DIR / "ng_prices.csv", index=False)
    print("Saved ng_prices.csv")

# -----------------------------
# 2. EIA Weekly Storage
# -----------------------------
def download_storage():
    url = (
        f"https://api.eia.gov/v2/natural-gas/stor/wkly/data/"
        f"?api_key={EIA_API_KEY}&frequency=weekly&data[0]=value"
        f"&facets[series][]=NG.WKSTORAGE.W"
    )
    js = fetch_json(url)
    df = pd.DataFrame(js["response"]["data"])
    df = df.rename(columns={"period": "date", "value": "storage"})
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    df.to_csv(DATA_DIR / "storage_eia_weekly.csv", index=False)
    print("Saved storage_eia_weekly.csv")

# -----------------------------
# 3. EIA Fundamentals (Production, Demand, LNG)
# -----------------------------
def download_fundamentals():
    url = (
        f"https://api.eia.gov/v2/natural-gas/ngs/dry/data/"
        f"?api_key={EIA_API_KEY}&frequency=weekly&data[0]=value"
    )
    js = fetch_json(url)
    df = pd.DataFrame(js["response"]["data"])
    df = df.rename(columns={"period": "date", "value": "prod"})
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    # Demand
    url_demand = (
        f"https://api.eia.gov/v2/natural-gas/ngs/cons/data/"
        f"?api_key={EIA_API_KEY}&frequency=weekly&data[0]=value"
    )
    js_d = fetch_json(url_demand)
    df_d = pd.DataFrame(js_d["response"]["data"])
    df_d = df_d.rename(columns={"period": "date", "value": "demand"})
    df_d["date"] = pd.to_datetime(df_d["date"])

    # LNG feedgas
    url_lng = (
        f"https://api.eia.gov/v2/natural-gas/ngs/lng/data/"
        f"?api_key={EIA_API_KEY}&frequency=weekly&data[0]=value"
    )
    js_l = fetch_json(url_lng)
    df_l = pd.DataFrame(js_l["response"]["data"])
    df_l = df_l.rename(columns={"period": "date", "value": "lng_exports"})
    df_l["date"] = pd.to_datetime(df_l["date"])

    # Merge
    df_all = df.merge(df_d, on="date", how="outer").merge(df_l, on="date", how="outer")
    df_all = df_all.sort_values("date")
    df_all.to_csv(DATA_DIR / "fundamentals_balances.csv", index=False)
    print("Saved fundamentals_balances.csv")

# -----------------------------
# 4. NOAA HDD/CDD (Daily)
# -----------------------------
def download_noaa_weather():
    # NOAA API does not require a key for basic HDD/CDD
    url = (
        "https://www.ncei.noaa.gov/access/services/data/v1?"
        "dataset=daily-summaries&stations=USW00012960&dataTypes=HDD,CDD&format=json"
    )
    js = fetch_json(url)
    df = pd.DataFrame(js)
    df = df.rename(columns={"DATE": "date", "HDD": "hdd", "CDD": "cdd"})
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    df.to_csv(DATA_DIR / "weather_degree_days.csv", index=False)
    print("Saved weather_degree_days.csv")

# -----------------------------
# Run all downloads
# -----------------------------
if __name__ == "__main__":
    download_henry_hub_spot()
    download_storage()
    download_fundamentals()
    download_noaa_weather()
    print("All datasets downloaded.")
