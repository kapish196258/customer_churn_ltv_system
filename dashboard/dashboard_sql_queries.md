# Dashboard SQL Queries & Business Insights

This document contains the key PostgreSQL queries used for customer churn, Customer Lifetime Value (LTV), revenue risk analysis, customer segmentation, and customer retention planning.

The queries documented here are used for Metabase dashboard development and business reporting.

---

# Tables Used

| Table Name              | Purpose                                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------------------ |
| customer_churn_ltv      | Final customer analytics table containing churn, LTV, segmentation, customer priority, and Customer_ID |
| high_priority_customers | High Value - High Risk customers identified for retention actions                                      |

---

# Dashboard SQL Queries

This section contains the SQL queries used to build the Metabase dashboard for churn analysis, LTV analysis, revenue risk, and retention decision-making.

---

# 1. Total Customers

## Business Question

How many customers are available in the final analytics table?

## SQL Query

```sql
SELECT 
    COUNT(*) AS total_customers
FROM customer_churn_ltv;
```

## Dashboard Usage

* KPI Card
* Total Customer Count
* Executive Overview

---

# 2. High-Priority Customers

## Business Question

How many customers require immediate retention focus?

## SQL Query

```sql
SELECT 
    COUNT(*) AS high_priority_customers
FROM high_priority_customers;
```

## Dashboard Usage

* KPI Card
* High-Priority Customer Count
* Retention Risk Overview

---

# 3. Total LTV at Risk Millions

## Business Question

What is the total estimated customer value at risk among high-priority customers?

## SQL Query

```sql
SELECT
    ROUND((SUM("Estimated_LTV") / 1000000.0)::numeric, 2) AS total_ltv_at_risk_million
FROM high_priority_customers;
```

## Dashboard Usage

* KPI Card
* Revenue Risk Indicator
* Executive Business Impact

---

# 4. Customer Distribution by LTV Segment

## Business Question

How are customers distributed across Low Value, Medium Value, and High Value segments?

## SQL Query

```sql
SELECT
    "LTV_Segment",
    COUNT(*) AS customer_count
FROM customer_churn_ltv
GROUP BY "LTV_Segment"
ORDER BY customer_count DESC;
```

## Dashboard Usage

* Donut Chart
* Pie Chart
* Customer Segmentation Overview

---

# 5. Churn Rate by LTV Segment

## Business Question

Which customer value segment experiences the highest churn rate?

## SQL Query

```sql
SELECT
    "LTV_Segment",
    ROUND((SUM("Churn")::numeric / COUNT(*)) * 100, 2) AS churn_rate_percentage
FROM customer_churn_ltv
GROUP BY "LTV_Segment"
ORDER BY churn_rate_percentage DESC;
```

## Dashboard Usage

* Bar Chart
* Churn Rate Analysis
* Segment Risk Comparison

---

# 6. Revenue Value by Customer Priority

## Business Question

Which customer priority group contributes the highest total estimated customer value?

## SQL Query

```sql
SELECT
    "Customer_Priority",
    COUNT(*) AS customer_count,
    ROUND((SUM("Estimated_LTV") / 1000000.0)::numeric, 2) AS total_ltv_million
FROM customer_churn_ltv
GROUP BY "Customer_Priority"
ORDER BY total_ltv_million DESC;
```

## Dashboard Usage

* Horizontal Bar Chart
* Revenue Contribution Analysis
* Customer Priority Comparison

---

# 7. LTV at Risk by Segment

## Business Question

Which customer value segment represents the highest revenue exposure due to churn?

## SQL Query

```sql
SELECT
    "LTV_Segment",
    COUNT(*) AS churned_customers,
    ROUND((SUM("Estimated_LTV") / 1000000.0)::numeric, 2) AS ltv_at_risk_million,
    ROUND(AVG("Estimated_LTV")::numeric, 2) AS avg_ltv_at_risk
FROM customer_churn_ltv
WHERE "Churn" = 1
GROUP BY "LTV_Segment"
ORDER BY ltv_at_risk_million DESC;
```

## Dashboard Usage

* Donut Chart
* Revenue Risk Chart
* Segment-wise Retention Planning

---

# 8. Retention Priority Summary

## Business Question

What are the spending patterns, tenure, and customer value across different customer priority groups?

## SQL Query

```sql
SELECT
    "Customer_Priority",
    COUNT(*) AS customers,
    ROUND(AVG("MonthlyCharges")::numeric, 2) AS avg_monthly_charges,
    ROUND(AVG("tenure")::numeric, 0) AS avg_tenure_months,
    ROUND(AVG("Estimated_LTV")::numeric, 2) AS avg_ltv
FROM customer_churn_ltv
GROUP BY "Customer_Priority"
ORDER BY avg_ltv DESC;
```

## Dashboard Usage

* Table
* Business Performance Summary
* Customer Group Comparison
* Retention Strategy Planning

---

# 9. Segment-wise Churn and Revenue Impact

## Business Question

How do customer count, churn count, churn rate, total LTV, and churned LTV compare across LTV segments?

## SQL Query

```sql
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
```

## Dashboard Usage

* Table
* Pivot Table
* Segment-wise Business Impact Analysis
* Churn and Revenue Comparison

---

# 10. Top 20 Customers to Retain

## Business Question

Which customers should be prioritized first for retention efforts?

## SQL Query

```sql
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
```

## Dashboard Usage

* Retention Target Table
* Customer Success Actions
* High-Priority Customer List

---

# 11. Top 10 Highest LTV Customers at Risk

## Business Question

Which are the top 10 highest-value customers currently at churn risk?

## SQL Query

```sql
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
```

## Dashboard Usage

* Executive Customer Risk Table
* Highest-Value Retention Targets
* Customer-Level Action Planning

---

# Dashboard Plan

| Dashboard Component           | Query Used                            | Recommended Visualization |
| ----------------------------- | ------------------------------------- | ------------------------- |
| Total Customers KPI           | Total Customers                       | KPI Number                |
| High-Priority Customers KPI   | High-Priority Customers               | KPI Number                |
| Total LTV at Risk KPI         | Total LTV at Risk Millions            | KPI Number                |
| LTV Segment Distribution      | Customer Distribution by LTV Segment  | Donut Chart               |
| Churn Rate Analysis           | Churn Rate by LTV Segment             | Bar Chart                 |
| Revenue Contribution Analysis | Revenue Value by Customer Priority    | Horizontal Bar Chart      |
| Revenue Risk Analysis         | LTV at Risk by Segment                | Donut Chart               |
| Retention Summary             | Retention Priority Summary            | Table                     |
| Segment Impact Analysis       | Segment-wise Churn and Revenue Impact | Table / Pivot Table       |
| Retention Target List         | Top 20 Customers to Retain            | Table                     |
| Highest LTV Customers at Risk | Top 10 Highest LTV Customers at Risk  | Table                     |

---

# Recommended Dashboard Tabs

## Tab 1: Executive Overview

This tab focuses on high-level business KPIs and visual insights.

Recommended components:

* Total Customers KPI
* High-Priority Customers KPI
* Total LTV at Risk KPI
* Customer Distribution by LTV Segment
* Churn Rate by LTV Segment
* Revenue Value by Customer Priority
* LTV at Risk by Segment

## Tab 2: Retention Action & Customer Insights

This tab focuses on deeper analysis and customer-level retention actions.

Recommended components:

* Retention Priority Summary
* Segment-wise Churn and Revenue Impact
* Top 20 Customers to Retain
* Top 10 Highest LTV Customers at Risk

---

# Expected Business Outcomes

* Identify customers at risk of churn.
* Quantify estimated revenue exposure caused by churn.
* Segment customers based on estimated lifetime value.
* Prioritize high-value customers for retention campaigns.
* Support data-driven customer retention strategies.
* Provide dashboard-ready business insights.
* Enable customer-level retention actions using Customer_ID.
* Help business teams focus on customers with the highest financial impact.

---

# Summary

These SQL queries support the complete customer churn and LTV dashboard workflow.

The dashboard helps answer:

* How many customers exist in the final dataset?
* How many customers are high-priority?
* How much estimated LTV is at risk?
* Which customer segments churn the most?
* Which customer groups contribute the most value?
* Which customers should be retained first?

This makes the dashboard useful for both technical analysis and business decision-making.