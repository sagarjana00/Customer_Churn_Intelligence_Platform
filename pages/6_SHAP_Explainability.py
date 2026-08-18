import streamlit as st
import pandas as pd
import shap
import plotly.express as px

from utils.data_loader import (
    load_best_model,
    load_preprocessor
)


st.set_page_config(
    page_title="SHAP Explainability",
    page_icon="🧠",
    layout="wide"
)


if "prediction_input" not in st.session_state:

    st.warning(
        "No customer prediction is available to explain."
    )

    st.info(
        "Please make a prediction first from the Customer Prediction page."
    )

    if st.button(
        "🎯 Go to Customer Prediction",
        use_container_width=True
    ):
        st.switch_page(
            "pages/4_Customer_Prediction.py"
        )

    st.stop()


input_df = st.session_state["prediction_input"]
prediction = st.session_state["prediction_result"]
probability = float(
    st.session_state["prediction_probability"]
)


model = load_best_model()
preprocessor = load_preprocessor()

explainer = shap.TreeExplainer(model)


st.html("""
<div class="section-heading" style="padding-top:30px;">

    <div class="section-badge">
        EXPLAINABLE AI
    </div>

    <h1>
        SHAP Explainability
    </h1>

    <p>
        Understand why the machine learning model made this
        customer churn prediction.
    </p>

</div>
""")


st.divider()


if prediction == 1:
    prediction_text = "⚠️ Customer Likely to Churn"
else:
    prediction_text = "✅ Customer Likely to Stay"


if probability >= 0.75:
    risk_level = "High Risk"
elif probability >= 0.50:
    risk_level = "Medium Risk"
else:
    risk_level = "Low Risk"


st.html("""
<div class="section-heading">

    <div class="section-badge">
        PREDICTION SUMMARY
    </div>

    <h2>
        Previous Customer Prediction
    </h2>

    <p>
        This explanation is based on the customer profile
        submitted on the Customer Prediction page.
    </p>

</div>
""")


col1, col2, col3 = st.columns(3)


with col1:

    if prediction == 1:
        st.error(prediction_text)
    else:
        st.success(prediction_text)


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



st.divider()


processed_input = preprocessor.transform(
    input_df
)


shap_values = explainer.shap_values(
    processed_input
)


if isinstance(shap_values, list):
    shap_values = shap_values[-1]


shap_values = shap_values[0]


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


st.html("""
<div class="section-heading">

    <div class="section-badge">
        SHAP ANALYSIS
    </div>

    <h2>
        Why Did the Model Make This Prediction?
    </h2>

    <p>
        SHAP values show how individual features influenced
        the model's prediction for this customer.
    </p>

</div>
""")


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

        st.success(
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

        st.info(
            "No major factors reducing churn risk."
        )


st.divider()


if st.button(
    "🎯 Make Another Prediction",
    use_container_width=True
):

    st.switch_page(
        "pages/4_Customer_Prediction.py"
    )


st.caption(
    "SHAP Explainability • "
    "Machine Learning • "
    "Customer Churn Intelligence Platform"
)