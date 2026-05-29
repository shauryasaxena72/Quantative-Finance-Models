# 📊 Index Risk Analyzer

> Quantitative Risk Engine for the Nifty 50 Index

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![yfinance](https://img.shields.io/badge/data-yfinance-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A quantitative risk analysis toolkit for the **Nifty 50 index** (`^NSEI`). Fetches live market data from Yahoo Finance and computes a full risk profile: volatility, Value at Risk, Conditional VaR, rolling risk windows, max drawdown, and 500-path Monte Carlo price simulations.

---

## Features

| Module | Description |
|---|---|
| 📈 Price Fetch | Downloads OHLCV data from Yahoo Finance (2020–2026) |
| 📉 Return Distribution | Daily % returns histogram |
| ⚡ Volatility | Daily volatility + annualised (×√252) |
| ⚠️ VaR (95%) | Historical Value at Risk at 5th percentile |
| 🔥 CVaR (95%) | Expected loss beyond the VaR threshold |
| 🔄 Rolling Volatility | 20-day rolling std dev window |
| 📉 Drawdown Analysis | Cumulative peak-to-trough drawdown chart |
| 🎲 Monte Carlo | 500-path GBM simulation, 30-day horizon |

---

## Installation

```bash
# Clone the repo
git clone https://github.com/your-username/nifty-risk-analyzer.git
cd nifty-risk-analyzer

# Install dependencies
pip install yfinance pandas numpy matplotlib

# Run
python nifty_risk.py
```

---

## Dependencies

| Package | Purpose | Version |
|---|---|---|
| `yfinance` | Market data from Yahoo Finance | ≥ 0.2 |
| `pandas` | Time-series manipulation | ≥ 1.5 |
| `numpy` | Numerical simulation engine | ≥ 1.24 |
| `matplotlib` | Charts and visualisations | ≥ 3.7 |

---

## How It Works

### 1. Data Fetch
Downloads closing prices for `^NSEI` from Yahoo Finance.

### 2. Return Calculation
```python
returns = prices.pct_change().dropna()
```

### 3. Volatility
```python
volatility        = returns.std()
volatility_annual = volatility * (252 ** 0.5)
```

### 4. Value at Risk (VaR)
95% historical VaR — the worst loss on 95% of trading days:
```python
var = returns.quantile(0.05)
```

### 5. Conditional VaR (CVaR)
Expected loss in the worst 5% of scenarios:
```python
cvar = returns[returns <= var].mean()
```

### 6. Rolling Volatility
20-day rolling standard deviation window to capture regime changes.

### 7. Drawdown Analysis
```python
cumulative_returns = (1 + returns).cumprod()
peak     = cumulative_returns.cummax()
drawdown = (cumulative_returns - peak) / peak
max_drawdown = drawdown.min()
```

### 8. Monte Carlo Simulation
500 independent GBM paths, each 30 days forward from the last known price:
```python
random_return = np.random.normal(mean, std)
price = price * (1 + random_return)
```
Outputs worst-case, best-case, and average projected prices.

---

## Sample Output (Nifty 50, 2020–2026)

```
Mean Return:       ~0.06% / day
Volatility:        ~1.1% / day
Annual Volatility: ~17–19%
VaR (95%):         ~ -1.6%
CVaR (95%):        ~ -2.5%
Max Drawdown:      ~ -38%  (March 2020 crash)
```

> Results vary with live data. Figures above are indicative only.

---

## Project Structure

```
Index Risk Analyzer/
├── main.py   # Main script — all logic
├── README.md       # This file
└── LICENSE         # MIT License
```

---

## Roadmap

- [ ] Multi-index support (Bank Nifty, Sensex)
- [ ] Sharpe & Sortino ratio
- [ ] Parametric VaR (normal + t-distribution)
- [ ] Export results to CSV / PDF report
- [ ] Streamlit dashboard UI

---

## Disclaimer

> This project is for **educational and research purposes only**.  
> Nothing here constitutes financial advice.  
> Past index performance does not guarantee future results.

---

## License

MIT © 2024 — fork it, build on it, dominate with it.
