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
    page_icon="📊",
    layout="wide"
)


df = load_dataset()


st.html("""
<div class="section-heading" style="text-align:left; margin-left:0;">

    <div class="section-badge">
        CUSTOMER ANALYTICS
    </div>

    <h1>
        Interactive Analytics
    </h1>

    <p>
        Explore customer behavior, feature distributions and their
        relationship with churn using interactive visual analytics.
    </p>

</div>
""")


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        FEATURE ANALYSIS
    </div>

    <h2>
        Explore a Customer Feature
    </h2>

    <p>
        Select a feature to analyze its distribution and relationship
        with customer churn.
    </p>

</div>
""")


features = df.columns.drop("Churn").tolist()


selected_feature = st.selectbox(
    "Select Feature",
    features
)


is_numeric = pd.api.types.is_numeric_dtype(
    df[selected_feature]
)


st.divider()


if is_numeric:

    st.html("""
    <div class="section-heading">

        <div class="section-badge">
            NUMERICAL FEATURE
        </div>

        <h2>
            Feature Statistics
        </h2>

    </div>
    """)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Mean",
            f"{df[selected_feature].mean():.2f}"
        )

    with col2:
        st.metric(
            "Median",
            f"{df[selected_feature].median():.2f}"
        )

    with col3:
        st.metric(
            "Minimum",
            f"{df[selected_feature].min():.2f}"
        )

    with col4:
        st.metric(
            "Maximum",
            f"{df[selected_feature].max():.2f}"
        )

else:

    st.html("""
    <div class="section-heading">

        <div class="section-badge">
            CATEGORICAL FEATURE
        </div>

        <h2>
            Feature Statistics
        </h2>

    </div>
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Unique Values",
            df[selected_feature].nunique()
        )

    with col2:
        mode_value = df[selected_feature].mode()

        st.metric(
            "Most Frequent",
            mode_value.iloc[0] if not mode_value.empty else "N/A"
        )

    with col3:
        st.metric(
            "Missing Values",
            df[selected_feature].isnull().sum()
        )


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        DISTRIBUTION ANALYSIS
    </div>

    <h2>
        Feature Distribution
    </h2>

    <p>
        Understand the shape, spread and potential outliers of the
        selected customer feature.
    </p>

</div>
""")


col1, col2 = st.columns(2, gap="large")


with col1:

    st.plotly_chart(
        plot_histogram(
            df,
            selected_feature
        ),
        use_container_width=True
    )


with col2:

    st.plotly_chart(
        plot_boxplot(
            df,
            selected_feature
        ),
        use_container_width=True
    )


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        CHURN RELATIONSHIP
    </div>

    <h2>
        How Does This Feature Relate to Churn?
    </h2>

    <p>
        Compare the selected feature across customers who churned
        and customers who remained.
    </p>

</div>
""")


st.plotly_chart(
    plot_histogram_by_churn(
        df,
        selected_feature
    ),
    use_container_width=True
)


st.divider()


insight = get_business_insight(
    selected_feature
)


st.html("""
<div class="section-heading">

    <div class="section-badge">
        BUSINESS INTERPRETATION
    </div>

    <h2>
        What Does This Tell Us?
    </h2>

</div>
""")


st.info(
    f"**Business Insight:** {insight}"
)


st.divider()


st.caption(
    "Interactive Analytics • "
    "Customer Churn Intelligence Platform"
)