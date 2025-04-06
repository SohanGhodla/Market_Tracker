from scraper_comodities import get_comodity_data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# from key_dates import important_dates
import argparse
import matplotlib.dates as mdates

# Set the default tick label size
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
# plt.rcParams['axes.titlesize'] = 12

if __name__ == "__main__":
    # List the stock/commodity symbols (check yfinance documentation for what's available) 
    tickers = ['GC=F', 'SI=F', 'CL=F', 'NG=F', 'ZW=F', 'LIT']
    handles = ['Gold', 'Silver', 'Crude Oil','Natural Gas', 'Wheat', 'Lithium (composit)']

    parser = argparse.ArgumentParser(description="To fetch please provide the following parameters.")
    parser.add_argument("--period", type=str, default="6y", help="Period of historical data (e.g., '1y', '1mo', '1d')")
    parser.add_argument("--interval", type=str, default="1mo", help="Interval of data (e.g., '1mo', '1d', '1h')")
    args = parser.parse_args()

    period = args.period
    interval = args.interval
    
    # Fetch data for each ticker and store them
    comodity_data = []
    comodity_attributes = []
    for ticker in tickers:
        data, attribute = get_comodity_data(ticker, period=period, interval=interval)
        if data is None or data.empty:
            print(f"No data retrieved for {ticker}.")
        else:
            comodity_data.append(data)
            comodity_attributes.append(attribute)
            
    # -------------------------------
    # Create a subplot for each ticker
    # -------------------------------
    n = len(comodity_data)
    fig, axes = plt.subplots(int(n/2), 2, figsize=(6 * 2, n))
    
    if n == 1:
        axes = [axes] # If there's only one subplot, ensure axes is iterable
    else:
        axes = axes.flatten()  # To make the 2D axes array into 1D for the below loop

    for i, (ax, ticker, data, attribute) in enumerate(zip(axes, tickers, comodity_data, comodity_attributes)):
        if period[1:] == 'mo': 
            # To have the x-labels less crowded drops the year
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
            
        ax.plot(data.index, data['Close'], label = handles[i])

        # Converting index to datetime
        data.index = pd.to_datetime(data.index)
        data.index = data.index.tz_convert(None)

        ax.set_xlabel('Time')
        ax.set_ylabel('Close Price [USD]')
        ax.set_title(f'{ticker} [Last {period}]')
        ax.legend(frameon = False, loc = 'upper left')
        ax.grid(True, linestyle = '--', alpha = 0.5)
    
    plt.tight_layout()
    plt.show()
