import joblib
import pandas as pd

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


DATA_PATH = Path("data/processed/feature_engineered_data.csv")
MODEL_OUTPUT_PATH = Path("models/saved_model/churn_prediction_pipeline.pkl")


def train_churn_pipeline():
    df = pd.read_csv(DATA_PATH)

    X = df.drop(columns=["Churn"])
    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    churn_pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(random_state=42, max_iter=1000))
        ]
    )

    churn_pipeline.fit(X_train, y_train)

    MODEL_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(churn_pipeline, MODEL_OUTPUT_PATH)

    print("Churn prediction pipeline trained and saved successfully.")
    print(f"Saved to: {MODEL_OUTPUT_PATH}")


if __name__ == "__main__":
    train_churn_pipeline()