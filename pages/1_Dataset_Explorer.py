import streamlit as st
import pandas as pd

from utils.data_loader import load_dataset

st.set_page_config(
    page_title="Dataset Explorer",
    page_icon="📂",
    layout="wide"
)

df = load_dataset()

st.title("📂 Dataset Explorer")

st.markdown("""
Explore the customer churn dataset and understand its structure before building predictive models.
""")

st.divider()

rows, columns = df.shape
missing = df.isnull().sum().sum()
categorical = len(df.select_dtypes(include="object").columns)
numerical = len(df.select_dtypes(exclude="object").columns)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Rows", f"{rows:,}")

with col2:
    st.metric("Columns", columns)

with col3:
    st.metric("Missing Values", missing)

with col4:
    st.metric("Categorical Features", categorical)

st.divider()

st.subheader("Dataset Preview")

rows_to_show = st.slider(
    "Rows to display",
    min_value=5,
    max_value=100,
    value=10,
    step=5
)

st.dataframe(
    df.head(rows_to_show),
    use_container_width=True,
    hide_index=True
)

st.divider()

info_df = pd.DataFrame({
    "Feature": df.columns,
    "Data Type": df.dtypes.astype(str).values,
    "Missing Values": df.isnull().sum().values,
    "Unique Values": df.nunique().values
})

with st.expander("Dataset Information", expanded=False):
    st.dataframe(
        info_df,
        use_container_width=True,
        hide_index=True
    )


st.divider()

st.subheader("Missing Values")

missing_df = pd.DataFrame({
    "Feature": df.columns,
    "Missing Values": df.isnull().sum().values
})

st.dataframe(
    missing_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("Feature Types")

feature_types = pd.DataFrame({
    "Type": ["Numerical", "Categorical"],
    "Count": [
        numerical,
        categorical
    ]
})

st.dataframe(
    feature_types,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("Target Variable Distribution")

target_counts = df["Churn"].value_counts()

col1, col2 = st.columns(2)

with col1:
    st.metric("No Churn", target_counts["No"])

with col2:
    st.metric("Churn", target_counts["Yes"])

st.divider()

with st.expander("Statistical Summary", expanded=False):
    st.dataframe(
        df.describe().T,
        use_container_width=True
    )

st.divider()

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Dataset",
    data=csv,
    file_name="customer_churn_dataset.csv",
    mime="text/csv",
    use_container_width=True
)