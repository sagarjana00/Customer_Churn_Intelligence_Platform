import streamlit as st

from utils.data_loader import load_model_comparison

from utils.visualization import plot_model_comparison

st.set_page_config(
    page_title="Model Comparison",
    page_icon="⚖️",
    layout="wide"
)

comparison_df = load_model_comparison()

st.title("⚖️ Model Comparison")

st.markdown("""
Compare the performance of all trained machine learning models across different evaluation metrics.
""")

st.divider()


st.subheader("Performance Summary")

st.dataframe(
    comparison_df,
    use_container_width=True,
    hide_index=True
)



st.divider()

metric = st.selectbox(
    "Select Evaluation Metric",
    [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC-AUC"
    ]
)



st.plotly_chart(
    plot_model_comparison(comparison_df, metric),
    use_container_width=True
)



st.divider()

best_model = comparison_df.loc[
    comparison_df["ROC-AUC"].idxmax()
]

st.subheader("🏆 Best Performing Model")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Model",
        best_model["Model"]
    )

with col2:
    st.metric(
        "ROC-AUC",
        f"{best_model['ROC-AUC']:.4f}"
    )





st.info(
    f"""
**Business Insight**

Based on ROC-AUC, **{best_model['Model']}** achieved the best overall performance
with a score of **{best_model['ROC-AUC']:.4f}** and is selected as the final model.
"""
)