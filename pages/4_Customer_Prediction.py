import streamlit as st
import pandas as pd
import shap
import plotly.express as px

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

explainer = shap.TreeExplainer(model)


st.html("""
<div class="section-heading" style="text-align:left; margin-left:0;">

    <div class="section-badge">
        CUSTOMER RISK ASSESSMENT
    </div>

    <h1>
        Customer Churn Prediction
    </h1>

    <p>
        Enter customer information to estimate churn probability,
        identify the customer's risk level, and understand the
        factors influencing the prediction.
    </p>

</div>
""")


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        CUSTOMER PROFILE
    </div>

    <h2>
        Customer Information
    </h2>

    <p>
        Provide the customer's demographic and account information.
    </p>

</div>
""")


col1, col2 = st.columns(2, gap="large")


with col1:

    st.subheader("👤 Demographics")

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


with col2:

    st.subheader("📱 Phone Services")

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        SERVICE USAGE
    </div>

    <h2>
        Internet & Additional Services
    </h2>

    <p>
        Select the services currently subscribed to by the customer.
    </p>

</div>
""")


col1, col2 = st.columns(2, gap="large")


with col1:

    st.subheader("🌐 Internet Services")

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


with col2:

    st.subheader("🎬 Entertainment & Support")

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


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        ACCOUNT & BILLING
    </div>

    <h2>
        Contract & Payment Information
    </h2>

</div>
""")


col1, col2 = st.columns(2, gap="large")


with col1:

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


with col2:

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


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        PREDICTION ENGINE
    </div>

    <h2>
        Ready to Assess Customer Risk?
    </h2>

    <p>
        The trained machine learning model will evaluate the customer
        profile and estimate the probability of churn.
    </p>

</div>
""")


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

    probability = float(probability)

    processed_input = preprocessor.transform(
        input_df
    )

    shap_values = explainer.shap_values(
        processed_input
    )

    if isinstance(shap_values, list):
        shap_values = shap_values[-1]

    shap_values = shap_values[0]


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


    if probability >= 0.75:

        risk_level = "High Risk"
        risk_message = (
            "This customer has a high likelihood of churning "
            "and should be prioritized for immediate retention action."
        )

    elif probability >= 0.50:

        risk_level = "Medium Risk"
        risk_message = (
            "This customer shows meaningful churn risk and "
            "should receive proactive engagement."
        )

    else:

        risk_level = "Low Risk"
        risk_message = (
            "This customer currently shows a relatively low "
            "likelihood of churn."
        )


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


    st.progress(
        probability
    )


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
            Why Did the Model Make This Prediction?
        </h2>

        <p>
            SHAP values show which customer characteristics had the
            strongest influence on the model's prediction.
        </p>

    </div>
    """)


    feature_names = (
        preprocessor
        .get_feature_names_out()
    )


    feature_names = [
        name
        .replace("onehot__", "")
        .replace("num__", "")
        .replace("_", " ")
        for name in feature_names
    ]


    shap_df = pd.DataFrame({
        "Feature": feature_names,
        "SHAP Value": shap_values
    })


    shap_df["Impact"] = (
        shap_df["SHAP Value"]
        .abs()
    )


    shap_df = (
        shap_df
        .sort_values(
            "Impact",
            ascending=False
        )
        .head(10)
    )


    fig = px.bar(
        shap_df.sort_values(
            "SHAP Value"
        ),
        x="SHAP Value",
        y="Feature",
        orientation="h",
        title="Top Factors Influencing This Prediction"
    )


    fig.add_vline(
        x=0,
        line_width=1
    )


    fig.update_layout(
        height=500,
        xaxis_title="SHAP Impact",
        yaxis_title="Feature",
        showlegend=False
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.divider()


    st.html("""
    <div class="section-heading">

        <div class="section-badge">
            CHURN DRIVERS
        </div>

        <h2>
            Key Factors Behind the Prediction
        </h2>

    </div>
    """)


    positive = (
        shap_df[
            shap_df["SHAP Value"] > 0
        ]
        .sort_values(
            "SHAP Value",
            ascending=False
        )
    )


    negative = (
        shap_df[
            shap_df["SHAP Value"] < 0
        ]
        .sort_values(
            "SHAP Value"
        )
    )


    col1, col2 = st.columns(2)


    with col1:

        st.subheader(
            "⚠️ Increasing Churn Risk"
        )

        if not positive.empty:

            for _, row in positive.head(5).iterrows():

                st.markdown(
                    f"**{row['Feature']}**  \n"
                    f"SHAP impact: `{row['SHAP Value']:.3f}`"
                )

        else:

            st.write(
                "No major factors increasing churn risk."
            )


    with col2:

        st.subheader(
            "🛡️ Reducing Churn Risk"
        )

        if not negative.empty:

            for _, row in negative.head(5).iterrows():

                st.markdown(
                    f"**{row['Feature']}**  \n"
                    f"SHAP impact: `{row['SHAP Value']:.3f}`"
                )

        else:

            st.write(
                "No major factors reducing churn risk."
            )


    st.divider()


    st.caption(
        "Prediction powered by machine learning and "
        "Explainable AI (SHAP)."
    )