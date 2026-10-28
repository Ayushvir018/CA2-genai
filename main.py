from fastapi import FastAPI
from pydantic import BaseModel
import joblib, numpy as np
import pandas as pd

app = FastAPI()
model = joblib.load("model.joblib")

class BikeInput(BaseModel):
    Hour: int
    Temperature: float
    Humidity: float
    WindSpeed: float
    Visibility: int
    DewPoint: float
    SolarRadiation: float
    Rainfall: float
    Snowfall: float
    Seasons: str
    Holiday: str
    FunctioningDay: str
    Month: int
    DayOfWeek: int

@app.get("/")
def root():
    return {"message": "Bike Demand Prediction API"}

@app.post("/predict")
def predict(data: BikeInput):
    df = pd.DataFrame([{
        "Hour": data.Hour,
        "Temperature(°C)": data.Temperature,
        "Humidity(%)": data.Humidity,
        "Wind speed (m/s)": data.WindSpeed,
        "Visibility (10m)": data.Visibility,
        "Dew point temperature(°C)": data.DewPoint,
        "Solar Radiation (MJ/m2)": data.SolarRadiation,
        "Rainfall(mm)": data.Rainfall,
        "Snowfall (cm)": data.Snowfall,
        "Seasons": data.Seasons,
        "Holiday": data.Holiday,
        "Functioning Day": data.FunctioningDay,
        "Month": data.Month,
        "DayOfWeek": data.DayOfWeek
    }])
    prediction = model.predict(df)[0]
    return {"predicted_bike_count": round(float(prediction), 2)}