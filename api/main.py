from fastapi import FastAPI
from api.schemas import CustomerData
from src.models.churn_predict import predict_churn
import pandas as pd


app = FastAPI(
    title="Customer Churn Prediction API",
    description=(
        "FastAPI service for predicting customer churn using model-ready "
        "encoded numerical input features."
    ),
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running successfully."
    }


def create_customer_dataframe(data: CustomerData) -> pd.DataFrame:
    """
    Converts API input data into a Pandas DataFrame with the exact
    feature column names expected by the trained churn prediction model.

    Note:
    API field names use underscores because Python variables cannot contain spaces.
    Model feature names keep spaces because they came from one-hot encoding.
    """

    input_data = {
        "gender": data.gender,
        "SeniorCitizen": data.SeniorCitizen,
        "Partner": data.Partner,
        "Dependents": data.Dependents,
        "tenure": data.tenure,
        "PhoneService": data.PhoneService,
        "PaperlessBilling": data.PaperlessBilling,
        "MonthlyCharges": data.MonthlyCharges,
        "TotalCharges": data.TotalCharges,

        "MultipleLines_No phone service": data.MultipleLines_No_phone_service,
        "MultipleLines_Yes": data.MultipleLines_Yes,

        "InternetService_Fiber optic": data.InternetService_Fiber_optic,
        "InternetService_No": data.InternetService_No,

        "OnlineSecurity_No internet service": data.OnlineSecurity_No_internet_service,
        "OnlineSecurity_Yes": data.OnlineSecurity_Yes,

        "OnlineBackup_No internet service": data.OnlineBackup_No_internet_service,
        "OnlineBackup_Yes": data.OnlineBackup_Yes,

        "DeviceProtection_No internet service": data.DeviceProtection_No_internet_service,
        "DeviceProtection_Yes": data.DeviceProtection_Yes,

        "TechSupport_No internet service": data.TechSupport_No_internet_service,
        "TechSupport_Yes": data.TechSupport_Yes,

        "StreamingTV_No internet service": data.StreamingTV_No_internet_service,
        "StreamingTV_Yes": data.StreamingTV_Yes,

        "StreamingMovies_No internet service": data.StreamingMovies_No_internet_service,
        "StreamingMovies_Yes": data.StreamingMovies_Yes,

        "Contract_One year": data.Contract_One_year,
        "Contract_Two year": data.Contract_Two_year,

        "PaymentMethod_Credit card (automatic)": data.PaymentMethod_Credit_card_automatic,
        "PaymentMethod_Electronic check": data.PaymentMethod_Electronic_check,
        "PaymentMethod_Mailed check": data.PaymentMethod_Mailed_check,
    }

    return pd.DataFrame([input_data])


@app.post("/predict")
def predict(data: CustomerData):
    customer_df = create_customer_dataframe(data)

    result = predict_churn(customer_df)

    return result