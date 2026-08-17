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


pages = [
    st.Page(
        "pages/Home_Page.py",
        title="Home",
        icon="🏠",
        default=True
    ),

    st.Page(
        "pages/1_Dataset_Explorer.py",
        title="Dataset Explorer",
        icon="📂"
    ),

    st.Page(
        "pages/2_Interactive_EDA.py",
        title="Analytics",
        icon="📊"
    ),

    st.Page(
        "pages/3_Model_Comparison.py",
        title="Model Intelligence",
        icon="🤖"
    ),

    st.Page(
        "pages/4_Customer_Prediction.py",
        title="Prediction",
        icon="🎯"
    ),

    st.Page(
        "pages/5_Batch_Prediction.py",
        title="Batch Prediction",
        icon="📁"
    ),
]


pg = st.navigation(pages)

pg.run()