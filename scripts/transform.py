# Transform means:

# Cleaning, standardizing, enriching data


def transform(df):
    df["amount"] = df["amount"].fillna(0)
    df["city"] = df["city"].str.upper()
    return df
