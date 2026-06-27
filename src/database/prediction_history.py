import os
from datetime import datetime
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError


load_dotenv()


def get_database_url() -> str:
    """
    Builds the PostgreSQL database URL using environment variables.
    Supports either DATABASE_URL directly or separate DB credentials.
    """

    database_url = os.getenv("DATABASE_URL")

    if database_url:
        return database_url

    db_user = os.getenv("DB_USER", "postgres")
    db_password = quote_plus(os.getenv("DB_PASSWORD", ""))
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "customer_churn_db")

    return f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


engine = create_engine(get_database_url())


def save_prediction_history(
    customer_id: str | None,
    churn_prediction: int,
    churn_probability: float,
    estimated_ltv: float
) -> bool:
    """
    Saves FastAPI prediction output into PostgreSQL prediction_history table.
    Returns True if saved successfully, otherwise False.
    """

    insert_query = text("""
        INSERT INTO prediction_history (
            customer_id,
            churn_prediction,
            churn_probability,
            estimated_ltv,
            created_at
        )
        VALUES (
            :customer_id,
            :churn_prediction,
            :churn_probability,
            :estimated_ltv,
            :created_at
        )
    """)

    try:
        with engine.begin() as connection:
            connection.execute(
                insert_query,
                {
                    "customer_id": customer_id,
                    "churn_prediction": churn_prediction,
                    "churn_probability": churn_probability,
                    "estimated_ltv": estimated_ltv,
                    "created_at": datetime.now()
                }
            )

        return True

    except SQLAlchemyError as error:
        print(f"Prediction history logging failed: {error}")
        return False