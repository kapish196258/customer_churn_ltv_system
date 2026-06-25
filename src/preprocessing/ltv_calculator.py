import pandas as pd


def calculate_estimated_ltv(
    df: pd.DataFrame,
    monthly_charge_col: str = "MonthlyCharges",
    tenure_col: str = "tenure",
    output_col: str = "Estimated_LTV"
) -> pd.DataFrame:
    """
    Calculate estimated Customer Lifetime Value (LTV).

    Estimated LTV is calculated using:
        MonthlyCharges * tenure

    Parameters
    ----------
    df : pd.DataFrame
        Input customer dataframe.
    monthly_charge_col : str
        Column name containing monthly charges.
    tenure_col : str
        Column name containing customer tenure.
    output_col : str
        Name of the output LTV column.

    Returns
    -------
    pd.DataFrame
        DataFrame with Estimated_LTV column added.
    """

    df = df.copy()

    df[output_col] = df[monthly_charge_col] * df[tenure_col]

    return df


def create_ltv_segment(
    df: pd.DataFrame,
    ltv_col: str = "Estimated_LTV",
    output_col: str = "LTV_Segment"
) -> pd.DataFrame:
    """
    Create LTV segments based on Estimated_LTV values.

    Customers are divided into:
    - Low Value
    - Medium Value
    - High Value

    Segmentation is based on the 50th and 75th percentile.
    """

    df = df.copy()

    low_threshold = df[ltv_col].quantile(0.50)
    high_threshold = df[ltv_col].quantile(0.75)

    def segment_customer(ltv_value: float) -> str:
        if ltv_value <= low_threshold:
            return "Low Value"
        elif ltv_value <= high_threshold:
            return "Medium Value"
        else:
            return "High Value"

    df[output_col] = df[ltv_col].apply(segment_customer)

    return df


def create_customer_priority(
    df: pd.DataFrame,
    ltv_segment_col: str = "LTV_Segment",
    churn_col: str = "Churn",
    output_col: str = "Customer_Priority"
) -> pd.DataFrame:
    """
    Create customer priority groups using LTV segment and churn status.

    Churn = 1 means high risk.
    Churn = 0 means low risk.
    """

    df = df.copy()

    def assign_priority(row) -> str:
        risk_label = "High Risk" if row[churn_col] == 1 else "Low Risk"
        return f"{row[ltv_segment_col]} - {risk_label}"

    df[output_col] = df.apply(assign_priority, axis=1)

    return df