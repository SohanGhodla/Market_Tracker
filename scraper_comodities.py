import yfinance as yf

def get_comodity_data(ticker, period='3mo', interval='1d'):
    """
    Fetch comodity data using yfinance.

    Parameters:
        ticker (str): Comodity symbol 
        period (str): Data period 
        interval (str): Data interval 

    Returns:
        pd.DataFrame: Historical comodity data.
    """
    comodity = yf.Ticker(ticker)
    data = comodity.history(period=period, interval=interval)
    info = comodity.info

    market_cap = info.get("marketCap")
    if market_cap is not None:
        attributes = f"Market Cap: ${market_cap/1e9:.1f}B"
    else:
        attributes = None

    
    return data, attributes
