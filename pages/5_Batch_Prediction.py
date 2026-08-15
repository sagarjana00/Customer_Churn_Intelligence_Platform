import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import (
    load_best_model,
    load_preprocessor
)

st.set_page_config(
    page_title="Batch Prediction",
    page_icon="📋",
    layout="wide"
)

st.title("Batch Customer Prediction")

st.markdown(
    """
    Upload a customer CSV file to predict churn probability for multiple customers.
    """
)

st.divider()

model = load_best_model()
preprocessor = load_preprocessor()

uploaded_file = st.file_uploader(
    "Upload Customer CSV",
    type=["csv"]
)

if uploaded_file:

    batch_df = pd.read_csv(uploaded_file)

    required_features = list(preprocessor.feature_names_in_)

    missing_features = [
        feature for feature in required_features
        if feature not in batch_df.columns
    ]

    if missing_features:
        st.error("The uploaded file is missing required features.")

        st.write("Missing features:")

        for feature in missing_features:
            st.write(f"- {feature}")

        st.stop()

    st.success("File uploaded successfully.")

    st.subheader("Dataset Preview")

    st.dataframe(
        batch_df.head(10),
        use_container_width=True,
        hide_index=True
    )

    st.write(
        f"Rows: {len(batch_df):,} | Columns: {len(batch_df.columns)}"
    )

    st.divider()

    if st.button("Predict Churn", use_container_width=True):

        prediction_input = batch_df[required_features].copy()

        prediction_input["TotalCharges"] = pd.to_numeric(
            prediction_input["TotalCharges"],
            errors="coerce"
        )

        prediction_input["TotalCharges"] = prediction_input["TotalCharges"].fillna(
            prediction_input["TotalCharges"].median()
        )

        processed_data = preprocessor.transform(prediction_input)

        predictions = model.predict(processed_data)

        probabilities = model.predict_proba(processed_data)[:, 1]

        st.divider()

        high_risk = (probabilities >= 0.50).sum()
        average_probability = probabilities.mean()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Customers Analyzed",
                f"{len(batch_df):,}"
            )

        with col2:
            st.metric(
                "High-Risk Customers",
                f"{high_risk:,}"
            )

        with col3:
            st.metric(
                "Average Churn Probability",
                f"{average_probability:.2%}"
            )
        
        result_df = batch_df.copy()

        result_df["Churn Prediction"] = predictions
        result_df["Churn Probability"] = probabilities

        result_df["Churn Prediction"] = result_df["Churn Prediction"].map({
            0: "No",
            1: "Yes"
        })

        st.subheader("Prediction Results")

        st.dataframe(
            result_df,
            use_container_width=True,
            hide_index=True
        )

        csv = result_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Prediction Results",
            data=csv,
            file_name="customer_churn_predictions.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.divider()

        st.subheader("High-Risk Customers")

        high_risk_df = result_df[
            result_df["Churn Probability"] >= 0.50
        ].sort_values(
            "Churn Probability",
            ascending=False
        )

        st.dataframe(
            high_risk_df,
            use_container_width=True,
            hide_index=True
        )


        st.divider()

        st.subheader("Churn Risk Distribution")

        risk_df = pd.DataFrame({
            "Risk": ["Low Risk", "Medium Risk", "High Risk"],
            "Customers": [
                (probabilities < 0.30).sum(),
                ((probabilities >= 0.30) & (probabilities < 0.50)).sum(),
                (probabilities >= 0.50).sum()
            ]
        })

        fig = px.bar(
            risk_df,
            x="Risk",
            y="Customers",
            title="Customer Churn Risk Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )