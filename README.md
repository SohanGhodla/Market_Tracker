# Project Setup Instructions

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
   Replace <script> below with your script’s filename (e.g. main.py) 
   Replace <period> and <interval> with valid yfinance values:
      - period: 1d, 5d, 1mo, 6mo, 1y, 5y, etc.
      - interval: 1m, 5m, 15m, 1h, 1d, 1wk, etc.
   
   python <script> --period <period> --interval <interval>
   ```

