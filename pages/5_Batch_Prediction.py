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


model = load_best_model()
preprocessor = load_preprocessor()


st.html("""
<div class="section-heading">
    <div class="section-badge">BATCH PREDICTION</div>

    <h2>Predict Churn for Multiple Customers</h2>

    <p>
        Upload customer data to generate churn predictions,
        probability scores and risk levels for multiple customers.
    </p>
</div>
""")


uploaded_file = st.file_uploader(
    "📁 Upload Customer CSV",
    type=["csv"]
)


if uploaded_file:

    batch_df = pd.read_csv(uploaded_file)

    required_features = list(
        preprocessor.feature_names_in_
    )

    missing_features = [
        feature
        for feature in required_features
        if feature not in batch_df.columns
    ]


    if missing_features:

        st.error(
            "The uploaded file is missing required features."
        )

        st.write("Missing features:")

        for feature in missing_features:
            st.write(f"- {feature}")

        st.stop()


    st.success("File uploaded successfully.")


    st.divider()


    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Customers",
            f"{len(batch_df):,}"
        )

    with col2:
        st.metric(
            "Columns",
            f"{len(batch_df.columns):,}"
        )

    with col3:
        st.metric(
            "Required Features",
            f"{len(required_features):,}"
        )


    st.subheader("Dataset Preview")

    st.dataframe(
        batch_df.head(10),
        use_container_width=True,
        hide_index=True
    )


    st.divider()


    if st.button(
        "🎯 Predict Churn",
        use_container_width=True
    ):

        prediction_input = batch_df[
            required_features
        ].copy()


        prediction_input["TotalCharges"] = pd.to_numeric(
            prediction_input["TotalCharges"],
            errors="coerce"
        )


        prediction_input["TotalCharges"] = (
            prediction_input["TotalCharges"]
            .fillna(
                prediction_input["TotalCharges"].median()
            )
        )


        processed_data = preprocessor.transform(
            prediction_input
        )


        predictions = model.predict(
            processed_data
        )


        probabilities = model.predict_proba(
            processed_data
        )[:, 1]


        result_df = batch_df.copy()


        result_df["Churn Prediction"] = predictions

        result_df["Churn Probability"] = probabilities


        result_df["Risk Level"] = pd.cut(
            probabilities,
            bins=[
                -float("inf"),
                0.30,
                0.50,
                float("inf")
            ],
            labels=[
                "Low Risk",
                "Medium Risk",
                "High Risk"
            ]
        )


        result_df["Churn Prediction"] = (
            result_df["Churn Prediction"]
            .map({
                0: "No",
                1: "Yes"
            })
        )


        high_risk = (
            probabilities >= 0.50
        ).sum()


        medium_risk = (
            (probabilities >= 0.30)
            & (probabilities < 0.50)
        ).sum()


        low_risk = (
            probabilities < 0.30
        ).sum()


        average_probability = (
            probabilities.mean()
        )


        st.divider()


        st.subheader("Risk Overview")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Customers Analyzed",
                f"{len(batch_df):,}"
            )

        with col2:
            st.metric(
                "🔴 High Risk",
                f"{high_risk:,}"
            )

        with col3:
            st.metric(
                "🟠 Medium Risk",
                f"{medium_risk:,}"
            )

        with col4:
            st.metric(
                "🟢 Low Risk",
                f"{low_risk:,}"
            )


        st.metric(
            "Average Churn Probability",
            f"{average_probability:.2%}"
        )


        st.progress(
            float(average_probability)
        )


        st.divider()


        st.subheader("Prediction Results")


        display_df = result_df.copy()

        display_df["Churn Probability"] = (
            display_df["Churn Probability"]
            .map(lambda x: f"{x:.2%}")
        )


        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )


        csv = result_df.to_csv(
            index=False
        ).encode("utf-8")


        st.download_button(
            label="📥 Download Prediction Results",
            data=csv,
            file_name="customer_churn_predictions.csv",
            mime="text/csv",
            use_container_width=True
        )


        st.divider()


        st.subheader("High-Risk Customers")


        high_risk_df = result_df[
            result_df["Risk Level"] == "High Risk"
        ].sort_values(
            "Churn Probability",
            ascending=False
        )


        if high_risk_df.empty:

            st.success(
                "No high-risk customers were identified."
            )

        else:

            high_risk_display = high_risk_df.copy()

            high_risk_display[
                "Churn Probability"
            ] = (
                high_risk_display[
                    "Churn Probability"
                ].map(
                    lambda x: f"{x:.2%}"
                )
            )


            st.dataframe(
                high_risk_display,
                use_container_width=True,
                hide_index=True
            )


        st.divider()


        st.subheader("Churn Risk Distribution")


        risk_df = pd.DataFrame({
            "Risk": [
                "Low Risk",
                "Medium Risk",
                "High Risk"
            ],
            "Customers": [
                low_risk,
                medium_risk,
                high_risk
            ]
        })


        fig = px.bar(
            risk_df,
            x="Risk",
            y="Customers",
            text="Customers",
            title="Customer Churn Risk Distribution"
        )


        fig.update_layout(
            height=400,
            showlegend=False
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )