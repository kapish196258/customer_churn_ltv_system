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

- Project Repository Setup
- Virtual Environment Setup
- Exploratory Data Analysis (EDA)
- Data Cleaning & Preprocessing
- Missing Value Handling
- Data Type Corrections
- PostgreSQL Installation
- pgAdmin Setup
- PostgreSQL Database Creation
- PostgreSQL-Python Integration
- Dataset Upload to PostgreSQL
- Environment Variable Security (.env)

### In Progress

- PostgreSQL Query Analysis

### Upcoming

- Feature Engineering
- Model Training
- Customer Lifetime Value (LTV) Modeling
- FastAPI Development
- Dashboard Development

---

## System Architecture

```text
Raw Dataset
    ↓
Data Cleaning
    ↓
PostgreSQL Database
    ↓
Feature Engineering
    ↓
Machine Learning Models
    ↓
FastAPI
    ↓
Dashboard
    ↓
Business Insights
``` 

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

telco_customer_churn

The cleaned dataset is stored inside PostgreSQL and will be used for feature engineering, machine learning, API development, and dashboard visualization.

---

## Project Structure
customer_churn_ltv_system/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── eda.ipynb
│   ├── feature_engineering.ipynb
│
├── src/
│   ├── data_engineering/
│   │   ├── ingest.py
│   │   ├── database.py
│   │
│   ├── preprocessing/
│   │   ├── clean_data.py
│   │   ├── feature_engineering.py
│   │
│   ├── models/
│   │   ├── train_model.py
│   │   ├── predict.py
│   │
│   ├── ltv/
│   │   ├── ltv_model.py
│   │
│   ├── utils/
│   │   ├── config.py
│   │   ├── helpers.py
│
├── api/
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│
├── dashboard/
│   ├── (for Superset/Metabase configs later)
│
├── models/
│   ├── saved_models/
│
├── requirements.txt
├── README.md
├── .gitignore

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
| Data Cleaning | Completed |
| PostgreSQL Integration | Completed |
| PostgreSQL Query Analysis | In Progress |
| Feature Engineering | Pending |
| Model Training | Pending |
| FastAPI Development | Pending |
| Dashboard Development | Pending |
| Deployment | Pending |

---

