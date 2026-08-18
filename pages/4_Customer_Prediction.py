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


st.html("""
<div class="section-heading" style="text-align:left; margin-left:0;">

    <div class="section-badge">
        CUSTOMER RISK ASSESSMENT
    </div>

    <h1>
        Customer Churn Prediction
    </h1>

    <p>
        Enter customer information to estimate churn probability
        and identify the customer's risk level.
    </p>

</div>
""")


st.divider()


st.subheader("👤 Customer Information")

st.caption(
    "Enter the customer's demographic, service, contract and billing information."
)


col1, col2, col3 = st.columns(3, gap="medium")


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


with col3:

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
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
        value=float(
            pd.to_numeric(
                df["TotalCharges"],
                errors="coerce"
            ).median()
        )
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


st.divider()


predict_button = st.button(
    "🎯 Predict Customer Churn",
    use_container_width=True
)


if predict_button:

    prediction, probability = predict_customer(
        model,
        preprocessor,
        input_df
    )

    st.session_state["prediction_input"] = input_df.copy()
    st.session_state["prediction_result"] = int(prediction)
    st.session_state["prediction_probability"] = float(probability)


if "prediction_result" in st.session_state:

    prediction = st.session_state["prediction_result"]
    probability = st.session_state["prediction_probability"]


    if probability >= 0.75:

        risk_level = "High Risk"

        risk_message = (
            "This customer has a high likelihood of churning "
            "and should be prioritized for immediate retention action."
        )

    elif probability >= 0.50:

        risk_level = "Medium Risk"

        risk_message = (
            "This customer shows meaningful churn risk "
            "and should receive proactive engagement."
        )

    else:

        risk_level = "Low Risk"

        risk_message = (
            "This customer currently shows a relatively low "
            "likelihood of churn."
        )


    st.divider()


    st.html("""
    <div class="section-heading">

        <div class="section-badge">
            PREDICTION RESULT
        </div>

        <h2>
            Customer Risk Assessment
        </h2>

    </div>
    """)


    col1, col2, col3 = st.columns(3)


    with col1:

        if prediction == 1:

            st.error(
                "⚠️ Customer Likely to Churn"
            )

        else:

            st.success(
                "✅ Customer Likely to Stay"
            )


    with col2:

        st.metric(
            "Churn Probability",
            f"{probability:.2%}"
        )


    with col3:

        st.metric(
            "Risk Level",
            risk_level
        )


    st.progress(probability)


    if probability >= 0.75:

        st.error(
            f"**High-Risk Recommendation:** {risk_message} "
            "Consider a personalized retention offer, proactive "
            "customer outreach, or service intervention."
        )

    elif probability >= 0.50:

        st.warning(
            f"**Medium-Risk Recommendation:** {risk_message} "
            "Consider targeted discounts, service upgrades, "
            "or personalized engagement."
        )

    else:

        st.success(
            f"**Low-Risk Recommendation:** {risk_message} "
            "Continue normal customer engagement and monitoring."
        )


    st.divider()


    st.html("""
    <div class="section-heading">

        <div class="section-badge">
            EXPLAINABLE AI
        </div>

        <h2>
            Why This Prediction?
        </h2>

        <p>
            Explore which customer characteristics influenced
            the machine learning model's prediction.
        </p>

    </div>
    """)


    if st.button(
        "🧠 Why This Prediction?",
        use_container_width=True,
        key="why_prediction_button"
    ):

        st.switch_page(
            "pages/6_SHAP_Explainability.py"
        )


st.divider()


st.caption(
    "Prediction powered by machine learning and "
    "Explainable AI (SHAP)."
)