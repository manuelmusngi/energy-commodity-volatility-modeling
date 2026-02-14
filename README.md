#### 🌐 Natural Gas Volatility Forecasting & Hedge Timing

A **research‑driven, production‑ready analytics framework** for forecasting natural gas volatility and translating market signals into hedge timing and risk insights for decision-making.  

This project integrates **fundamentals, storage dynamics, and market structure** into a modular Python pipeline designed for quantitative research, risk management, and trading decision support.


#### 📌 Project Objective
Build an end‑to‑end volatility forecasting system that:
- Models **natural gas price uncertainty** using historical and forward‑looking signals
- Identifies **volatility regimes** relevant for hedge timing
- Bridges **academic research** and **real‑world risk workflows**


#### 🧠 Research Reference Foundation
Grounded in peer‑reviewed and working‑paper literature on natural gas markets, storage dynamics, and volatility modeling, including:

- **Stochastic Path‑Dependent Volatility Models for Price‑Storage Dynamics in Natural Gas Markets** (arXiv)

  [Stochastic Path-Dependent Volatility Models for Price-Storage Dynamics in Natural Gas Markets and Discrete-Time Swing Option Pricing](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/Natural%20Gas%20Markets%20and%20Discrete-Time%20.pdf)
  
- Academic and SSRN research on **storage surprises, fundamentals, and hedging effectiveness**
 
  [Natural gas price, market fundamentals and hedging effectiveness](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/Natural%20Gas%20Price%2C%20Market%20Fundamentals%20and%20Hedging%20Effectiveness.pdf )

  [Optimal Hedging Strategies for Natural Gas](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/Optimal_Hedging_Strategies_for_Natural_Gas.pdf)
   
The implementation reflects a **reduced‑form, data‑driven interpretation** of these models suitable for operational use.


All analytics are orchestrated within a **single, fully documented Jupyter notebook**, making the project easy to review, extend, and adapt.

#### 🚀 Key Takeaway
This repository demonstrates how **academic volatility concepts** can be transformed into a **practical hedge‑timing and risk analytics tool** for natural gas markets—balancing rigor, interpretability, and operational relevance.

*Built with reproducibility, modularity, and decision‑making impact in mind.*

#### 🧩 Pipeline Architecture
A modular, notebook‑centric design that mirrors production analytics systems:

 - [0. Notebook metadata](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/0.%20Notebook%20metadata)

 - [1. Imports, paths, and config](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/1.%20Imports%2C%20paths%2C%20and%20config)

- 📥 **Data Ingestion**  
  futures prices, futures curves, storage levels, fundamentals, and weather proxies
  
  [2. Data ingestion](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/2.%20Data%20ingestion)

- 🛠️ **Feature Engineering**  
  Realized volatility, curve shape metrics, storage surprises, and regime indicators

  [3. Feature engineering](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/3.%20Feature%20engineering)

- 📈 **Modeling & Forecasting**   
  Linear HAR‑style regressions and non‑linear machine learning models

  [4. Modeling and forecasting](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/4.%20Modeling%20and%20forecasting)

- 🔍 **Volatility Regimes**   
  Classification of low, medium, and high volatility environments

  [5. Volatility regimes and hedge timing](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/5.%20Volatility%20regimes%20and%20hedge%20timing)

- ⏱️ **Hedge Timing Logic**   
  Translating forecasts into actionable hedge bias signals

  [5. Volatility regimes and hedge timing](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/5.%20Volatility%20regimes%20and%20hedge%20timing)

- ⚖️ **Risk Interpretation**  
  Linking volatility forecasts to P&L dispersion and risk views

  [6. Risk view and simple P&L dispersion](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/6.%20Risk%20view%20and%20simple%20P%26L%20dispersion)


#### License
This project is licensed under the [MIT License](https://github.com/manuelmusngi/regime_switching_models/edit/main/LICENSE).
