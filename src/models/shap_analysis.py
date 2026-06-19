import pandas as pd
import shap
import joblib
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load("models/saved_model/logistic_regression_model.pkl")

# Load feature-engineered dataset
df = pd.read_csv("data/processed/feature_engineered_data.csv")

# Separate features and target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Create SHAP explainer
explainer = shap.Explainer(model, X)

# Generate SHAP values
shap_values = explainer(X)

# SHAP Summary (Beeswarm) Plot
shap.summary_plot(
    shap_values,
    X,
    max_display=15,
    plot_size=(12, 8)
)

# SHAP Feature Importance (Bar) Plot
shap.plots.bar(
    shap_values,
    max_display=15
)