import pandas as pd

from src.preprocessing.ltv_calculator import (
    calculate_estimated_ltv,
    create_ltv_segment,
    create_customer_priority,
)


def generate_ltv_predictions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate LTV-based customer analytics features.

    This function applies the complete LTV workflow:
    1. Calculates Estimated_LTV
    2. Creates LTV_Segment
    3. Creates Customer_Priority

    Parameters
    ----------
    df : pd.DataFrame
        Input customer dataset containing MonthlyCharges, tenure, and Churn columns.

    Returns
    -------
    pd.DataFrame
        Customer dataset enriched with Estimated_LTV, LTV_Segment, and Customer_Priority.
    """

    required_columns = ["MonthlyCharges", "tenure", "Churn"]

    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    ltv_df = df.copy()

    ltv_df = calculate_estimated_ltv(ltv_df)
    ltv_df = create_ltv_segment(ltv_df)
    ltv_df = create_customer_priority(ltv_df)

    return ltv_df


if __name__ == "__main__":
    print("LTV prediction module is ready to use.")