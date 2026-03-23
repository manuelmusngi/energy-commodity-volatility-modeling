import os
import requests
import pandas as pd
from pathlib import Path

def fetch_json(url: str) -> dict:
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    return r.json()

def main():
    data_dir = Path("data/raw")
    data_dir.mkdir(parents=True, exist_ok=True)

    eia_key = os.getenv("EIA_API_KEY", "").strip()
    if not eia_key:
        raise RuntimeError("Set EIA_API_KEY env var to use download_data.py")

    # NOTE: Replace series IDs with the exact ones you choose for your pipeline.
    # This script is a template that enforces schema + output filenames.

    # Example: Henry Hub spot (placeholder series)
    url_spot = f"https://api.eia.gov/v2/natural-gas/pri/sum/data/?api_key={eia_key}&frequency=daily&data[0]=value"
    js = fetch_json(url_spot)
    df = pd.DataFrame(js["response"]["data"]).rename(columns={"period": "date", "value": "spot"})
    df["date"] = pd.to_datetime(df["date"])
    df.sort_values("date").to_csv(data_dir / "ng_prices.csv", index=False)

    print("Downloaded ng_prices.csv (verify series IDs in script).")

if __name__ == "__main__":
    main()
