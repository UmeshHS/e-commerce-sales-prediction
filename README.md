# 📦 E-Commerce Demand Prediction (React + FastAPI + ML)

This project predicts **product demand**, performs **sentiment analysis** on customer reviews, and generates **prescriptive business recommendations**.  
It uses:

- 🧠 Machine Learning (XGBoost)
- ✍️ NLP Sentiment Analysis (TextBlob)
- ⚙️ FastAPI Backend
- 💻 React Frontend (Recharts + Axios)

---

## 📂 Project Structure

project/
│
├── ecommerce-frontend/ # React Frontend
│ ├── public/
│ ├── src/
│ │ ├── App.js # DemandPrediction UI
│ │ ├── DemandForm.js
│ │ ├── App.css
│ │ ├── index.js
│ ├── package.json
│
├── app.py # FastAPI Backend (Main API)
├── train_model.py # ML training script
├── xgb_demand_model.pkl # Saved ML model
├── ecommerce_sales_data.csv # Dataset
├── test_request.py # For backend testing
└── README.md

## 🚀 Features

### 🔮 Machine Learning
- Predicts **units sold**
- Uses XGBoost regression
- Analyzes demand patterns

### 😊 Sentiment Analysis
- Uses TextBlob to detect:
  - **Positive**
  - **Neutral**
  - **Negative**

### ⚙️ Backend (FastAPI)
- `/predict-prescribe` endpoint
- Returns:
  - Predicted units sold  
  - Sentiment category  
  - Business recommendation (dynamic)

### 💻 UI (React + Axios)
- Input form for all product parameters  
- Customer review textbox  
- Displays prediction + recommendation  
- Recharts bar graph visualization  
- Clean, modern UI  

---

## 📦 Installation & Setup

---

# 🧠 Backend Setup (FastAPI)

### 1️⃣ Go to project folder

  cd project
  
2️⃣ Install dependencies
  pip install fastapi uvicorn numpy pandas scikit-learn xgboost joblib textblob

3️⃣ Run backend

uvicorn app:app --reload

Backend will run at:
http://127.0.0.1:8000
Swagger documentation:
http://127.0.0.1:8000/docs


💻 Frontend Setup (React)
1️⃣ Go inside React folder
  cd ecommerce-frontend
  
2️⃣ Install packages
  npm install
  
3️⃣ Run frontend
  npm start run


Frontend will run at:

http://localhost:3000



🔗 API Route Used by Frontend
POST /predict-prescribe
Request:

json
Copy code
{
  "product_id": 101,
  "store_id": 1,
  "price": 250,
  "promotion": 1,
  "stock_level": 50,
  "day_of_week": 2,
  "month": 8,
  "review": "Customers love the product but feel it's a bit costly"
}
Response:

json
Copy code
{
  "predicted_units_sold": 187,
  "sentiment": "Positive",
  "recommendation": "Increase stock immediately and continue promotion."
}
📊 UI Features
Real-time predictions

Sentiment color indicators

Recommendations based on stock + demand + sentiment

Recharts bar graph comparing:

Predicted Demand

Current Stock


👤 Author
Umesh H S

yaml
Copy code
