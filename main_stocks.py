from src.scraper_stocks import get_stock_data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from src.key_dates import important_dates
import argparse
import matplotlib.dates as mdates

# Set the default tick label size
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
# plt.rcParams['axes.titlesize'] = 12

if __name__ == "__main__":
    # List the stock/commodity symbols (check yfinance documentation for what's available)
    tickers = ['AAPL', 'AMZN', 'GOOGL', 'META', 'MSFT', 'NFLX', 'NVDA', 'TSLA'] 

    parser = argparse.ArgumentParser(description="To fetch please provide the following parameters.")
    parser.add_argument("--period", type=str, default="6y", help="Period of historical data (e.g., '1y', '1mo', '1d')")
    parser.add_argument("--interval", type=str, default="1d", help="Interval of data (e.g., '1mo', '1d', '1h')")
    args = parser.parse_args()

    period = args.period
    interval = args.interval
    
    # Fetch data for each ticker and store them
    stock_data = []
    stock_attributes = []
    for ticker in tickers:
        data, attribute = get_stock_data(ticker, period=period, interval=interval)
        if data is None or data.empty:
            print(f"No data retrieved for {ticker}.")
        else:
            stock_data.append(data)
            stock_attributes.append(attribute)
            
    # -------------------------------
    # Create a subplot for each ticker
    # -------------------------------
    n = len(stock_data)
    fig, axes = plt.subplots(int(n/2), 2, figsize=(6 * 2, n))
    
    if n == 1:
        axes = [axes] # If there's only one subplot, ensure axes is iterable
    else:
        axes = axes.flatten()  # To make the 2D axes array into 1D for the below loop

    for i, (ax, ticker, data, attribute) in enumerate(zip(axes, tickers, stock_data, stock_attributes)):
        if period[1:] == 'mo': 
            # To have the x-labels less crowded drops the year
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

        ax.plot(data.index, data['Close'], label = attribute)

        # Converting index to datetime
        data.index = pd.to_datetime(data.index)
        data.index = data.index.tz_convert(None)

        # Add vertical lines and labels
        for label, date in important_dates.items():
            if data.index.min() <= date <= data.index.max(): # To ensure that the date within range
                ylim = ax.get_ylim()
                # To plot vertical line
                ax.axvline(date, color='gray', linestyle=':', alpha=0.7, linewidth = 1.5)
                # place text on RHS of the line
                span = data.index.max() - data.index.min() # this is a Timedelta
                offsetx = span * 0.01  
                offsety = 0.1 * (ylim[1] - ylim[0])
                if i == 0:
                    ax.text(date + offsetx, ylim[0] + offsety, label,
                            rotation=90, fontsize=8, color='red')

        ax.set_xlabel('Time')
        ax.set_ylabel('Price [USD]')
        ax.set_title(f'{ticker} [Last {period}]')
        ax.legend(frameon = False, handlelength=0, loc = 'upper left')
        ax.grid(True, linestyle = '--', alpha = 0.5)
    
    plt.tight_layout()
    plt.show()
