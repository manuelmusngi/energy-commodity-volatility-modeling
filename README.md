#### 🌐 Natural Gas Volatility Forecasting & Hedge Timing

A **research‑driven, production‑ready analytics framework** for forecasting natural gas volatility and translating market signals into actionable hedge timing and risk insights.  

This project integrates **fundamentals, storage dynamics, and market structure** into a modular Python pipeline designed for quantitative research, risk management, and trading decision support.


#### 📌 Project Objective
Build an end‑to‑end volatility forecasting system that:
- Models **natural gas price uncertainty** using historical and forward‑looking signals
- Identifies **volatility regimes** relevant for hedge timing
- Bridges **academic research** and **real‑world risk workflows**


#### 🧠 Research Foundation
Grounded in peer‑reviewed and working‑paper literature on natural gas markets, storage dynamics, and volatility modeling, including:

- **Stochastic Path‑Dependent Volatility Models for Price‑Storage Dynamics in Natural Gas Markets** (arXiv)

  [Stochastic Path-Dependent Volatility Models for Price-Storage Dynamics in Natural Gas Markets and Discrete-Time Swing Option Pricing](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/Natural%20Gas%20Markets%20and%20Discrete-Time%20.pdf)
  
- Academic and SSRN research on **storage surprises, fundamentals, and hedging effectiveness**
 
  [Natural gas price, market fundamentals and hedging effectiveness](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/Natural%20Gas%20Price%2C%20Market%20Fundamentals%20and%20Hedging%20Effectiveness.pdf )
   
The implementation reflects a **reduced‑form, data‑driven interpretation** of these models suitable for operational use.


#### 🧩 Pipeline Architecture
A modular, notebook‑centric design that mirrors production analytics systems:

    - - [0. Notebook metadata](https://github.com/manuelmusngi/Natural-Gas-Volatility-Forecasting-Hedge-Timing/blob/main/0.%20Notebook%20metadata)

- **Data Ingestion** 📥  
  Spot prices, futures curves, storage levels, fundamentals, and weather proxies

- **Feature Engineering** 🛠️  
  Realized volatility, curve shape metrics, storage surprises, and regime indicators

- **Modeling & Forecasting** 📈  
  Linear HAR‑style regressions and non‑linear machine learning models

- **Volatility Regimes** 🔍  
  Classification of low, medium, and high volatility environments

- **Hedge Timing Logic** ⏱️  
  Translating forecasts into actionable hedge bias signals

- **Risk Interpretation** ⚖️  
  Linking volatility forecasts to P&L dispersion and risk views


#### License
This project is licensed under the [MIT License](https://github.com/manuelmusngi/regime_switching_models/edit/main/LICENSE).
