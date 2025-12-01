from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
from textblob import TextBlob

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route (important for Render health check)
@app.get("/")
def home():
    return {"message": "Ecommerce Prediction Backend Running"}

# Load model
model = joblib.load("xgb_demand_model.pkl")

class ProductInput(BaseModel):
    product_id: int
    store_id: int
    price: float
    promotion: int
    stock_level: int
    day_of_week: int
    month: int
    review: str = "No review provided"

def generate_recommendation(pred, stock, sentiment):

    if pred > stock + 20:
        return "Very high demand expected! Increase stock immediately and boost supply."

    if pred > stock:
        return "Demand is slightly higher than stock. Consider restocking soon."

    if stock > pred + 30:
        return "Too much inventory. Offer discounts or reduce stock."

    if sentiment == "Negative":
        return "Customer sentiment is low. Improve quality or reduce price."

    if sentiment == "Positive" and pred > stock * 0.8:
        return "Strong demand and positive reviews! Increase stock and continue promotion."

    if sentiment == "Neutral":
        return "Stable performance. Try moderate promotions to increase visibility."

    return "Monitor performance and adjust strategy."

@app.post("/predict-prescribe")
def predict_and_prescribe(data: ProductInput):

    features = np.array([[data.product_id, data.store_id, data.price,
                          data.promotion, data.stock_level,
                          data.day_of_week, data.month]])

    prediction = model.predict(features)[0]
    prediction = max(0, prediction)

    sentiment_score = TextBlob(data.review).sentiment.polarity

    if sentiment_score > 0.2:
        sentiment = "Positive"
    elif sentiment_score < -0.2:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    recommendation = generate_recommendation(prediction, data.stock_level, sentiment)

    return {
        "predicted_units_sold": round(float(prediction), 2),
        "sentiment": sentiment,
        "recommendation": recommendation
    }
