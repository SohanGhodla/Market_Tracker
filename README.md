# Project Setup Instructions

## Prerequisites

This package requires ``Python 3.8.x``. Using ``Python 3.8.16`` is recommended for best compatibility on modern macOS systems.

### Installing Python 3.8.x with pyenv

If you don't have pyenv installed, first install it via Homebrew:
```bash
brew install pyenv
```

Next, install Python 3.8.16
```bash
pyenv install 3.8.16
```

Next, navigate to your directory and set the local directory to use Python 3.8.16
```bash
pyenv local 3.8.16
```

## Installation  

To install the requirements for this project, follow these steps:
1. **Best to first create a virtual environment**  
   Run the following command:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. **To install the requirements**  
   Run the following command:
    ```bash
    pip install -r requirements.txt
    ```
3. **To run the script**  
   Choose which (forex, stocks, commodities, crypto) script you want to run. Then
   ```bash
   Replace <script> below with your script’s filename (e.g. main_stocks.py) 
   Replace <period> and <interval> with valid yfinance values:
      - period: 1d, 5d, 1mo, 6mo, 1y, 5y, etc.
      - interval: 1m, 5m, 15m, 1h, 1d, 1wk, etc.
   
   python <script> --period <period> --interval <interval>
   ```


