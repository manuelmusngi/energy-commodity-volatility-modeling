from pathlib import Path
from ng_vol.pipeline import run

def main():
    out = run(
        config_dir=Path("config"),
        save_outputs=True,
    )
    print("Pipeline complete.")
    print({k: str(v) for k, v in out.items()})

if __name__ == "__main__":
    main()
