import yfinance as yf
import pandas as pd

def get_stock_data(ticker, period='3mo', interval='1d'):
    """
    Fetch historical stock data using yfinance.

    Parameters:
        ticker (str): Stock symbol (e.g., 'AAPL')
        period (str): Data period (e.g., '3mo' for 3 months)
        interval (str): Data interval (e.g., '1d' for daily)

    Returns:
        pd.DataFrame: Historical stock data.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    return data
