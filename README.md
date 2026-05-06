# 📊 Customer Churn Prediction & Lifetime Value (LTV) System

## 🚀 Overview
This project is a **production-level data analytics system** designed to predict customer churn and estimate Customer Lifetime Value (LTV) for a telecom or subscription-based business.

The system enables organizations to:
- Identify customers at risk of churn  
- Prioritize high-value customers  
- Optimize marketing and retention strategies  

---

## 🧠 Problem Statement
Customer churn directly impacts revenue and growth in subscription-based businesses.  
This project aims to:
- Predict the probability of customer churn  
- Estimate long-term customer value (LTV)  
- Provide actionable insights through dashboards  

---

## 🏗️ System Architecture

Raw Dataset → PostgreSQL → Data Processing → Machine Learning Models → API → Dashboard  

---

## 🛠️ Tech Stack

### 👨‍💻 Programming Languages
- Python  
- SQL  

### 🗄️ Data Engineering & Storage
- PostgreSQL  
- SQLAlchemy  

### 📊 Data Analysis & Machine Learning
- Pandas  
- NumPy  
- Scikit-learn  
- XGBoost  
- SHAP (Model Explainability)  

### 🌐 API Layer
- FastAPI  

### 📈 Visualization & Dashboard
- Metabase / Apache Superset  

---

## 📂 Project Structure
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



