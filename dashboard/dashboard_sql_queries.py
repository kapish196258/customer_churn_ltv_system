"""
Reusable SQL queries for Metabase dashboard development.

These queries are used to create KPI cards, charts, and tables for
customer churn, LTV, revenue risk, and retention analysis.
"""

# 1. Total Customers
TOTAL_CUSTOMERS_QUERY = """
SELECT 
    COUNT(*) AS total_customers
FROM customer_churn_ltv;
"""


# 2. High Priority Customers
HIGH_PRIORITY_CUSTOMERS_QUERY = """
SELECT 
    COUNT(*) AS high_priority_customers
FROM high_priority_customers;
"""


# 3. Total LTV at Risk Millions
TOTAL_LTV_AT_RISK_MILLIONS_QUERY = """
SELECT
    ROUND((SUM("Estimated_LTV") / 1000000.0)::numeric, 2) AS total_ltv_at_risk_million
FROM high_priority_customers;
"""


# 4. Customer Distribution by LTV Segment
CUSTOMER_DISTRIBUTION_BY_LTV_SEGMENT_QUERY = """
SELECT
    "LTV_Segment",
    COUNT(*) AS customer_count
FROM customer_churn_ltv
GROUP BY "LTV_Segment"
ORDER BY customer_count DESC;
"""


# 5. Churn Rate by LTV Segment
CHURN_RATE_BY_LTV_SEGMENT_QUERY = """
SELECT
    "LTV_Segment",
    ROUND((SUM("Churn")::numeric / COUNT(*)) * 100, 2) AS churn_rate_percentage
FROM customer_churn_ltv
GROUP BY "LTV_Segment"
ORDER BY churn_rate_percentage DESC;
"""


# 6. Revenue Value by Customer Priority
REVENUE_VALUE_BY_CUSTOMER_PRIORITY_QUERY = """
SELECT
    "Customer_Priority",
    COUNT(*) AS customer_count,
    ROUND((SUM("Estimated_LTV") / 1000000.0)::numeric, 2) AS total_ltv_million
FROM customer_churn_ltv
GROUP BY "Customer_Priority"
ORDER BY total_ltv_million DESC;
"""


# 7. LTV at Risk by Segment
LTV_AT_RISK_BY_SEGMENT_QUERY = """
SELECT
    "LTV_Segment",
    COUNT(*) AS churned_customers,
    ROUND((SUM("Estimated_LTV") / 1000000.0)::numeric, 2) AS ltv_at_risk_million,
    ROUND(AVG("Estimated_LTV")::numeric, 2) AS avg_ltv_at_risk
FROM customer_churn_ltv
WHERE "Churn" = 1
GROUP BY "LTV_Segment"
ORDER BY ltv_at_risk_million DESC;
"""


# 8. Retention Priority Summary
RETENTION_PRIORITY_SUMMARY_QUERY = """
SELECT
    "Customer_Priority",
    COUNT(*) AS customers,
    ROUND(AVG("MonthlyCharges")::numeric, 2) AS avg_monthly_charges,
    ROUND(AVG("tenure")::numeric, 0) AS avg_tenure_months,
    ROUND(AVG("Estimated_LTV")::numeric, 2) AS avg_ltv
FROM customer_churn_ltv
GROUP BY "Customer_Priority"
ORDER BY avg_ltv DESC;
"""


# 9. Segment-wise Churn and Revenue Impact
SEGMENT_WISE_CHURN_AND_REVENUE_IMPACT_QUERY = """
SELECT
    "LTV_Segment",
    COUNT(*) AS total_customers,
    SUM("Churn") AS churned_customers,
    ROUND((SUM("Churn")::numeric / COUNT(*)) * 100, 2) AS churn_rate_percentage,
    ROUND((SUM("Estimated_LTV") / 1000000.0)::numeric, 2) AS total_ltv_million,
    ROUND((SUM(CASE WHEN "Churn" = 1 THEN "Estimated_LTV" ELSE 0 END) / 1000000.0)::numeric, 2) AS churned_ltv_million
FROM customer_churn_ltv
GROUP BY "LTV_Segment"
ORDER BY churned_ltv_million DESC;
"""


# 10. Top 20 Customers to Retain
TOP_20_CUSTOMERS_TO_RETAIN_QUERY = """
SELECT
    "Customer_ID",
    "Estimated_LTV",
    "MonthlyCharges",
    "tenure",
    "LTV_Segment",
    "Customer_Priority"
FROM high_priority_customers
ORDER BY "Estimated_LTV" DESC, "MonthlyCharges" DESC
LIMIT 20;
"""


# 11. Top 10 Highest LTV Customers at Risk
TOP_10_HIGHEST_LTV_CUSTOMERS_AT_RISK_QUERY = """
SELECT
    "Customer_ID",
    "Estimated_LTV",
    "MonthlyCharges",
    "tenure",
    "LTV_Segment",
    "Customer_Priority"
FROM high_priority_customers
ORDER BY "Estimated_LTV" DESC
LIMIT 10;
"""