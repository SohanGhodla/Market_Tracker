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
   Choose which (forex, stocks, commodities, crypto) script you want to run 
   ```bash
   python main_<your choice>.py --period <e.g., 1yr> --interval <e.g., 1d>
   ```

