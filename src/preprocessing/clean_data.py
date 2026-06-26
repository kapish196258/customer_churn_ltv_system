"""
Reusable data cleaning module for the Telco Customer Churn dataset.

This script converts the raw Telco customer dataset into a cleaned dataset
that can be used for EDA, feature engineering, model training, PostgreSQL
integration, and LTV analysis.
"""

from pathlib import Path

import pandas as pd


RAW_DATA_PATH = Path("data/raw/Telco-Customer-Churn.csv")
PROCESSED_DATA_PATH = Path("data/processed/cleaned_telco_data.csv")


def load_data(file_path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """
    Load the raw Telco Customer Churn dataset.

    Args:
        file_path: Path to the raw CSV file.

    Returns:
        Loaded pandas DataFrame.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Raw data file not found: {file_path}")

    return pd.read_csv(file_path)


def clean_total_charges(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert TotalCharges column from object/string type to numeric type.

    Invalid or blank values are converted to NaN.
    """
    df = df.copy()

    if "TotalCharges" not in df.columns:
        raise KeyError("Column 'TotalCharges' not found in dataset.")

    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    return df


def remove_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows containing missing values.

    In the Telco dataset, missing values appear after converting TotalCharges
    to numeric because some records contain blank TotalCharges values.
    """
    df = df.copy()
    df = df.dropna()

    return df


def remove_duplicate_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows from the dataset.
    """
    df = df.copy()
    df = df.drop_duplicates()

    return df


def clean_telco_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply the complete data cleaning workflow.

    Cleaning steps:
    1. Convert TotalCharges to numeric
    2. Remove missing values
    3. Remove duplicate rows

    Args:
        df: Raw Telco customer DataFrame.

    Returns:
        Cleaned Telco customer DataFrame.
    """
    cleaned_df = df.copy()
    cleaned_df = clean_total_charges(cleaned_df)
    cleaned_df = remove_missing_values(cleaned_df)
    cleaned_df = remove_duplicate_rows(cleaned_df)

    return cleaned_df


def save_cleaned_data(
    df: pd.DataFrame,
    output_path: Path = PROCESSED_DATA_PATH
) -> None:
    """
    Save the cleaned dataset as a CSV file.

    Args:
        df: Cleaned DataFrame.
        output_path: Path where cleaned CSV should be saved.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def main() -> None:
    """
    Run the full data cleaning pipeline.
    """
    raw_df = load_data()
    cleaned_df = clean_telco_data(raw_df)
    save_cleaned_data(cleaned_df)

    print("Data cleaning completed successfully.")
    print(f"Original shape: {raw_df.shape}")
    print(f"Cleaned shape: {cleaned_df.shape}")
    print(f"Cleaned data saved to: {PROCESSED_DATA_PATH}")


if __name__ == "__main__":
    main()