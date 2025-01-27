import yfinance as yf
import pandas as pd

reliance_stock=yf.Ticker("RELIANCE.NS")
stock_history=reliance_stock.history("1mo")
sorted_stock_data=stock_history.sort_values(by='Date',ascending=False)
print(sorted_stock_data)
sorted_stock_data.to_csv("RelianceIndustries.csv",index=False)








