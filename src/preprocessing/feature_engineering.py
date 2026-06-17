import pandas as pd

def engineer_features(df):
"""
Perform feature engineering on customer churn data.
"""

```
# Encode target variable
df["Churn"] = df["Churn"].map({
    "Yes": 1,
    "No": 0
})

# Remove identifier column
df.drop(
    columns=["customerID"],
    inplace=True
)

# Encode binary features
binary_mapping = {
    "Yes": 1,
    "No": 0,
    "Female": 1,
    "Male": 0
}

binary_cols = [
    "gender",
    "Partner",
    "Dependents",
    "PhoneService",
    "PaperlessBilling"
]

for col in binary_cols:
    df[col] = df[col].map(binary_mapping)

# One-Hot Encoding
df = pd.get_dummies(
    df,
    columns=[
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaymentMethod"
    ],
    drop_first=True
)

# Convert boolean columns to integers
bool_cols = df.select_dtypes(
    include="bool"
).columns

df[bool_cols] = df[bool_cols].astype(int)

return df
```
