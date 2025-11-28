from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from pydantic import BaseModel
import joblib
import numpy as np
from textblob import TextBlob  # simple sentiment analysis

app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] to restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("xgb_demand_model.pkl")

class ProductInput(BaseModel):
    product_id: int
    store_id: int
    price: float
    promotion: int
    stock_level: int
    day_of_week: int
    month: int
    review: str = "No review provided"  # <-- add review text

@app.post("/predict-prescribe")
def predict_and_prescribe(data: ProductInput):
    # Predict demand
    features = np.array([[data.product_id, data.store_id, data.price,
                          data.promotion, data.stock_level,
                          data.day_of_week, data.month]])
    prediction = model.predict(features)[0]
    prediction = max(0, prediction)

    # Sentiment Analysis on review
    sentiment_score = TextBlob(data.review).sentiment.polarity
    if sentiment_score > 0.2:
        sentiment = "Positive"
    elif sentiment_score < -0.2:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Prescriptive Rule
    if prediction < 1 and sentiment == "Negative":
        recommendation = "Low demand and poor feedback. Consider reducing price or improving quality."
    elif prediction > 5 and sentiment == "Positive":
        recommendation = "High demand and positive feedback. Stock up and continue promotion."
    elif prediction > 2 and sentiment == "Neutral":
        recommendation = "Moderate demand. Try promotions to boost sales."
    else:
        recommendation = "Monitor performance and adjust strategy."

    return {
        "predicted_units_sold": round(float(prediction), 2),
        "sentiment": sentiment,
        "recommendation": recommendation
    }
