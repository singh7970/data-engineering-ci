# A data test verifies:

# Data meets business & technical rules


from scripts.extract import extract

def test_order_id_not_null():
    df = extract()
    assert df["order_id"].isnull().sum() == 0



# 🧠 This is DATA CI
# 
# Not UI test
# Not API test
# 👉 DATA QUALITY TEST