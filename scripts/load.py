# Load means:

    # Save processed data to storage


def load(df):
    df.to_csv("data/processed_sales.csv", index=False)
