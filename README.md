#### 🌐 Natural Gas Volatility Forecasting Inference

![Repo](https://img.shields.io/badge/repo-energy--commodity--volatility--modeling-171717?logo=github)
![Domain](https://img.shields.io/badge/domain-Natural%20Gas%20Volatility-0b7285)
![Market](https://img.shields.io/badge/market-Henry%20Hub-1864ab)
![Focus](https://img.shields.io/badge/focus-Forecasting%20Inference-5c7cfa)

A research‑driven, production‑ready analytics framework for forecasting natural gas volatility and translating market signals into hedge timing and risk insights for decision-making.  

This project integrates fundamentals, storage dynamics, and market structure into a modular Python pipeline designed for quantitative research, risk management, and trading decision support.


#### 📌 Project Objective
Build an end‑to‑end volatility forecasting system that:
- Models natural gas price uncertainty using historical and forward‑looking signals
- Identifies volatility regimes relevant for hedge timing
- Bridges academic research and real‑world risk workflows


#### 🧠 Research Reference Foundation
Grounded in peer‑reviewed and working‑paper literature on natural gas markets, storage dynamics, and volatility modeling, including:

- Stochastic Path‑Dependent Volatility Models for Price‑Storage Dynamics in Natural Gas Markets (arXiv)

  [Stochastic Path-Dependent Volatility Models for Price-Storage Dynamics in Natural Gas Markets and Discrete-Time Swing Option Pricing](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/Natural%20Gas%20Markets%20and%20Discrete-Time%20.pdf)
  
- Academic and SSRN research on storage surprises, fundamentals, and hedging effectiveness
 
  [Natural gas price, market fundamentals and hedging effectiveness](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/Natural%20Gas%20Price%2C%20Market%20Fundamentals%20and%20Hedging%20Effectiveness.pdf )

  [Optimal Hedging Strategies for Natural Gas](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/Optimal_Hedging_Strategies_for_Natural_Gas.pdf)
   
The implementation reflects a reduced‑form, data‑driven interpretation of these models suitable for operational use.


All analytics are orchestrated within a single, fully documented Jupyter notebook, making the project easy to review, extend, and adapt.

#### 🚀 Key Takeaway
This repository demonstrates how academic volatility concepts can be transformed into a practical hedge‑timing and risk analytics tool for natural gas markets—balancing rigor, interpretability, and operational relevance.

#### 🏗️ Project Architecture
ng-volatility-forecasting/\
├── README.md\
├── [pyproject.toml](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/pyproject.toml)\
├── config/\
│   ├── [data_sources.yaml](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/pyproject.toml)\
│   ├── [features.yaml](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/config/features.yaml)\
│   ├── [models.yaml](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/config/models.yaml)\
│   └── [backtest.yaml](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/config/backtest.yaml)\
├── data/\
│   ├── raw/\
│   ├── interim/\
│   └── processed/\
├── notebooks/\
│   └── ng_volatility_pipeline.ipynb\
├── scripts/\
│   ├── download_data.py\
│   ├── generate_synthetic_data.py\
│   └── run_pipeline.py\
├── src/\
│   └── ng_vol/\
│       ├── [__init__.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/init.py)\
│       ├── config/\
│       │   └── [loader.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/config/loader.py)\
│       ├── io/\
│       │   ├── [ingestion.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/io/ingestion.py)\
│       │   └── [validation.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/io/validation.py)\
│       ├── preprocessing/\
│       │   └── [align.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/preprocessing/align.py)\
│       ├── features/\
│       │   ├── [volatility.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/features/volatility.py)\
│       │   ├── [curve.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/features/curve.py)\
│       │   ├── [storage.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/features/storage.py)\
│       │   └── [weather.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/features/weather.py)\
│       ├── models/\
│       │   ├── [base.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/models/base.py)\
│       │   ├── [har.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/models/har.py)\
│       │   └── [tree.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/models/tree.py)\
│       ├── forecasting/\
│       │   └── [engine.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/forecasting/engine.py)\
│       ├── regimes/\
│       │   └── [classifier.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/regimes/classifier.py)\
│       ├── risk/\
│       │   └── [pnl_proxy.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/risk/pnl_proxy.py)\
│       ├── reporting/\
│       │   └── [plots.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/reporting/plots.py)\
│       └── [pipeline.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/src/ng_vol/pipeline.py)\
└── tests/\
    ├── [test_ingestion.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/tests/test_ingestion.py)\
    ├── [test_features.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/tests/test_features.py)\
    └── [test_models.py](https://github.com/manuelmusngi/energy-commodity-volatility-modeling/blob/main/ng-volatility-forecasting/tests/test_models.py)


#### License
This project is licensed under the [MIT License](https://github.com/manuelmusngi/regime_switching_models/edit/main/LICENSE).
