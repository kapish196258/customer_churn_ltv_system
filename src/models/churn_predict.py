import joblib
import pandas as pd

model = joblib.load("models/saved_model/logistic_regression_model.pkl")

def predict_churn(customer_data):
    prediction = model.predict(customer_data)
    probability = model.predict_proba(customer_data)

    return {
        "prediction": int(prediction[0]),
        "churn_probability": float(probability[0][1])
    }