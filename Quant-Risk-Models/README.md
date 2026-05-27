# 📊 Quant Risk Management System

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Quant Finance](https://img.shields.io/badge/Domain-Quant%20Finance-orange)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

A quantitative finance project built in Python to analyze and measure market risk using historical data from the NIFTY 50 index.  
The system calculates important financial risk metrics and performs Monte Carlo simulations to model possible future market scenarios.

---

# 🚀 Features

- Historical market data collection using Yahoo Finance
- Daily returns calculation
- Volatility & Annualized Volatility
- Value at Risk (VaR)
- Conditional Value at Risk (CVaR / Expected Shortfall)
- Rolling Volatility Analysis
- Drawdown Analysis
- Monte Carlo Simulation
- Data Visualization with Matplotlib

---

# 📂 Project Workflow

```text
Fetch Historical Data
        ↓
Extract Closing Prices
        ↓
Calculate Daily Returns
        ↓
Compute Volatility Metrics
        ↓
Calculate VaR & CVaR
        ↓
Analyze Rolling Volatility
        ↓
Perform Drawdown Analysis
        ↓
Run Monte Carlo Simulations
        ↓
Visualize Results
```

---

# 📊 Risk Metrics Used

## 🔹 Volatility
Measures how much the returns fluctuate over time.

---

## 🔹 Annualized Volatility
Annual representation of market volatility using 252 trading days.

---

## 🔹 Value at Risk (VaR)
Estimates the maximum expected loss at a 95% confidence level.

---

## 🔹 Conditional Value at Risk (CVaR)
Measures the average loss beyond the VaR threshold.

---

## 🔹 Drawdown
Calculates the decline from a historical peak in cumulative returns.

---

## 🔹 Monte Carlo Simulation
Generates multiple simulated future price paths using historical mean returns and volatility.

---

# 📈 Visualizations

The project generates:

- 📈 Index Price Trend
- 📊 Returns Distribution Histogram
- 📉 Rolling Volatility Chart
- 📉 Drawdown Curve
- 🎲 Monte Carlo Simulation Paths

---

# ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- yfinance

---

# 📦 Libraries Used

```python
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

---

# ▶️ Installation & Usage

## 1️⃣ Clone Repository

```bash
git clone <your-repository-link>
cd quant-risk-management-system
```

---

## 2️⃣ Install Dependencies

```bash
pip install yfinance pandas numpy matplotlib
```

---

## 3️⃣ Run Project

```bash
python main.py
```

---

# 🧠 Project Pipeline Explained

## Step 1: Fetch Historical Data

Historical NIFTY 50 data is collected using the yfinance library.

```python
ticker='^NSEI'
data=yf.download(ticker,start='2020-01-01',end='2026-01-01')
```

---

## Step 2: Extract Closing Prices

Only the closing prices are used for risk calculations.

```python
prices=data['Close']
```

---

## Step 3: Calculate Daily Returns

Percentage change is used to compute returns.

```python
returns=prices.pct_change()
returns=returns.dropna()
```

---

## Step 4: Calculate Volatility

Standard deviation of returns is used as volatility.

```python
volatility=returns.std()
```

Annualized volatility:

```python
volatility_annual=volatility*(252**0.5)
```

---

## Step 5: Calculate Value at Risk (VaR)

VaR estimates the worst expected daily loss at 95% confidence.

```python
var=returns.quantile(0.05)
```

---

## Step 6: Calculate Conditional VaR (CVaR)

CVaR measures the average loss beyond the VaR threshold.

```python
cvar=returns[returns <= var].mean()
```

---

## Step 7: Rolling Volatility Analysis

Rolling volatility measures changing market risk over time.

```python
rolling_volatility=returns.rolling(window=20).std()
```

---

## Step 8: Drawdown Analysis

Measures the maximum decline from peak cumulative returns.

```python
cumulative_returns = (1 + returns).cumprod()
peak = cumulative_returns.cummax()
drawdown = (cumulative_returns - peak) / peak
```

---

## Step 9: Monte Carlo Simulation

Simulates future market price paths using historical mean returns and volatility.

```python
random_return = np.random.normal(mean, std)
```

500 simulations are generated for 30 future trading days.

---

# 📊 Example Output

```text
Volatility = 0.012
Annual Volatility = 0.19
Value at Risk = -0.018
Conditional Value at Risk = -0.028
Maximum Drawdown = -0.38
Worst Case = 21000
Best Case = 28500
Average Case = 24500
```

---

# ⚠️ Limitations

- Assumes returns follow a normal distribution
- Based only on historical market data
- Does not account for extreme tail-risk events
- Single asset/index analysis only

---

# 🚀 Future Improvements

- Sharpe Ratio
- Beta & Correlation Analysis
- Portfolio Risk Management
- GARCH Volatility Modeling
- Interactive Streamlit Dashboard
- Multi-Asset Risk Analysis
- Real-Time Data Integration

---

# 💡 Motivation

This project was built to explore how quantitative finance techniques can be applied to:

- Measure financial risk
- Analyze market uncertainty
- Simulate future price behavior
- Understand downside risk in financial markets

It serves as a foundational project for quantitative finance, risk analytics, and algorithmic trading systems.

---

# 📎 License

This project is open-source and available for educational purposes.

---
