import pandas as pd
import random
from datetime import datetime, timedelta

rows = []
start_date = datetime(2024, 1, 1)

for i in range(1, 10001):  # 10K rows
    rows.append({
        "order_id": i,
        "order_date": start_date + timedelta(days=random.randint(0, 30)),
        "amount": random.randint(100, 10000),
        "city": random.choice(["delhi", "mumbai", "chennai", "kanpur"])
    })

df = pd.DataFrame(rows)
df.to_csv("sales_large.csv", index=False)
