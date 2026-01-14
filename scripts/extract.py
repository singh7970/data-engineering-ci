# Extract means:

# Reading data from a source (CSV, DB, API)



import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "sales.csv"

def extract():
    return pd.read_csv(DATA_PATH)
