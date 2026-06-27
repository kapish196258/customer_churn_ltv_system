from typing import Literal
from pydantic import BaseModel, Field


class CustomerData(BaseModel):
    gender: Literal[0, 1] = Field(
        ...,
        description="0 = Male, 1 = Female",
        example=1
    )

    SeniorCitizen: Literal[0, 1] = Field(
        ...,
        description="0 = Not senior citizen, 1 = Senior citizen",
        example=1
    )

    Partner: Literal[0, 1] = Field(
        ...,
        description="0 = No partner, 1 = Has partner",
        example=0
    )

    Dependents: Literal[0, 1] = Field(
        ...,
        description="0 = No dependents, 1 = Has dependents",
        example=0
    )

    tenure: int = Field(
        ...,
        description="Customer tenure in months",
        example=1
    )

    PhoneService: Literal[0, 1] = Field(
        ...,
        description="0 = No phone service, 1 = Has phone service",
        example=1
    )

    PaperlessBilling: Literal[0, 1] = Field(
        ...,
        description="0 = No paperless billing, 1 = Uses paperless billing",
        example=1
    )

    MonthlyCharges: float = Field(
        ...,
        description="Monthly charges paid by the customer",
        example=118.75
    )

    TotalCharges: float = Field(
        ...,
        description="Total charges paid by the customer",
        example=118.75
    )

    MultipleLines_No_phone_service: Literal[0, 1] = Field(
        ...,
        description="1 = No phone service, 0 = Otherwise",
        example=0
    )

    MultipleLines_Yes: Literal[0, 1] = Field(
        ...,
        description="1 = Multiple lines = Yes, 0 = Otherwise. If both MultipleLines fields are 0, MultipleLines = No.",
        example=1
    )

    InternetService_Fiber_optic: Literal[0, 1] = Field(
        ...,
        description="1 = Internet service = Fiber optic, 0 = Otherwise",
        example=1
    )

    InternetService_No: Literal[0, 1] = Field(
        ...,
        description="1 = Internet service = No, 0 = Otherwise. If both InternetService fields are 0, InternetService = DSL.",
        example=0
    )

    OnlineSecurity_No_internet_service: Literal[0, 1] = Field(
        ...,
        description="1 = No internet service, 0 = Otherwise",
        example=0
    )

    OnlineSecurity_Yes: Literal[0, 1] = Field(
        ...,
        description="1 = Online security = Yes, 0 = Otherwise. If both OnlineSecurity fields are 0, OnlineSecurity = No.",
        example=0
    )

    OnlineBackup_No_internet_service: Literal[0, 1] = Field(
        ...,
        description="1 = No internet service, 0 = Otherwise",
        example=0
    )

    OnlineBackup_Yes: Literal[0, 1] = Field(
        ...,
        description="1 = Online backup = Yes, 0 = Otherwise. If both OnlineBackup fields are 0, OnlineBackup = No.",
        example=0
    )

    DeviceProtection_No_internet_service: Literal[0, 1] = Field(
        ...,
        description="1 = No internet service, 0 = Otherwise",
        example=0
    )

    DeviceProtection_Yes: Literal[0, 1] = Field(
        ...,
        description="1 = Device protection = Yes, 0 = Otherwise. If both DeviceProtection fields are 0, DeviceProtection = No.",
        example=0
    )

    TechSupport_No_internet_service: Literal[0, 1] = Field(
        ...,
        description="1 = No internet service, 0 = Otherwise",
        example=0
    )

    TechSupport_Yes: Literal[0, 1] = Field(
        ...,
        description="1 = Tech support = Yes, 0 = Otherwise. If both TechSupport fields are 0, TechSupport = No.",
        example=0
    )

    StreamingTV_No_internet_service: Literal[0, 1] = Field(
        ...,
        description="1 = No internet service, 0 = Otherwise",
        example=0
    )

    StreamingTV_Yes: Literal[0, 1] = Field(
        ...,
        description="1 = Streaming TV = Yes, 0 = Otherwise. If both StreamingTV fields are 0, StreamingTV = No.",
        example=1
    )

    StreamingMovies_No_internet_service: Literal[0, 1] = Field(
        ...,
        description="1 = No internet service, 0 = Otherwise",
        example=0
    )

    StreamingMovies_Yes: Literal[0, 1] = Field(
        ...,
        description="1 = Streaming movies = Yes, 0 = Otherwise. If both StreamingMovies fields are 0, StreamingMovies = No.",
        example=1
    )

    Contract_One_year: Literal[0, 1] = Field(
        ...,
        description="1 = Contract = One year, 0 = Otherwise",
        example=0
    )

    Contract_Two_year: Literal[0, 1] = Field(
        ...,
        description="1 = Contract = Two year, 0 = Otherwise. If both Contract fields are 0, Contract = Month-to-month.",
        example=0
    )

    PaymentMethod_Credit_card_automatic: Literal[0, 1] = Field(
        ...,
        description="1 = Payment method = Credit card automatic, 0 = Otherwise",
        example=0
    )

    PaymentMethod_Electronic_check: Literal[0, 1] = Field(
        ...,
        description="1 = Payment method = Electronic check, 0 = Otherwise",
        example=1
    )

    PaymentMethod_Mailed_check: Literal[0, 1] = Field(
        ...,
        description="1 = Payment method = Mailed check, 0 = Otherwise. If all PaymentMethod fields are 0, Payment method = Bank transfer automatic.",
        example=0
    )