import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from math import sqrt

from src.car_preprocess import Preprocessor  # adjust if you renamed file

# Paths
DATA_PATH = os.path.join("..", "data", "train-data.csv")
MODEL_PATH = os.path.join("..", "models", "car_price_model.pkl")

# Load dataset
df = pd.read_csv(DATA_PATH)

# Preprocess
preprocessor = Preprocessor(current_year=2025)
df_clean = preprocessor.clean_data(df)

# Features and target
X = df_clean[['car_age', 'km_driven', 'fuel_type', 'transmission', 'owner',
              'Mileage_num', 'Engine_num', 'Power_num', 'Seats']]
y = df_clean['selling_price']

# One-hot encoding for categorical features
X = pd.get_dummies(X, columns=['fuel_type', 'transmission', 'owner'], drop_first=True)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = sqrt(mean_squared_error(y_test, y_pred))

print(f"✅ R² Score: {r2:.3f}")
print(f"✅ RMSE: {rmse:.3f}")

# Save model
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print(f"✅ Model saved at {MODEL_PATH}")