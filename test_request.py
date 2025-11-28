# test_request.py
import requests

# API endpoint (make sure your FastAPI server is running!)
url = "http://127.0.0.1:8000/predict-demand"

# Example input payload (adjust values as you like)
payload = {
    "product_id": 1,
    "store_id": 101,
    "price": 250.5,
    "promotion": 1,
    "stock_level": 50,
    "day_of_week": 3,
    "month": 8
}

# Send POST request
response = requests.post(url, json=payload)

# Show response
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
