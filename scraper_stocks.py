import yfinance as yf

def get_stock_data(ticker, period='3mo', interval='1d'):
    """
    Fetch stock data using yfinance.

    Parameters:
        ticker (str): Stock symbol 
        period (str): Data period 
        interval (str): Data interval

    Returns:
        pd.DataFrame: Historical stock data.
        stock_attributes: Like market cap and Price to earning ratio (P/E)
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    info = stock.info

    market_cap = info.get("marketCap")
    pe_ratio = info.get("trailingPE")
    current_price = info.get("regularMarketPrice")
    last_close = info.get("previousClose")
    
    # Build a custom label with the extra info
    stock_attributes = (
                        f"Market Cap: ${market_cap/1e9:.1f}B\n"
                        f"P/E: {pe_ratio:.1f}\n"
                        f"Cur Price: ${current_price:.1f}\n"
                        f"Last Close: ${last_close:.1f}"
                    )
    
    return data, stock_attributes
