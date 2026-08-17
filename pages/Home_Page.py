import streamlit as st


col1, col2 = st.columns(
    [1.05, 0.95],
    gap="large"
)

with col1:
    st.html("""
    <div class="hero-content">

        <div class="hero-badge">
            🤖 AI POWERED CUSTOMER INTELLIGENCE
        </div>

        <h1 class="hero-title">
            Customer Churn<br>
            Intelligence Platform
        </h1>

        <p class="hero-description">
            An advanced machine learning platform that predicts
            customer churn, explains model decisions, and helps
            businesses take proactive retention actions.
        </p>

        <p class="hero-description">
            Predict • Explain • Analyze • Retain
        </p>

    </div>
    """)

with col2:
    st.image(
        "assets/images/churn_hero.png",
        use_container_width=True
    )


col1, col2 = st.columns(2)

with col1:
    if st.button(
        "🎯 Make Prediction",
        use_container_width=True
    ):
        st.switch_page("pages/4_Customer_Prediction.py")

with col2:
    if st.button(
        "📊 Explore Analytics",
        use_container_width=True
    ):
        st.switch_page("pages/2_Interactive_EDA.py")


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        PLATFORM CAPABILITIES
    </div>

    <h2>
        Everything You Need to Understand Customer Churn
    </h2>

    <p>
        From prediction to explainability, the platform combines
        machine learning and business intelligence in one place.
    </p>

</div>

<div class="feature-grid">

    <div class="feature-card">

        <div class="feature-icon">🤖</div>

        <div class="feature-title">
            Machine Learning
        </div>

        <div class="feature-text">
            Evaluate and optimize multiple machine learning models
            to identify the strongest churn predictor.
        </div>

    </div>

    <div class="feature-card">

        <div class="feature-icon">🧠</div>

        <div class="feature-title">
            Explainable AI
        </div>

        <div class="feature-text">
            Understand why a customer is predicted to churn using
            SHAP-based model explanations.
        </div>

    </div>

    <div class="feature-card">

        <div class="feature-icon">📊</div>

        <div class="feature-title">
            Advanced Analytics
        </div>

        <div class="feature-text">
            Explore customer behavior, churn patterns and
            important business trends through interactive analytics.
        </div>

    </div>

    <div class="feature-card">

        <div class="feature-icon">👥</div>

        <div class="feature-title">
            Customer Intelligence
        </div>

        <div class="feature-text">
            Analyze customer characteristics and discover patterns
            associated with customer churn.
        </div>

    </div>

    <div class="feature-card">

        <div class="feature-icon">📁</div>

        <div class="feature-title">
            Batch Prediction
        </div>

        <div class="feature-text">
            Upload customer data and generate predictions for
            multiple customers in a single operation.
        </div>

    </div>

    <div class="feature-card">

        <div class="feature-icon">📈</div>

        <div class="feature-title">
            Risk Analysis
        </div>

        <div class="feature-text">
            Identify high-risk customers and prioritize them
            for proactive retention strategies.
        </div>

    </div>

</div>
""")


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        BUSINESS INTELLIGENCE
    </div>

    <h2>
        Churn at a Glance
    </h2>

    <p>
        Key metrics from the customer churn dataset and
        machine learning evaluation.
    </p>

</div>
""")


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Customers",
        "7,032"
    )

with col2:
    st.metric(
        "Churn Rate",
        "26.5%"
    )

with col3:
    st.metric(
        "Best Model",
        "XGBoost"
    )

with col4:
    st.metric(
        "ROC-AUC",
        "0.8346"
    )


st.divider()


st.html("""
<div class="section-heading">

    <div class="section-badge">
        MACHINE LEARNING PIPELINE
    </div>

    <h2>
        From Data to Decision
    </h2>

    <p>
        The platform follows a complete machine learning workflow
        from data preparation to customer prediction.
    </p>

</div>
""")


workflow = [
    "Data Preparation",
    "Exploratory Analysis",
    "Feature Engineering",
    "Model Training",
    "Hyperparameter Tuning",
    "Model Evaluation",
    "Explainable AI",
    "Prediction",
]

cols = st.columns(len(workflow))

for col, step in zip(cols, workflow):
    with col:
        st.markdown(
            f"**{step}**"
        )


st.divider()


st.caption(
    "Customer Churn Intelligence Platform • "
    "Python • Scikit-learn • XGBoost • SHAP • Streamlit"
)