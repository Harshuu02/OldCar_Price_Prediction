from flask import Flask, render_template, request
import pickle
import os
from src.car_preprocess import Preprocessor   # if you renamed -> car_preprocess
import datetime
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

# Load model
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "car_price_model.pkl")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Preprocessor
preprocessor = Preprocessor(current_year=2025)

@app.context_processor
def inject_now():
    return {'now': datetime.datetime.now()}

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", title="Car Price Predictor")

@app.route("/predict", methods=["POST"])
def predict():
    car_details = {
        "brand": request.form.get("brand"),
        "year": request.form.get("year"),
        "km_driven": request.form.get("km_driven"),
        "fuel_type": request.form.get("fuel_type"),
        "transmission": request.form.get("transmission"),
        "owner": request.form.get("owner"),
        "mileage": request.form.get("mileage"),
        "engine": request.form.get("engine"),
        "power": request.form.get("power"),
        "seats": request.form.get("seats")
    }

    # Preprocess input
    X_input = preprocessor.transform_input(car_details)

    # One-hot encode same as training
    X_input = pd.get_dummies(X_input, columns=['fuel_type', 'transmission', 'owner'], drop_first=True)

    # Align with model training columns
    model_features = model.feature_names_in_
    X_input = X_input.reindex(columns=model_features, fill_value=0)

    # Predict
    predicted_price = model.predict(X_input)[0]

    return render_template(
        "result.html",
        predicted_price=round(predicted_price, 2),
        brand=car_details["brand"],
        year=car_details["year"],
        fuel_type=car_details["fuel_type"],
        transmission=car_details["transmission"],
        km_driven=car_details["km_driven"],
        mileage=car_details["mileage"],
        engine=car_details["engine"],
        power=car_details["power"],
        seats=car_details["seats"]
    )

if __name__ == "__main__":
    app.run(debug=True)