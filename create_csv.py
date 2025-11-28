# create_csv.py
import pandas as pd
import random
from datetime import datetime, timedelta

# Generate sample data
data = []
start_date = datetime(2025, 1, 1)

for i in range(500):  # generate 500 rows
    date = start_date + timedelta(days=i % 30)
    product_id = random.choice([101, 102, 103, 104])
    store_id = random.choice([1, 2, 3])
    price = round(random.uniform(50, 200), 2)
    promotion = random.choice([0, 1])
    stock_level = random.randint(50, 500)
    units_sold = int((200 - price) * (1 + promotion * 0.5) * random.uniform(0.5, 1.5))
    data.append([product_id, store_id, date.strftime("%Y-%m-%d"), units_sold, price, promotion, stock_level])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'product_id', 'store_id', 'date', 'units_sold', 'price', 'promotion', 'stock_level'
])

# Save to CSV
df.to_csv('ecommerce_sales_data.csv', index=False)
print("CSV file created: ecommerce_sales_data.csv")
