import pandas as pd

important_dates = {
    'US Global Tariffs': '2025-04-02',
    'Rus‑Ukr War': '2022-02-24',
    'Isrl‑Gaza War': '2023-10-07',
    'COVID-19': '2019-12-01'
}
# Convert to timestamps in format e.g., 2025-04-05 00:00:00
important_dates = {k: pd.to_datetime(v) for k, v in important_dates.items()}
