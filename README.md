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

### In Progress

* Customer Lifetime Value (LTV) Modeling
* Dashboard Development (Metabase)

### Upcoming

* Prediction Storage in PostgreSQL
* Dockerization
* Final Deployment
* Final Documentation

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

telco_customer_churn

The cleaned dataset is stored inside PostgreSQL and will be used for feature engineering, machine learning, API development, and dashboard visualization.

---

## Project Structure

```text
customer_churn_ltv_system/
├── api/
│   ├── main.py
│   └── schemas.py
├── data/
│   ├── raw/
│   └── processed/
│       └── feature_engineered_data.csv
├── models/
│   └── saved_model/
│       └── logistic_regression_model.pkl
├── notebooks/
│   ├── eda.ipynb
│   ├── data_cleaning.ipynb
│   ├── feature_engineering.ipynb
│   ├── model_preparation.ipynb
│   ├── model_training.ipynb
│   └── shap_analysis.ipynb
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

| Phase                         | Status      |
| ----------------------------- | ----------- |
| Project Setup                 | Completed   |
| EDA                           | Completed   |
| Data Cleaning                 | Completed   |
| PostgreSQL Integration        | Completed   |
| PostgreSQL Query Analysis     | Completed   |
| Feature Engineering           | Completed   |
| Model Preparation             | Completed   |
| Model Training & Evaluation   | Completed   |
| Model Selection & Persistence | Completed   |
| SHAP Explainability           | Completed   |
| FastAPI Development           | In Progress |
| LTV Modeling                  | Pending     |
| Dashboard Development         | Pending     |
| Deployment                    | Pending     |


---

## Recent Updates

- Completed PostgreSQL Query Analysis
- Completed Feature Engineering Pipeline
- Completed Model Preparation (Train-Test Split & Feature Scaling)
- Completed Multi-Model Training and Evaluation
- Selected Logistic Regression as the Final Model
- Added Model Persistence using Joblib (`.pkl`)
- Added Prediction Pipeline (`churn_predict.py`)
- Added SHAP Explainability Analysis
- Added SHAP Automation Script (`shap_analysis.py`)
- Implemented FastAPI Application
- Added Prediction API Endpoint
- Successfully Tested API using Swagger UI

---

## FastAPI Usage

The churn prediction model is exposed using FastAPI.

To run the API locally:

```bash
uvicorn api.main:app --reload

**Open Swagger UI:** http://127.0.0.1:8000/docs