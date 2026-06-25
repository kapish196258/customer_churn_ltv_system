# Dashboard SQL Queries & Business Insights

This document contains the key PostgreSQL queries used for customer churn, Customer Lifetime Value (LTV), revenue risk analysis, and customer retention planning.

The queries documented here will be used later for Metabase dashboard development and business reporting.

---

# Tables Used

| Table Name              | Purpose                                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------------------ |
| customer_churn_ltv      | Final customer analytics table containing churn, LTV, segmentation, customer priority, and Customer_ID |
| high_priority_customers | High Value - High Risk customers identified for retention actions                                      |

---

# 1. Total Customers

## Business Question

How many customers are available in the final analytics table?

## SQL Query

```sql
SELECT COUNT(*) AS total_customers
FROM customer_churn_ltv;
```

## Dashboard Usage

* KPI Card
* Total Customer Count

---

# 2. High-Priority Customers

## Business Question

How many customers require immediate retention focus?

## SQL Query

```sql
SELECT COUNT(*) AS high_priority_customers
FROM high_priority_customers;
```

## Dashboard Usage

* KPI Card
* High-Priority Customer Count

---

# 3. Customer Distribution by LTV Segment

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

* Pie Chart
* Bar Chart

---

# 4. Churn Rate by LTV Segment

## Business Question

Which customer value segment experiences the highest churn rate?

## SQL Query

```sql
SELECT
    "LTV_Segment",
    COUNT(*) AS total_customers,
    SUM("Churn") AS churned_customers,
    ROUND((SUM("Churn")::numeric / COUNT(*)) * 100, 2) AS churn_rate_percentage
FROM customer_churn_ltv
GROUP BY "LTV_Segment"
ORDER BY churn_rate_percentage DESC;
```

## Dashboard Usage

* Bar Chart
* Churn Rate Analysis

---

# 5. Customer Priority Distribution

## Business Question

How many customers belong to each customer priority group?

## SQL Query

```sql
SELECT
    "Customer_Priority",
    COUNT(*) AS customer_count
FROM customer_churn_ltv
GROUP BY "Customer_Priority"
ORDER BY customer_count DESC;
```

## Dashboard Usage

* Bar Chart
* Customer Priority Analysis

---

# 6. Revenue Value by Customer Priority

## Business Question

Which customer priority group contributes the highest total customer value?

## SQL Query

```sql
SELECT
    "Customer_Priority",
    COUNT(*) AS customer_count,
    ROUND(SUM("Estimated_LTV")::numeric, 2) AS total_ltv_value
FROM customer_churn_ltv
GROUP BY "Customer_Priority"
ORDER BY total_ltv_value DESC;
```

## Dashboard Usage

* Bar Chart
* Revenue Contribution Analysis

---

# 7. LTV at Risk by Segment

## Business Question

Which customer segment represents the highest revenue exposure due to churn?

## SQL Query

```sql
SELECT
    "LTV_Segment",
    COUNT(*) AS churned_customers,
    ROUND(SUM("Estimated_LTV")::numeric, 2) AS total_ltv_at_risk,
    ROUND(AVG("Estimated_LTV")::numeric, 2) AS avg_ltv_at_risk
FROM customer_churn_ltv
WHERE "Churn" = 1
GROUP BY "LTV_Segment"
ORDER BY total_ltv_at_risk DESC;
```

## Dashboard Usage

* Revenue Risk Chart
* Retention Planning

---

# 8. Retention Priority Summary

## Business Question

What are the spending patterns, tenure, and customer value across priority groups?

## SQL Query

```sql
SELECT
    "Customer_Priority",
    COUNT(*) AS customers,
    ROUND(AVG("MonthlyCharges")::numeric, 2) AS avg_monthly_charges,
    ROUND(AVG("tenure")::numeric, 2) AS avg_tenure,
    ROUND(AVG("Estimated_LTV")::numeric, 2) AS avg_ltv
FROM customer_churn_ltv
GROUP BY "Customer_Priority"
ORDER BY avg_ltv DESC;
```

## Dashboard Usage

* Business Performance Summary
* Customer Group Comparison

---

# 9. Top Customers to Retain

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

---

# Dashboard Plan

| Dashboard Component           | Query                                |
| ----------------------------- | ------------------------------------ |
| Total Customers KPI           | Total Customers                      |
| High-Priority Customers KPI   | High-Priority Customers              |
| LTV Segment Distribution      | Customer Distribution by LTV Segment |
| Churn Rate Analysis           | Churn Rate by LTV Segment            |
| Customer Priority Analysis    | Customer Priority Distribution       |
| Revenue Contribution Analysis | Revenue Value by Customer Priority   |
| Revenue Risk Analysis         | LTV at Risk by Segment               |
| Retention Summary             | Retention Priority Summary           |
| Retention Target List         | Top Customers to Retain              |

---

# Expected Business Outcomes

* Identify customers at risk of churn.
* Quantify revenue exposure caused by churn.
* Prioritize high-value customers for retention.
* Support data-driven retention strategies.
* Provide dashboard-ready business insights.
* Enable customer-level retention actions using Customer_ID.