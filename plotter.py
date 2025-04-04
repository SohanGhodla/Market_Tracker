import matplotlib.pyplot as plt

def plot_stock_data(data, ticker):
    """
    Plot the closing price of the stock.

    Parameters:
        data (pd.DataFrame): DataFrame containing stock data.
        ticker (str): Stock symbol for labeling the plot.
    """
    if data is None or data.empty:
        print(f"No data to plot for {ticker}")
        return

    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label=f'{ticker} Close Price')
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.title(f'{ticker} Stock Price Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()
