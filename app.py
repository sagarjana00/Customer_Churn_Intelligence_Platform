import streamlit as st

st.set_page_config(
    page_title="Customer Churn Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("Customer Churn")

st.sidebar.markdown("""
**Customer Churn Intelligence Platform**

End-to-End Machine Learning Dashboard
""")

st.title("📊 Customer Churn Intelligence Platform")

st.markdown("""
### Predict • Explain • Analyze • Retain

An end-to-end machine learning platform that predicts customer churn,
explains model decisions using SHAP, compares multiple machine learning models,
and provides actionable business insights through an interactive dashboard.
""")

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Customers", "7,032")

with col2:
    st.metric("Churn Rate", "26.5%")

with col3:
    st.metric("Best Model", "XGBoost")

with col4:
    st.metric("ROC-AUC", "0.8346")

st.divider()

st.header("Project Overview")

st.write("""
Customer churn is one of the biggest challenges faced by subscription-based businesses.
This platform leverages machine learning to identify customers at risk of leaving,
helping organizations take proactive retention actions.

The application combines predictive analytics, model comparison, Explainable AI (SHAP),
and interactive visualizations into a unified business intelligence platform.
""")

st.divider()

st.header("Technology Stack")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Data")
    st.markdown("""
- Pandas
- NumPy
""")

with col2:
    st.subheader("Machine Learning")
    st.markdown("""
- Scikit-learn
- XGBoost
""")

with col3:
    st.subheader("Explainability")
    st.markdown("""
- SHAP
""")

with col4:
    st.subheader("Application")
    st.markdown("""
- Streamlit
- Plotly
- Joblib
""")

st.divider()

st.header("Project Workflow")

workflow = [
    "Data Cleaning",
    "EDA",
    "Feature Engineering",
    "Model Training",
    "Hyperparameter Tuning",
    "Model Comparison",
    "Explainable AI",
    "Prediction",
]

cols = st.columns(len(workflow))

for col, step in zip(cols, workflow):
    with col:
        st.markdown(f"**{step}**")

st.divider()

st.header("Platform Features")

left, right = st.columns(2)

with left:
    st.markdown("""
- Interactive Dataset Explorer
- Exploratory Data Analysis
- Customer Churn Prediction
- Batch Prediction
""")

with right:
    st.markdown("""
- Model Comparison
- Explainable AI (SHAP)
- Business Insights
- Export Predictions
""")

st.divider()

st.header("Project Highlights")

left, right = st.columns(2)

with left:
    st.markdown("""
- Evaluated 8 machine learning models
- Hyperparameter tuning using GridSearchCV
- Explainable AI with SHAP
""")

with right:
    st.markdown("""
- Interactive business dashboard
- Batch prediction support
- Actionable business insights
""")

st.divider()

st.caption("Developed by Sagar Jana | DATA lover")

st.caption("Python • Scikit-learn • XGBoost • SHAP • Streamlit")