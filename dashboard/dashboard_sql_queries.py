"""
Reusable SQL queries for Metabase dashboard development.

These queries are used to create KPI cards, charts, and tables for
customer churn, LTV, revenue risk, customer segmentation, and retention analysis.

Metabase Dashboard Filter:
- Filter Name: LTV Segment
- Variable Name: ltv_segment
- Variable Type: Field Filter
- Field Mapping: customer_churn_ltv -> LTV_Segment
- Filter Values: Low Value, Medium Value, High Value
"""

# ============================================================
# KPI QUERIES
# ============================================================

# 1. Total Customers
TOTAL_CUSTOMERS_QUERY = """
SELECT 
    COUNT(*) AS total_customers
FROM customer_churn_ltv;
"""


# 2. Overall Churn Rate
# Filter-enabled using LTV Segment
OVERALL_CHURN_RATE_QUERY = """
SELECT
    ROUND((SUM("Churn")::numeric / COUNT(*)) * 100, 2) AS overall_churn_rate_percentage
FROM customer_churn_ltv
WHERE 1=1
[[AND {{ltv_segment}}]];
"""


# 3. Total LTV at Risk Millions
TOTAL_LTV_AT_RISK_MILLIONS_QUERY = """
SELECT
    ROUND((SUM("Estimated_LTV") / 1000000.0)::numeric, 2) AS total_ltv_at_risk_million
FROM high_priority_customers;
"""


# 4. High Priority Customers
HIGH_PRIORITY_CUSTOMERS_QUERY = """
SELECT 
    COUNT(*) AS high_priority_customers
FROM high_priority_customers;
"""


# ============================================================
# EXECUTIVE OVERVIEW CHART QUERIES
# ============================================================

# 5. Churn vs Non-Churn Customers
# Filter-enabled using LTV Segment
CHURN_VS_NON_CHURN_CUSTOMERS_QUERY = """
SELECT
    CASE 
        WHEN "Churn" = 1 THEN 'Churned'
        ELSE 'Not Churned'
    END AS churn_status,
    COUNT(*) AS customer_count
FROM customer_churn_ltv
WHERE 1=1
[[AND {{ltv_segment}}]]
GROUP BY churn_status
ORDER BY customer_count DESC;
"""


# 6. Customer Distribution by LTV Segment
CUSTOMER_DISTRIBUTION_BY_LTV_SEGMENT_QUERY = """
SELECT
    "LTV_Segment",
    COUNT(*) AS customer_count
FROM customer_churn_ltv
GROUP BY "LTV_Segment"
ORDER BY customer_count DESC;
"""


# 7. Churn Rate by LTV Segment
CHURN_RATE_BY_LTV_SEGMENT_QUERY = """
SELECT
    "LTV_Segment",
    ROUND((SUM("Churn")::numeric / COUNT(*)) * 100, 2) AS churn_rate_percentage
FROM customer_churn_ltv
GROUP BY "LTV_Segment"
ORDER BY churn_rate_percentage DESC;
"""


# 8. Revenue Value by Customer Priority
# Filter-enabled using LTV Segment
REVENUE_VALUE_BY_CUSTOMER_PRIORITY_QUERY = """
SELECT
    "Customer_Priority",
    COUNT(*) AS customer_count,
    ROUND((SUM("Estimated_LTV") / 1000000.0)::numeric, 2) AS total_ltv_million
FROM customer_churn_ltv
WHERE 1=1
[[AND {{ltv_segment}}]]
GROUP BY "Customer_Priority"
ORDER BY total_ltv_million DESC;
"""


# 9. LTV at Risk by Segment
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


# ============================================================
# RETENTION ACTION TABLE QUERIES
# ============================================================

# 10. Retention Priority Summary
# Filter-enabled using LTV Segment
RETENTION_PRIORITY_SUMMARY_QUERY = """
SELECT
    "Customer_Priority",
    COUNT(*) AS customers,
    ROUND(AVG("MonthlyCharges")::numeric, 2) AS avg_monthly_charges,
    ROUND(AVG("tenure")::numeric, 0) AS avg_tenure_months,
    ROUND(AVG("Estimated_LTV")::numeric, 2) AS avg_ltv
FROM customer_churn_ltv
WHERE 1=1
[[AND {{ltv_segment}}]]
GROUP BY "Customer_Priority"
ORDER BY avg_ltv DESC;
"""


# 11. Segment-wise Churn and Revenue Impact
# Filter-enabled using LTV Segment
SEGMENT_WISE_CHURN_AND_REVENUE_IMPACT_QUERY = """
SELECT
    "LTV_Segment",
    COUNT(*) AS total_customers,
    SUM("Churn") AS churned_customers,
    ROUND((SUM("Churn")::numeric / COUNT(*)) * 100, 2) AS churn_rate_percentage,
    ROUND((SUM("Estimated_LTV") / 1000000.0)::numeric, 2) AS total_ltv_million,
    ROUND((SUM(CASE WHEN "Churn" = 1 THEN "Estimated_LTV" ELSE 0 END) / 1000000.0)::numeric, 2) AS churned_ltv_million
FROM customer_churn_ltv
WHERE 1=1
[[AND {{ltv_segment}}]]
GROUP BY "LTV_Segment"
ORDER BY churned_ltv_million DESC;
"""


# 12. Top 20 Customers to Retain
# Filter-enabled using LTV Segment
TOP_20_CUSTOMERS_TO_RETAIN_QUERY = """
SELECT
    "Customer_ID",
    "Estimated_LTV",
    "MonthlyCharges",
    "tenure",
    "LTV_Segment",
    "Customer_Priority"
FROM customer_churn_ltv
WHERE "Churn" = 1
[[AND {{ltv_segment}}]]
ORDER BY "Estimated_LTV" DESC, "MonthlyCharges" DESC
LIMIT 20;
"""


# 13. Top 10 Highest LTV Customers at Risk
# Filter-enabled using LTV Segment
TOP_10_HIGHEST_LTV_CUSTOMERS_AT_RISK_QUERY = """
SELECT
    "Customer_ID",
    "Estimated_LTV",
    "MonthlyCharges",
    "tenure",
    "LTV_Segment",
    "Customer_Priority"
FROM customer_churn_ltv
WHERE "Churn" = 1
[[AND {{ltv_segment}}]]
ORDER BY "Estimated_LTV" DESC
LIMIT 10;
"""