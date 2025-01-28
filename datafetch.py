import yfinance as yf
import pandas as pd
from pymongo import MongoClient

def fetch_data():
    reliance_stock=yf.Ticker("RELIANCE.NS")
    stock_history=reliance_stock.history("1mo")
    stock_history.reset_index(inplace=True)
    sorted_stock_data=stock_history.sort_values(by='Date',ascending=False)
    #Fetching the Date Column and converting the Date Col datatype (Date) to String
    sorted_stock_data['StockId']=sorted_stock_data['Date'].dt.date.astype(str)
    sorted_stock_data['StockId']=sorted_stock_data["StockId"]+"RELIANCE.NS"
    #Placing the Unique ID in the first column
    stock_date_col = sorted_stock_data.pop("StockId")  
    sorted_stock_data.insert(0, "Stock_Id", stock_date_col) 
    print(sorted_stock_data)
    return sorted_stock_data   
    #sorted_stock_data.to_csv("RelianceIndustries.csv",index=False)


if __name__=="__main__":
    sorted_stock_data=fetch_data()
    










