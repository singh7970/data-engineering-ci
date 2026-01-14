from scripts.extract import extract
from scripts.transform import transform

def test_sql_transformation():
    df = transform(extract())

    assert "city" in df.columns
    assert df["city"].str.isupper().all()
    assert df["amount"].isnull().sum() == 0
