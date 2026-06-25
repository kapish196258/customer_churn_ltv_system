"""
Reusable SQL queries for Metabase dashboard development.

These queries are used to create KPI cards and visualizations for
customer churn, LTV, and retention analysis.
"""


TOTAL_CUSTOMERS_QUERY = """
SELECT COUNT(*) AS total_customers
FROM customer_churn_ltv;
"""


HIGH_PRIORITY_CUSTOMERS_QUERY = """
SELECT COUNT(*) AS high_priority_customers
FROM high_priority_customers;
"""


LTV_AT_RISK_MILLIONS_QUERY = """
SELECT
    ROUND((SUM("Estimated_LTV") / 1000000.0)::numeric, 2) AS total_ltv_at_risk_million
FROM high_priority_customers;
"""


CUSTOMER_DISTRIBUTION_BY_LTV_SEGMENT_QUERY = """
SELECT
    "LTV_Segment",
    COUNT(*) AS customer_count
FROM customer_churn_ltv
GROUP BY "LTV_Segment"
ORDER BY customer_count DESC;
"""


CHURN_RATE_BY_LTV_SEGMENT_QUERY = """
SELECT
    "LTV_Segment",
    ROUND((SUM("Churn")::numeric / COUNT(*)) * 100, 2) AS churn_rate_percentage
FROM customer_churn_ltv
GROUP BY "LTV_Segment"
ORDER BY churn_rate_percentage DESC;
"""