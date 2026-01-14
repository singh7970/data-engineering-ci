# Extract means:

# Reading data from a source (CSV, DB, API)




# import pandas as pd

# def extract():
#     return pd.read_csv("data/sales.csv")


import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "sales.csv"

EXPECTED_COLUMNS = ["order_id", "order_date", "amount", "city"]

def extract():
    df = pd.read_csv(DATA_FILE)

    # 🔧 NORMALIZE COLUMN NAMES (CRITICAL)
    df.columns = (
        df.columns
        .str.strip()      # remove leading/trailing spaces
        .str.lower()      # standardize case
    )

    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # enforce column order
    df = df[EXPECTED_COLUMNS]

    return df
