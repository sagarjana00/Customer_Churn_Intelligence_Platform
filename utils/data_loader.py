import pandas as pd
import joblib

from config import (
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    MODELS_DIR
)


def load_dataset():
    return pd.read_csv(RAW_DATA_DIR / "WA_Fn-UseC_-Telco-Customer-Churn.csv")


def load_processed_data():
    x_test = joblib.load(PROCESSED_DATA_DIR / "x_test_processed.pkl")
    y_test = joblib.load(PROCESSED_DATA_DIR / "y_test.pkl")

    return x_test, y_test


def load_best_model():
    return joblib.load(MODELS_DIR / "best_model.pkl")