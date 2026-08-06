import streamlit as st
import pandas as pd
from utils.data_loader import (
    load_dataset,
    load_best_model,
    load_preprocessor
)

from utils.prediction import predict_customer

st.set_page_config(
    page_title="Customer Prediction",
    page_icon="🎯",
    layout="wide"
)

df = load_dataset()
model = load_best_model()
preprocessor = load_preprocessor()

st.title("🎯 Customer Churn Prediction")

st.markdown("""
Enter customer information below to predict the likelihood of customer churn.
""")

st.divider()




st.subheader("Customer Information")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        24
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

with col2:

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )
    contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.slider(
        "Monthly Charges",
        float(df["MonthlyCharges"].min()),
        float(df["MonthlyCharges"].max()),
        float(df["MonthlyCharges"].median())
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=float(pd.to_numeric(df["TotalCharges"], errors="coerce").median())
    )




input_df = pd.DataFrame({
    "gender": [gender],
    "SeniorCitizen": [senior_citizen],
    "Partner": [partner],
    "Dependents": [dependents],
    "tenure": [tenure],
    "PhoneService": [phone_service],
    "MultipleLines": [multiple_lines],
    "InternetService": [internet_service],
    "OnlineSecurity": [online_security],
    "OnlineBackup": [online_backup],
    "DeviceProtection": [device_protection],
    "TechSupport": [tech_support],
    "StreamingTV": [streaming_tv],
    "StreamingMovies": [streaming_movies],
    "Contract": [contract],
    "PaperlessBilling": [paperless_billing],
    "PaymentMethod": [payment_method],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges]
})


if st.button("Predict Churn", use_container_width=True):

    prediction, probability = predict_customer(
        model,
        preprocessor,
        input_df
    )

    st.divider()

    st.divider()

col1, col2 = st.columns(2)

with col1:
    if prediction == 1:
        st.error("⚠️ High Risk of Churn")
    else:
        st.success("✅ Customer is Likely to Stay")

with col2:
    st.metric(
        "Churn Probability",
        f"{probability:.2%}"
    )

st.progress(float(probability))

if probability >= 0.75:
    st.error("Recommendation: Contact the customer immediately with a personalized retention offer.")

elif probability >= 0.50:
    st.warning("Recommendation: Offer discounts or service upgrades to improve retention.")

else:
    st.success("Recommendation: The customer appears to be at low risk. Continue regular engagement.")











