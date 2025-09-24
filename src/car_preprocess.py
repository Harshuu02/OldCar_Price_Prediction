import pandas as pd
import numpy as np
import re

class Preprocessor:
    def __init__(self, current_year=2025):
        self.current_year = current_year

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        # Make a copy
        df = df.copy()

        # Drop unnecessary index column
        if 'Unnamed: 0' in df.columns:
            df = df.drop(columns=['Unnamed: 0'])

        # Create car_age
        df['car_age'] = self.current_year - df['Year']

        # Clean numeric columns (Mileage, Engine, Power)
        df['Mileage_num'] = df['Mileage'].str.extract(r'([\d.]+)').astype(float)
        df['Engine_num'] = df['Engine'].str.extract(r'([\d.]+)').astype(float)
        df['Power_num'] = df['Power'].str.extract(r'([\d.]+)').astype(float)

        # Rename for consistency
        df = df.rename(columns={
            'Kilometers_Driven': 'km_driven',
            'Fuel_Type': 'fuel_type',
            'Transmission': 'transmission',
            'Owner_Type': 'owner',
            'Price': 'selling_price'
        })

        # Drop high-cardinality columns
        df = df.drop(columns=['Name', 'Location', 'New_Price'], errors='ignore')

        # Drop rows with missing target
        df = df.dropna(subset=['selling_price'])

        return df

    def transform_input(self, car_details: dict) -> pd.DataFrame:
        """Convert single user input into a DataFrame suitable for model prediction"""
        df = pd.DataFrame([car_details])

        # Calculate car age
        df['car_age'] = self.current_year - df['year'].astype(int)

        # Ensure numeric conversion
        df['km_driven'] = df['km_driven'].astype(float)
        df['Mileage_num'] = pd.to_numeric(df.get('mileage', 0), errors='coerce')
        df['Engine_num'] = pd.to_numeric(df.get('engine', 0), errors='coerce')
        df['Power_num'] = pd.to_numeric(df.get('power', 0), errors='coerce')
        df['Seats'] = pd.to_numeric(df.get('seats', 5), errors='coerce')

        # Rename to match training
        df = df.rename(columns={
            'year': 'Year',
            'fuel_type': 'fuel_type',
            'transmission': 'transmission',
            'owner': 'owner'
        })

        return df[['car_age', 'km_driven', 'fuel_type', 'transmission', 'owner',
                   'Mileage_num', 'Engine_num', 'Power_num', 'Seats']]