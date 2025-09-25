# 🚗 Old Car Price Prediction

#### A machine learning web app that predicts the **selling price of used cars** based on features such as year, kilometers driven, fuel type, transmission, ownership, mileage, engine, power, and seats.  

#### The project includes **data preprocessing, model training, and a Flask web application with a modern UI**.

---

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Harshuu02/OldCar_Price_Prediction.git
   cd OldCar_Price_Prediction

   
   
2. Create the Envoronment:

       python -m venv venv
       source venv/bin/activate     # Mac/Linux
   
       venv\Scripts\activate        # Windows

3. Install the Requirements:

             pip install -r requirements.txt

    
---

## 🧹 Data Preprocessing

	•	Cleans raw dataset (train-data.csv)
	•	Extracts numeric values from Mileage, Engine, and Power
	•	Creates car_age from Year
	•	Encodes categorical variables (Fuel_Type, Transmission, Owner_Type)
	•	Drops unnecessary columns (Name, Location, New_Price)

    See car_preprocess.py

---

## 🤖 Model Training

    python src/train_model.py

    •	Uses RandomForestRegressor

    •	Splits data into train/test

    •	Evaluates with R² and RMSE

    •	Saves trained model to models/car_price_model.pkl

---

## 🌐 Web Application

1.	Start the Flask app:

     python app/app.py

2.	Open in browser:

    http://127.0.0.1:5000/

3.	Enter car details → Click Predict Price → Get instant estimated price.

---

## 🎨 UI Features

	•	Built with Bootstrap 5 + custom CSS
	•	Responsive design
	•	Modern input forms with hover/focus effects
	•	Clear results with gradient highlights

---

## 📊 Example Prediction

    Input:
	    •	Year: 2017
	    •	Kilometers Driven: 45,000
	    •	Fuel Type: Petrol
	    •	Transmission: Manual
	    •	Owner: First
	    •	Mileage: 20 km/l
	    •	Engine: 1200 CC
	    •	Power: 82 bhp
	    •	Seats: 5

    💰 Estimated Price: ₹ 4.75 Lakh

---

## 🚀 Future Improvements

	•	Add visualizations (price distribution, feature importance)
	•	Deploy on Heroku / Render / Railway
	•	Add login & user history of predictions
	•	Support API endpoint for external usage

---

## 📝 License

This project is for educational purposes only.
