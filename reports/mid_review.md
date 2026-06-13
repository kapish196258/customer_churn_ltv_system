# Customer Churn Prediction & Customer Lifetime Value (LTV) System

## Mid Review Progress Report

## Project Overview

The objective of this project is to analyze customer behavior, identify churn patterns, and develop a system capable of predicting customer churn and estimating Customer Lifetime Value (LTV). The solution combines data analytics, machine learning, database integration, API development, and business intelligence to support data-driven decision-making.

---

## Work Completed

### Project Setup

- Created the GitHub repository and project structure
- Organized folders for datasets, notebooks, source code, and reports
- Configured Python virtual environment
- Installed required libraries and development tools
- Set up Jupyter Notebook environment

### Repository Management

- Established Git and GitHub workflow for collaboration
- Managed repository access and project organization
- Maintained project progress through commits, pushes, and pulls
- Tracked development using version control

### Exploratory Data Analysis (EDA)

- Dataset inspection
- Statistical summary analysis
- Data type validation
- Missing value analysis
- Duplicate record analysis
- Unique value analysis
- Customer churn exploration
- Business insight generation through visualizations

### Visualizations Performed

- Churn Distribution
- Contract Type vs Churn
- Monthly Charges vs Churn
- Tenure vs Churn
- Internet Service vs Churn
- Payment Method vs Churn
- Correlation Heatmap

---

## Source Code Documentation

### EDA Notebook

**File:** `notebooks/eda.ipynb`

Contains exploratory data analysis, statistical summaries, data quality checks, and visualizations used to identify churn patterns and business insights.

### Data Cleaning Notebook

**File:** `notebooks/data_cleaning.ipynb`

Contains initial data cleaning tasks, including datatype validation, missing value analysis, duplicate checks, and dataset preparation.

### Dataset Files

**Raw Dataset**

```text
data/raw/Telco-Customer-Churn.csv
```

Original dataset used for analysis and preprocessing.

**Processed Dataset**

```text
data/processed/cleaned_telco_data.csv
```

Dataset generated after the initial cleaning process.

### Development Environment

The project was developed using:

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn

A Python virtual environment was created and used throughout development to manage project dependencies.

### Version Control

Git and GitHub were used for project management and collaboration.

Activities performed:

- Repository creation
- Repository cloning
- Pulling latest changes
- Committing updates
- Pushing changes to GitHub
- Tracking project progress through version control

---

## Key Findings

The exploratory analysis identified several important churn indicators:

- Customers with month-to-month contracts exhibit higher churn rates.
- Customers with shorter tenure are more likely to leave the service.
- Higher monthly charges are associated with increased churn.
- Fiber optic customers demonstrate comparatively higher churn behavior.
- Electronic check users show higher churn rates than other payment groups.
- The `TotalCharges` column was identified as a datatype inconsistency and required conversion from object to numeric format.

---

## Data Cleaning Progress

### Completed

- Data type validation
- Conversion of `TotalCharges` to numeric datatype
- Missing value identification and handling
- Duplicate record verification
- Cleaned dataset generation

### Remaining Tasks

- Validate numerical columns for invalid values
- Check for outliers in key numerical features
- Review categorical columns for inconsistent values
- Verify data quality after cleaning
- Finalize the processed dataset for feature engineering

---

## Team Contributions

### Kapish Gupta (Team Leader)

- Repository setup and project structure creation
- GitHub workflow management
- Exploratory Data Analysis (EDA)
- Project documentation and reporting

### Vishnukant Dharmendra

- Initial data cleaning
- Dataset preprocessing
- Cleaned dataset generation

### Sumit Prakash

- Repository cloning
- Development environment setup

### Leela Durga

- Contribution pending

---

## Current Project Status

### Completed

- Project setup
- GitHub repository management
- Exploratory Data Analysis (EDA)
- Initial data cleaning
- Dataset quality assessment

### Current Phase

- Data cleaning validation and finalization

---

## Next Phase

- Complete remaining data cleaning tasks
- Perform feature engineering
- Integrate PostgreSQL database
- Develop churn prediction and LTV models
- Build FastAPI endpoints
- Implement authentication and security
- Create dashboards and deploy the solution

---

## Challenges Faced

- Understanding dataset quality issues
- Identifying datatype inconsistencies
- Establishing a collaborative Git workflow
- Organizing a scalable project structure
- Interpreting business insights from customer churn data

---

## Conclusion

The project is progressing according to the planned roadmap. The dataset has been explored, key churn patterns have been identified, and the initial data cleaning phase has been completed. The next stage will focus on finalizing data preparation, feature engineering, and developing predictive models for churn prediction and Customer Lifetime Value estimation.