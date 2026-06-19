import joblib
import pandas as pd

model = joblib.load("models/saved_model/logistic_regression_model.pkl")

def predict_churn(customer_data):
    customer_values = customer_data.values

    prediction = model.predict(customer_values)
    probability = model.predict_proba(customer_values)

    return {
        "prediction": int(prediction[0]),
        "churn_probability": round(float(probability[0][1]), 4)
    }