import streamlit as st
import pandas as pd

from utils.data_loader import load_dataset


st.set_page_config(
    page_title="Dataset Explorer",
    page_icon="📂",
    layout="wide"
)


df = load_dataset()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        DATASET INTELLIGENCE
    </div>

    <h2>
        Explore the Customer Churn Dataset
    </h2>

    <p>
        Understand the structure, quality and key characteristics
        of the customer dataset before applying machine learning.
    </p>

</div>
""")


rows, columns = df.shape

missing = df.isnull().sum().sum()

categorical = len(
    df.select_dtypes(include="object").columns
)

numerical = len(
    df.select_dtypes(exclude="object").columns
)


st.subheader("Dataset Overview")


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Customers",
        f"{rows:,}"
    )


with col2:
    st.metric(
        "Features",
        columns
    )


with col3:
    st.metric(
        "Missing Values",
        f"{missing:,}"
    )


with col4:
    st.metric(
        "Categorical Features",
        categorical
    )


st.divider()


st.subheader("Dataset Preview")


rows_to_show = st.slider(
    "Rows to display",
    min_value=5,
    max_value=min(100, rows),
    value=min(10, rows),
    step=5
)


st.dataframe(
    df.head(rows_to_show),
    use_container_width=True,
    hide_index=True
)


st.divider()


st.subheader("Feature Information")


info_df = pd.DataFrame({
    "Feature": df.columns,
    "Data Type": df.dtypes.astype(str).values,
    "Missing Values": df.isnull().sum().values,
    "Unique Values": df.nunique().values
})


st.dataframe(
    info_df,
    use_container_width=True,
    hide_index=True
)


st.divider()


col1, col2 = st.columns(2)


with col1:

    st.subheader("Feature Types")

    feature_types = pd.DataFrame({
        "Type": [
            "Numerical",
            "Categorical"
        ],
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


with col2:

    st.subheader("Missing Values")

    missing_df = pd.DataFrame({
        "Feature": df.columns,
        "Missing Values": df.isnull().sum().values
    })

    missing_df = missing_df[
        missing_df["Missing Values"] > 0
    ]

    if missing_df.empty:

        st.success(
            "No missing values found in the dataset."
        )

    else:

        st.dataframe(
            missing_df,
            use_container_width=True,
            hide_index=True
        )


st.divider()


st.subheader("Target Variable Distribution")


target_counts = df["Churn"].value_counts()


col1, col2 = st.columns(2)


with col1:

    st.metric(
        "Customers Staying",
        f"{target_counts.get('No', 0):,}"
    )


with col2:

    st.metric(
        "Customers Churning",
        f"{target_counts.get('Yes', 0):,}"
    )


if "Churn" in df.columns:

    churn_rate = (
        df["Churn"]
        .value_counts(normalize=True)
        .get("Yes", 0)
        * 100
    )

    st.progress(
        float(churn_rate / 100)
    )

    st.caption(
        f"Overall churn rate: {churn_rate:.2f}%"
    )


st.divider()


with st.expander(
    "📊 Statistical Summary",
    expanded=False
):

    st.dataframe(
        df.describe().T,
        use_container_width=True
    )


st.divider()


st.subheader("Download Dataset")


csv = df.to_csv(
    index=False
).encode("utf-8")


st.download_button(
    label="📥 Download Dataset",
    data=csv,
    file_name="customer_churn_dataset.csv",
    mime="text/csv",
    use_container_width=True
)


st.divider()


st.caption(
    "Customer Churn Intelligence Platform • "
    "Dataset Intelligence • Python • Pandas"
)