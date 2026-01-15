# A data test verifies:

# Data meets business & technical rules

import pandas as pd 

from scripts.extract import extract

def test_order_id_not_null():
    df = extract()
    assert df["order_id"].isnull().sum() == 0



def test_order_id_is_unique():
    """
    order_id must be unique.
    Duplicate primary keys can cause double counting in analytics.
    """
    df = extract()
    duplicate_count = df["order_id"].duplicated().sum()
    assert duplicate_count == 0

def test_amount_positive():
    df = extract()
    assert (df["amount"] > 0).all()


def test_order_date_not_future():
    df = extract()
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    assert (df["order_date"] <= pd.Timestamp.today()).all()



# 🧠 This is DATA CI
# 
# Not UI test
# Not API test
# 👉 DATA QUALITY TEST