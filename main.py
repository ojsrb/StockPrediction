import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

symbol = "AAPL"

stock_data = yf.download(symbol, start="2010-01-01", end="2025-01-01")

stock_data["MA20"] = stock_data["Close"].rolling(window=20).mean()

print(stock_data.isnull().sum())

plt.figure(figsize=(12, 6))
plt.plot(stock_data["Close"], label="Close Price", color="blue")
plt.plot(stock_data["MA20"], label="MA20", color="red")
plt.title(f"{symbol} Stock Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()