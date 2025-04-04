from scraper import get_stock_data
from plotter import plot_stock_data

if __name__ == "__main__":
    # List the stock symbols you want to track
    tickers = ['AAPL', 'MSFT']  # You can add more tickers if needed
    period = '6mo'
    interval = '1d'

    for ticker in tickers:
        data = get_stock_data(ticker, period=period, interval=interval)
        if data is None or data.empty:
            print(f"No data retrieved for {ticker}.")
        else:
            plot_stock_data(data, ticker)
