# train_model.py
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# Load dataset
df = pd.read_csv('ecommerce_sales_data.csv')

# Feature engineering
df['day_of_week'] = pd.to_datetime(df['date']).dt.dayofweek
df['month'] = pd.to_datetime(df['date']).dt.month

# Define features and target
X = df[['product_id', 'store_id', 'price', 'promotion', 'stock_level', 'day_of_week', 'month']]
y = df['units_sold']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, max_depth=6)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'xgb_demand_model.pkl')

# Evaluate
y_pred = model.predict(X_test)
from math import sqrt
rmse = sqrt(mean_squared_error(y_test, y_pred))

print(f"✅ Model trained and saved. RMSE: {rmse:.2f}")
