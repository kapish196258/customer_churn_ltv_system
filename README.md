# Customer Churn Prediction & Lifetime Value (LTV) System

## Overview
This project is a **production-level data analytics system** designed to predict customer churn and estimate Customer Lifetime Value (LTV) for a telecom or subscription-based business.

The system enables organizations to:
- Identify customers at risk of churn  
- Prioritize high-value customers  
- Optimize marketing and retention strategies  

---

## Problem Statement
Customer churn directly impacts revenue and growth in subscription-based businesses.  
This project aims to:
- Predict the probability of customer churn  
- Estimate long-term customer value (LTV)  
- Provide actionable insights through dashboards  

---

## Current Project Status

### Completed

* Project Repository Setup
* Virtual Environment Setup
* Exploratory Data Analysis (EDA)
* Data Cleaning & Preprocessing
* Missing Value Handling
* Data Type Corrections
* PostgreSQL Installation
* pgAdmin Setup
* PostgreSQL Database Creation
* PostgreSQL-Python Integration
* Dataset Upload to PostgreSQL
* Environment Variable Security (.env)
* PostgreSQL Query Analysis
* Feature Engineering
* Model Preparation (Train-Test Split & Feature Scaling)
* Multi-Model Training & Evaluation
* Final Model Selection (Logistic Regression)
* Model Persistence using Joblib (.pkl)
* Prediction Pipeline (`churn_predict.py`)
* SHAP Model Explainability
* FastAPI Setup
* FastAPI Prediction Endpoint
* Swagger UI Testing
* Customer Lifetime Value (LTV) Modeling
* LTV Segmentation
* Customer Priority Matrix
* High-Priority Customer Identification
* Customer Data Enrichment (Customer_ID Restoration)
* PostgreSQL Integration of LTV Datasets

### In Progress

* Customer Lifetime Value (LTV) Modeling
* Dashboard Development (Metabase)

### Upcoming

* Dashboard Development using Metabase
* Advanced SQL Business Insights
* Dockerization
* Final Deployment
* Final Documentation

---

## System Architecture

```text
Raw Dataset
    ↓
Data Cleaning & Preprocessing
    ↓
PostgreSQL Database
    ↓
Feature Engineering
    ↓
Model Preparation
    ↓
Machine Learning Model Training
    ↓
Model Evaluation & Selection
    ↓
Model Explainability (SHAP)
    ↓
FastAPI Prediction API
    ↓
Customer Lifetime Value (LTV) Modeling
    ↓
Customer Segmentation & Priority Matrix
    ↓
PostgreSQL Business Analytics Tables
    ↓
Dashboard Development (Metabase)
    ↓
Business Insights & Retention Strategy
---

## Tech Stack

### Programming Languages
- Python  
- SQL  

### Data Engineering & Storage
- PostgreSQL  
- SQLAlchemy  

### Data Analysis & Machine Learning
- Pandas  
- NumPy
- Seaborn  
- Scikit-learn  
- XGBoost
- Logistic Regression
- Random Forest  
- SHAP (Model Explainability)  

### API Layer
- FastAPI  

### Visualization & Dashboard
- Metabase / Apache Superset  

---

## Database Information

Database: PostgreSQL

Database Name:

customer_churn_db

Main Table:

| Table Name | Purpose |
|----------|---------|
| `telco_customer_churn` | Cleaned customer churn dataset stored in PostgreSQL |
| `customer_churn_ltv` | Final analytics table containing churn, LTV, customer segments, priority groups, and Customer_ID |
| `high_priority_customers` | Subset of High Value - High Risk customers for retention-focused analysis |

The PostgreSQL database is used to store cleaned data, final LTV-enhanced customer data, and high-priority customer segments. These tables will later support SQL analysis, dashboard development, and business reporting.
---

## Project Structure

```text
customer_churn_ltv_system/
├── api/
│   ├── main.py
│   ├── routes.py
│   └── schemas.py
├── data/
│   ├── raw/
│   └── processed/
│       ├── cleaned_telco_data.csv
│       ├── feature_engineered_data.csv
│       ├── customer_churn_ltv_final.csv
│       └── high_priority_customers.csv
├── models/
│   └── saved_model/
│       └── logistic_regression_model.pkl
├── notebooks/
│   ├── eda.ipynb
│   ├── data_cleaning.ipynb
│   ├── feature_engineering.ipynb
│   ├── model_preparation.ipynb
│   ├── model_training.ipynb
│   ├── shap_analysis.ipynb
│   ├── ltv_modelling.ipynb
│   ├── ltv_postgresql_integration.ipynb
│   ├── ltv_postgresql_analysis.ipynb
│   └── customer_data_enrichment.ipynb
├── reports/
├── src/
│   ├── database/
│   │   └── connection.py
│   ├── preprocessing/
│   │   ├── clean.py
│   │   └── feature_engineering.py
│   └── models/
│       ├── churn_predict.py
│       └── shap_analysis.py
├── requirements.txt
├── README.md
└── .gitignore

```

---

## Security

Sensitive credentials are stored using environment variables.

Files excluded from GitHub:

- .env
- venv/
- __pycache__/

Database passwords and local configuration files are never pushed to the repository.

---

## Project Progress

| Phase | Status |
|---------|---------|
| Project Setup | Completed |
| EDA | Completed |
| Data Cleaning & Preprocessing | Completed |
| PostgreSQL Integration | Completed |
| PostgreSQL Query Analysis | Completed |
| Feature Engineering | Completed |
| Model Preparation | Completed |
| Model Training & Evaluation | Completed |
| Model Selection & Persistence | Completed |
| SHAP Explainability | Completed |
| FastAPI Development | Completed |
| LTV Modeling | Completed |
| Customer Segmentation | Completed |
| Customer Priority Matrix | Completed |
| Customer Data Enrichment | Completed |
| PostgreSQL LTV Integration | Completed |
| PostgreSQL Business Analysis | In Progress |
| Dashboard Development | Pending |
| Dockerization | Pending |
| Deployment | Pending |


---

## Recent Updates

- Completed Customer Lifetime Value (LTV) Modeling
- Created LTV Segmentation using Estimated LTV
- Built Customer Priority Matrix by combining LTV segment and churn status
- Identified High Value - High Risk customers for retention planning
- Exported final LTV-enhanced customer dataset
- Exported high-priority customer dataset
- Restored Customer_ID for business reporting and customer-level tracking
- Loaded final LTV dataset into PostgreSQL
- Created `customer_churn_ltv` table
- Created `high_priority_customers` table
- Started PostgreSQL Business Analysis on LTV and customer priority tables

---

## FastAPI Usage

The churn prediction model is exposed using FastAPI.

To run the API locally:

```bash
uvicorn api.main:app --reload

**Open Swagger UI:** http://127.0.0.1:8000/docs

## LTV Modeling & Customer Analytics

The project now includes Customer Lifetime Value (LTV) modeling to estimate customer value and support retention-focused business decisions.

### What Was Added

- Estimated LTV calculation using customer tenure and monthly charges
- LTV Segmentation into Low Value, Medium Value, and High Value customers
- Customer Priority Matrix based on LTV segment and churn status
- High Value - High Risk customer identification
- Customer_ID restoration for customer-level tracking
- PostgreSQL tables for final analytics and high-priority customers

### Why Customer_ID Was Restored

Customer_ID was removed during model training because it does not help the machine learning model predict churn. However, it was restored later for business analytics because customer-level identification is required for reporting, dashboards, and retention actions.

### Business Value

This helps the business identify:

- Which customers are likely to churn
- Which customers are most valuable
- Which customers should be prioritized for retention
- Which customer segments create the highest revenue risk

The `high_priority_customers` dataset contains the customers who are both high-value and at risk of churn, making it useful for retention campaigns and customer success actions.
