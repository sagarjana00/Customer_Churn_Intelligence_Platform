import streamlit as st
import pandas as pd

from utils.data_loader import load_dataset
from utils.visualization import (
    plot_histogram,
    plot_boxplot,
    plot_histogram_by_churn
)
from utils.helpers import get_business_insight

st.set_page_config(
    page_title="Interactive EDA",
    page_icon="📈",
    layout="wide"
)

df = load_dataset()

st.title("📈 Interactive Exploratory Data Analysis")

st.markdown("""
Explore feature distributions and their relationship with customer churn.
""")

st.divider()



features = df.columns.drop("Churn").tolist()

selected_feature = st.selectbox(
    "Select a Feature",
    features
)
is_numeric = pd.api.types.is_numeric_dtype(df[selected_feature])


st.subheader("Feature Statistics")

if is_numeric:

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Mean", round(df[selected_feature].mean(), 2))

    with col2:
        st.metric("Median", round(df[selected_feature].median(), 2))

    with col3:
        st.metric("Minimum", round(df[selected_feature].min(), 2))

    with col4:
        st.metric("Maximum", round(df[selected_feature].max(), 2))

else:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Unique Values", df[selected_feature].nunique())

    with col2:
        st.metric(
            "Most Frequent",
            df[selected_feature].mode()[0]
        )

    with col3:
        st.metric(
            "Missing Values",
            df[selected_feature].isnull().sum()
        )



st.divider()

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        plot_histogram(df, selected_feature),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        plot_boxplot(df, selected_feature),
        use_container_width=True
    )




st.divider()

st.subheader("Relationship with Churn")

st.plotly_chart(
    plot_histogram_by_churn(df, selected_feature),
    use_container_width=True
)



st.divider()

st.info(
    f"**Business Insight:** {get_business_insight(selected_feature)}"
)