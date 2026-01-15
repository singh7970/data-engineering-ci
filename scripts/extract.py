# Extract means:

# Reading data from a source (CSV, DB, API)




# import pandas as pd

# def extract():
#     return pd.read_csv("data/sales.csv")


# Configure logging once per module
import logging
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "sales.csv"

EXPECTED_COLUMNS = ["order_id", "order_date", "amount", "city"]

def extract():
    logging.info("Starting data extraction")
    df = pd.read_csv(DATA_FILE)

    # 🔧 NORMALIZE COLUMN NAMES (CRITICAL)
    df.columns = (
        df.columns
        .str.strip()      # remove leading/trailing spaces
        .str.lower()      # standardize case
    )

    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        logging.error(f"Missing columns: {missing_columns}")
        raise ValueError(f"Missing required columns: {missing}")

    # enforce column order
    df = df[EXPECTED_COLUMNS]
    logging.info("Data extraction completed successfully")

    return df
