import streamlit as st

from utils.style import load_css


st.set_page_config(
    page_title="Customer Churn Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_css()


st.sidebar.markdown("""
# 📊 Customer Churn

**Intelligence Platform**

End-to-End Machine Learning
Dashboard
""")

st.sidebar.divider()


home_page = st.Page(
    "pages/Home_Page.py",
    title="Home",
    icon="🏠",
    default=True
)

dataset_page = st.Page(
    "pages/1_Dataset_Explorer.py",
    title="Dataset Explorer",
    icon="📂"
)

analytics_page = st.Page(
    "pages/2_Interactive_EDA.py",
    title="Analytics",
    icon="📊"
)

model_page = st.Page(
    "pages/3_Model_Comparison.py",
    title="Model Intelligence",
    icon="🤖"
)

prediction_page = st.Page(
    "pages/4_Customer_Prediction.py",
    title="Prediction",
    icon="🎯"
)

shap_page = st.Page(
    "pages/6_SHAP_Explainability.py",
    title="SHAP Explainability",
    icon="🧠"
)

batch_page = st.Page(
    "pages/5_Batch_Prediction.py",
    title="Batch Prediction",
    icon="📁"
)


pages = [
    home_page,
    dataset_page,
    analytics_page,
    model_page,
    prediction_page,
    shap_page,
    batch_page,
]


pg = st.navigation(pages)

pg.run()