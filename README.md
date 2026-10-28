# 🚲 Bike Demand Prediction API

A Machine Learning API that predicts hourly bike rental demand using the **Seoul Bike Sharing Dataset** from Kaggle.

## 📌 Tech Stack

- **ML Model:** Random Forest Regressor (scikit-learn)
- **API:** FastAPI
- **Containerization:** Docker
- **CI/CD:** GitHub Actions

---

## 📁 Project Structure
bike-demand-api/
├── main.py # FastAPI application
├── model.joblib # Trained ML model
├── model_params.json # Model parameters
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration
└── .github/
└── workflows/
└── ci.yml # GitHub Actions CI pipeline
---

## 📊 Dataset

- **Source:** [Seoul Bike Sharing Demand - Kaggle](https://www.kaggle.com/datasets/saurabhshahane/seoul-bike-sharing-demand-prediction)
- **Size:** 8,760 records (hourly data)
- **Target:** `Rented Bike Count`
- **Features:** Hour, Temperature, Humidity, Wind Speed, Visibility, Dew Point, Solar Radiation, Rainfall, Snowfall, Season, Holiday, Functioning Day

---

## 🤖 Model

| Parameter | Value |
|---|---|
| Algorithm | Random Forest Regressor |
| n_estimators | 100 |
| Train/Test Split | 80/20 (time-based) |
| Training Period | Dec 2017 – Sep 2018 |
| Testing Period | Sep 2018 – Nov 2018 |

---

## 🚀 Run Locally with Docker

```bash
# Build image
docker build -t bike-demand-api .

# Run container
docker run -p 7000:7000 bike-demand-api
```

API will be live at: `http://localhost:7000`

---

## 📡 API Endpoints

### `GET /`
Health check
```json
{ "message": "Bike Demand Prediction API" }
```

### `POST /predict`
Predict bike demand

**Request Body:**
```json
{
  "Hour": 8,
  "Temperature": 15.0,
  "Humidity": 60,
  "WindSpeed": 2.0,
  "Visibility": 2000,
  "DewPoint": 5.0,
  "SolarRadiation": 0.5,
  "Rainfall": 0.0,
  "Snowfall": 0.0,
  "Seasons": "Autumn",
  "Holiday": "No Holiday",
  "FunctioningDay": "Yes",
  "Month": 9,
  "DayOfWeek": 2
}
```

**Response:**
```json
{ "predicted_bike_count": 742.35 }
```

### Swagger UI
Interactive API docs at: `http://localhost:7000/docs`

---

## ⚙️ GitHub Actions CI Pipeline

On every push to `main`:
1. ✅ Checkout code
2. ✅ Set up Python 3.10
3. ✅ Install dependencies
4. ✅ Test API starts successfully
5. ✅ Build Docker image

---

## 🛠️ Setup Without Docker

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 7000
```

---

## 👤 Author

Ayush Gupta
2400290120078
Course: MLOps / CA2 Assignment
