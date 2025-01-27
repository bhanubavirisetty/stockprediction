import yfinance as yf
import pandas as pd
from pymongo import MongoClient

def fetch_data():
    reliance_stock=yf.Ticker("RELIANCE.NS")

    stock_history=reliance_stock.history("1mo")
    stock_history.reset_index(inplace=True)

    sorted_stock_data=stock_history.sort_values(by='Date',ascending=False)

    return sorted_stock_data
    
    #sorted_stock_data.to_csv("RelianceIndustries.csv",index=False)


if __name__=="__main__":
    sorted_stock_data=fetch_data()
    print(sorted_stock_data)






