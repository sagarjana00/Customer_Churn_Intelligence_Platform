import streamlit as st

from utils.data_loader import load_model_comparison
from utils.visualization import plot_model_comparison


st.set_page_config(
    page_title="Model Comparision",
    page_icon="🤖",
    layout="wide"
)


comparison_df = load_model_comparison()


st.html("""
<div class="section-heading" style="text-align:left; margin-left:0;">

    <div class="section-badge">
        MACHINE LEARNING INTELLIGENCE
    </div>

    <h1>
        Model Intelligence
    </h1>

    <p>
        Compare trained machine learning models across multiple evaluation
        metrics and identify the model best suited for customer churn prediction.
    </p>

</div>
""")


st.divider()


best_model = comparison_df.loc[
    comparison_df["ROC-AUC"].idxmax()
]


best_accuracy = comparison_df["Accuracy"].max()
best_precision = comparison_df["Precision"].max()
best_recall = comparison_df["Recall"].max()
best_f1 = comparison_df["F1 Score"].max()
best_roc_auc = comparison_df["ROC-AUC"].max()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        PERFORMANCE OVERVIEW
    </div>

    <h2>
        Model Performance at a Glance
    </h2>

</div>
""")


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Models Evaluated",
        len(comparison_df)
    )


with col2:
    st.metric(
        "Best Accuracy",
        f"{best_accuracy:.4f}"
    )


with col3:
    st.metric(
        "Best F1 Score",
        f"{best_f1:.4f}"
    )


with col4:
    st.metric(
        "Best ROC-AUC",
        f"{best_roc_auc:.4f}"
    )


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        MODEL RANKING
    </div>

    <h2>
        Performance Summary
    </h2>

    <p>
        Review the evaluation results of every trained machine learning model.
    </p>

</div>
""")


display_df = comparison_df.copy()

display_df.insert(
    0,
    "Rank",
    display_df["ROC-AUC"]
    .rank(
        ascending=False,
        method="min"
    )
    .astype(int)
)


display_df = display_df.sort_values(
    "Rank"
)


st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        METRIC ANALYSIS
    </div>

    <h2>
        Compare Models
    </h2>

    <p>
        Select an evaluation metric to compare model performance visually.
    </p>

</div>
""")


metric = st.selectbox(
    "Evaluation Metric",
    [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC-AUC"
    ]
)


st.plotly_chart(
    plot_model_comparison(
        comparison_df,
        metric
    ),
    use_container_width=True
)


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        MODEL SELECTION
    </div>

    <h2>
        🏆 Best Performing Model
    </h2>

    <p>
        The model with the highest ROC-AUC is selected as the primary
        candidate for churn prediction.
    </p>

</div>
""")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Selected Model",
        best_model["Model"]
    )


with col2:

    st.metric(
        "ROC-AUC",
        f"{best_model['ROC-AUC']:.4f}"
    )


with col3:

    st.metric(
        "F1 Score",
        f"{best_model['F1 Score']:.4f}"
    )


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        BUSINESS INTERPRETATION
    </div>

    <h2>
        What Does This Mean?
    </h2>

</div>
""")


st.info(
    f"""
**Model Selection Insight**

Based on ROC-AUC, **{best_model['Model']}** achieved the strongest
overall performance with a score of **{best_model['ROC-AUC']:.4f}**.

This model is therefore selected as the primary model for the
customer churn prediction workflow.
"""
)


st.divider()


st.caption(
    "Model Comparison • "
    "Scikit-learn • XGBoost • Customer Churn Intelligence Platform"
)