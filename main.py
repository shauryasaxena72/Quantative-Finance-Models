import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Getting nifty data

ticker='^NSEI'
data=yf.download(ticker,start='2020-01-01',end='2026-01-01')

# Taking only closing price

prices=data['Close']
prices.plot(title="Index Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

# Getting returns in percentage change and removing missing val

returns=prices.pct_change()
returns=returns.dropna()
print(returns.head())
returns.hist(bins=50)
plt.xlabel("Returns")
plt.ylabel("Frequency")
plt.title("Returns Distribution")
plt.show()


# Calculating Volatility and Annual Volatility

volatility=returns.std()
print("Volatility = ",volatility)
volatility_annual=volatility*(252**0.5)
print("Volatility Annual = ",volatility_annual)

# Calculating VaR ( Value at Risk )

var=returns.quantile(0.05)
print("Value at Risk = ",var)

# Calculating CVaR

cvar=returns[returns <= var].mean()
print("Conditional Value at Risk = ",cvar)

# Calculating Rolling Volatility

rolling_volatility=returns.rolling(window=20).std()
rolling_volatility=rolling_volatility.dropna()
print(rolling_volatility.head())
rolling_volatility.plot(title="Rolling Volatility")
plt.show()

# Drawdown Analysis

cumulative_returns = (1 + returns).cumprod()
peak = cumulative_returns.cummax()
drawdown = (cumulative_returns - peak) / peak
max_drawdown = drawdown.min()
print("Maximum Drawdown = ",max_drawdown)
drawdown.plot(title="Drawdown")
plt.show()

# Monte Carlo Simulation

days = 30
simulations = 500
last_price = prices.iloc[-1]
mean = returns.mean()
std = returns.std()
simulated_prices = []
for i in range(simulations):
    price = last_price
    path = []
    for d in range(days):
        random_return = np.random.normal(mean, std)
        price = price * (1 + random_return)
        path.append(price)
    simulated_prices.append(path)
simulated_prices = np.array(simulated_prices)
print(simulated_prices.shape)
final_prices = simulated_prices[:, -1]
print("Worst Case:", final_prices.min())
print("Best Case:", final_prices.max())
print("Average Case:", final_prices.mean())
plt.figure(figsize=(10,6))
for i in range(50):
    plt.plot([last_price] + list(simulated_prices[i]))
plt.title("Monte Carlo Simulation (30 Days Forecast)")
plt.xlabel("Days")
plt.ylabel("Price")
plt.grid()
plt.show()
print("\n--- SUMMARY ---")
print("Mean Return:", returns.mean())
print("Volatility:", volatility)
print("Annual Volatility:", volatility_annual)
print("VaR (95%):", var)
print("CVaR (95%):", cvar)
print("Max Drawdown:", max_drawdown)