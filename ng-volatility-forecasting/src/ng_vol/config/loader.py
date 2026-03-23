from pathlib import Path
import yaml

def load_yaml(path: Path) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)

def load_all_configs(config_dir: Path) -> dict:
    return {
        "data": load_yaml(config_dir / "data_sources.yaml"),
        "features": load_yaml(config_dir / "features.yaml"),
        "models": load_yaml(config_dir / "models.yaml"),
        "backtest": load_yaml(config_dir / "backtest.yaml"),
    }
