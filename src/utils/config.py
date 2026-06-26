"""
Centralized configuration module for the Customer Churn Prediction & LTV System.

This file stores common project paths, database settings, model paths,
and reusable configuration values used across preprocessing, modeling,
API, PostgreSQL integration, and dashboard-related scripts.
"""

import os
from pathlib import Path
from urllib.parse import quote_plus

from dotenv import load_dotenv


# ============================================================
# PROJECT ROOT
# ============================================================

# This points to the main project directory:
# customer_churn_ltv_system/
PROJECT_ROOT = Path(__file__).resolve().parents[2]


# ============================================================
# ENVIRONMENT VARIABLES
# ============================================================

ENV_FILE_PATH = PROJECT_ROOT / ".env"

if ENV_FILE_PATH.exists():
    load_dotenv(ENV_FILE_PATH)
else:
    load_dotenv()


# ============================================================
# DATA DIRECTORIES
# ============================================================

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"


# ============================================================
# DATA FILE PATHS
# ============================================================

RAW_TELCO_DATA_PATH = RAW_DATA_DIR / "Telco-Customer-Churn.csv"

CLEANED_TELCO_DATA_PATH = PROCESSED_DATA_DIR / "cleaned_telco_data.csv"

FEATURE_ENGINEERED_DATA_PATH = PROCESSED_DATA_DIR / "feature_engineered_data.csv"

CUSTOMER_CHURN_LTV_FINAL_PATH = PROCESSED_DATA_DIR / "customer_churn_ltv_final.csv"

HIGH_PRIORITY_CUSTOMERS_PATH = PROCESSED_DATA_DIR / "high_priority_customers.csv"


# ============================================================
# MODEL DIRECTORIES AND FILES
# ============================================================

MODELS_DIR = PROJECT_ROOT / "models"

CHURN_MODEL_PATH = MODELS_DIR / "churn_model.pkl"

SCALER_PATH = MODELS_DIR / "scaler.pkl"

FEATURE_COLUMNS_PATH = MODELS_DIR / "feature_columns.pkl"


# ============================================================
# DASHBOARD DIRECTORIES
# ============================================================

DASHBOARD_DIR = PROJECT_ROOT / "dashboard"

DASHBOARD_SCREENSHOTS_DIR = DASHBOARD_DIR / "screenshots"

DASHBOARD_SQL_QUERIES_FILE = DASHBOARD_DIR / "dashboard_sql_queries.py"

DASHBOARD_DOCUMENTATION_FILE = DASHBOARD_DIR / "dashboard_sql_queries.md"

METABASE_PROGRESS_FILE = DASHBOARD_DIR / "metabase_dashboard_progress.md"


# ============================================================
# NOTEBOOKS AND REPORTS
# ============================================================

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

REPORTS_DIR = PROJECT_ROOT / "reports"


# ============================================================
# DATABASE CONFIGURATION
# ============================================================

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "customer_churn_db")


def get_database_url() -> str:
    """
    Create PostgreSQL database connection URL.

    Returns:
        SQLAlchemy-compatible PostgreSQL connection URL.
    """
    encoded_password = quote_plus(DB_PASSWORD)

    return (
        f"postgresql+psycopg2://{DB_USER}:{encoded_password}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


# ============================================================
# DATABASE TABLE NAMES
# ============================================================

TELCO_CUSTOMER_CHURN_TABLE = "telco_customer_churn"

CUSTOMER_CHURN_LTV_TABLE = "customer_churn_ltv"

HIGH_PRIORITY_CUSTOMERS_TABLE = "high_priority_customers"


# ============================================================
# API CONFIGURATION
# ============================================================

API_TITLE = "Customer Churn Prediction API"

API_DESCRIPTION = (
    "FastAPI service for predicting customer churn probability "
    "using the trained machine learning model."
)

API_VERSION = "1.0.0"


# ============================================================
# BUSINESS CONSTANTS
# ============================================================

CHURN_TARGET_COLUMN = "Churn"

CUSTOMER_ID_COLUMN = "Customer_ID"

ORIGINAL_CUSTOMER_ID_COLUMN = "customerID"

LTV_COLUMN = "Estimated_LTV"

LTV_SEGMENT_COLUMN = "LTV_Segment"

CUSTOMER_PRIORITY_COLUMN = "Customer_Priority"


LTV_SEGMENTS = [
    "Low Value",
    "Medium Value",
    "High Value",
]


CUSTOMER_PRIORITY_GROUPS = [
    "Low Value - Low Risk",
    "Low Value - High Risk",
    "Medium Value - Low Risk",
    "Medium Value - High Risk",
    "High Value - Low Risk",
    "High Value - High Risk",
]


HIGH_PRIORITY_LABEL = "High Value - High Risk"


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def create_required_directories() -> None:
    """
    Create important project directories if they do not already exist.
    """
    required_dirs = [
        RAW_DATA_DIR,
        PROCESSED_DATA_DIR,
        MODELS_DIR,
        DASHBOARD_DIR,
        DASHBOARD_SCREENSHOTS_DIR,
        REPORTS_DIR,
    ]

    for directory in required_dirs:
        directory.mkdir(parents=True, exist_ok=True)


def validate_file_exists(file_path: Path) -> bool:
    """
    Check whether a file exists.

    Args:
        file_path: Path of the file to check.

    Returns:
        True if file exists, otherwise False.
    """
    return file_path.exists()


if __name__ == "__main__":
    print("Project configuration loaded successfully.")
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Database name: {DB_NAME}")
    print(f"Raw data path: {RAW_TELCO_DATA_PATH}")
    print(f"Processed data directory: {PROCESSED_DATA_DIR}")