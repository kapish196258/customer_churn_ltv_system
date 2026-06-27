import joblib
import pandas as pd


pipeline = joblib.load("models/saved_model/churn_prediction_pipeline.pkl")


def predict_churn(customer_data: pd.DataFrame):
    """
    Predict customer churn using the trained pipeline.

    The pipeline includes:
    1. StandardScaler
    2. Logistic Regression model

    Therefore, FastAPI can send normal model-ready raw numeric values,
    and scaling is applied automatically before prediction.
    """

    prediction = pipeline.predict(customer_data)[0]
    probability = pipeline.predict_proba(customer_data)[0][1]

    return {
        "prediction": int(prediction),
        "churn_probability": round(float(probability), 4)
    }