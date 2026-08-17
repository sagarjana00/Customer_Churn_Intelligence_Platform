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
<div class="section-heading" style="text-align:left; margin-left:0;">

    <div class="section-badge">
        DATA INTELLIGENCE
    </div>

    <h1>
        Dataset Explorer
    </h1>

    <p>
        Explore customer records, feature distributions and data quality
        before building and evaluating churn prediction models.
    </p>

</div>
""")


rows, columns = df.shape

missing = int(df.isnull().sum().sum())

categorical = len(
    df.select_dtypes(include="object").columns
)

numerical = len(
    df.select_dtypes(exclude="object").columns
)

duplicates = int(df.duplicated().sum())


st.html("""
<div class="section-heading">

    <div class="section-badge">
        DATASET OVERVIEW
    </div>

    <h2>
        Dataset at a Glance
    </h2>

</div>
""")


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
        "Duplicate Rows",
        f"{duplicates:,}"
    )


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        DATA EXPLORATION
    </div>

    <h2>
        Explore Customer Records
    </h2>

    <p>
        Filter the dataset and inspect individual customer records.
    </p>

</div>
""")


filter_col1, filter_col2, filter_col3 = st.columns(3)


filtered_df = df.copy()


with filter_col1:

    if "Churn" in df.columns:

        churn_options = ["All"] + sorted(
            df["Churn"].dropna().unique().tolist()
        )

        churn_filter = st.selectbox(
            "Churn Status",
            churn_options
        )

        if churn_filter != "All":
            filtered_df = filtered_df[
                filtered_df["Churn"] == churn_filter
            ]


with filter_col2:

    if "Contract" in df.columns:

        contract_options = ["All"] + sorted(
            df["Contract"].dropna().unique().tolist()
        )

        contract_filter = st.selectbox(
            "Contract",
            contract_options
        )

        if contract_filter != "All":
            filtered_df = filtered_df[
                filtered_df["Contract"] == contract_filter
            ]


with filter_col3:

    if "InternetService" in df.columns:

        internet_options = ["All"] + sorted(
            df["InternetService"].dropna().unique().tolist()
        )

        internet_filter = st.selectbox(
            "Internet Service",
            internet_options
        )

        if internet_filter != "All":
            filtered_df = filtered_df[
                filtered_df["InternetService"] == internet_filter
            ]


st.write(
    f"Showing **{len(filtered_df):,}** of **{len(df):,}** customers"
)


rows_to_show = st.slider(
    "Rows to display",
    min_value=5,
    max_value=100,
    value=10,
    step=5
)


st.dataframe(
    filtered_df.head(rows_to_show),
    use_container_width=True,
    hide_index=True
)


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        DATA QUALITY
    </div>

    <h2>
        Data Quality Overview
    </h2>

    <p>
        Check missing values, duplicates and feature types before modeling.
    </p>

</div>
""")


quality_col1, quality_col2, quality_col3 = st.columns(3)


with quality_col1:

    st.metric(
        "Missing Values",
        f"{missing:,}"
    )


with quality_col2:

    st.metric(
        "Duplicate Rows",
        f"{duplicates:,}"
    )


with quality_col3:

    st.metric(
        "Numerical / Categorical",
        f"{numerical} / {categorical}"
    )


st.divider()


col1, col2 = st.columns(2)


with col1:

    st.subheader("Missing Values by Feature")

    missing_df = pd.DataFrame({
        "Feature": df.columns,
        "Missing Values": df.isnull().sum().values
    })

    st.dataframe(
        missing_df,
        use_container_width=True,
        hide_index=True
    )


with col2:

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


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        CHURN DISTRIBUTION
    </div>

    <h2>
        Target Variable
    </h2>

    <p>
        Distribution of customers across churn and non-churn classes.
    </p>

</div>
""")


if "Churn" in df.columns:

    target_counts = df["Churn"].value_counts()

    col1, col2 = st.columns(2)

    with col1:

        no_churn = target_counts.get("No", 0)

        st.metric(
            "No Churn",
            f"{no_churn:,}"
        )

    with col2:

        churn = target_counts.get("Yes", 0)

        st.metric(
            "Churn",
            f"{churn:,}"
        )

    st.bar_chart(
        target_counts
    )


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        FEATURE INFORMATION
    </div>

    <h2>
        Dataset Schema
    </h2>

    <p>
        Detailed information about every feature in the dataset.
    </p>

</div>
""")


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


st.html("""
<div class="section-heading">

    <div class="section-badge">
        STATISTICAL ANALYSIS
    </div>

    <h2>
        Statistical Summary
    </h2>

    <p>
        Descriptive statistics for numerical features.
    </p>

</div>
""")


st.dataframe(
    df.describe().T,
    use_container_width=True
)


st.divider()


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