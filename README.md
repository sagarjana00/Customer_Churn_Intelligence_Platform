# 📊 Customer Churn Intelligence Platform

An end-to-end machine learning platform for **customer churn prediction, explainable AI, customer risk assessment, and business intelligence**.

The project takes the complete machine learning workflow from data understanding and exploratory analysis to feature engineering, model training, hyperparameter tuning, model comparison, explainability, and deployment as an interactive Streamlit application.

## 🚀 Live Application

🔗 **[Customer Churn Intelligence Platform](https://customerchurnintelligenceplatform.streamlit.app/)**

The deployed application allows users to:

- Explore the customer churn dataset
- Perform interactive exploratory data analysis
- Compare machine learning models
- Predict churn for individual customers
- Analyze prediction explanations using SHAP
- Perform batch churn prediction using CSV files
- Identify high-risk customers
- Download batch prediction results

---

# 🎯 Project Overview

Customer churn is a major business problem where customers discontinue their services or subscriptions.

The goal of this project is to build an intelligent system that can:

1. Understand customer behavior
2. Identify patterns associated with churn
3. Train multiple machine learning models
4. Optimize model performance
5. Predict the probability of customer churn
6. Classify customers according to risk
7. Explain individual predictions using SHAP
8. Support batch prediction for multiple customers
9. Provide an interactive business-oriented dashboard

Instead of building only a machine learning model, this project focuses on creating a **complete end-to-end ML application**.

---

# ✨ Key Features

## 📂 Dataset Explorer

Explore the customer churn dataset through an interactive interface.

Features include:

- Dataset dimensions
- Data preview
- Feature information
- Numerical and categorical feature analysis
- Missing-value analysis
- Dataset statistics

---

## 📊 Interactive EDA

The platform provides interactive analytics for understanding customer behavior.

Analysis includes:

- Churn distribution
- Categorical feature analysis
- Numerical feature distributions
- Customer tenure analysis
- Monthly charges analysis
- Total charges analysis
- Contract-based churn analysis
- Internet service analysis
- Payment method analysis
- Customer demographic patterns

Interactive visualizations are built using Plotly and other Python visualization libraries.

---

## 🤖 Model Intelligence

Multiple machine learning algorithms were trained and evaluated.

The project includes:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

Both baseline and hyperparameter-tuned versions were evaluated.

---

## 🎯 Individual Customer Prediction

Users can enter customer information through the web interface and receive:

- Churn prediction
- Churn probability
- Customer risk level
- Retention recommendation

Risk levels are categorized into:

- 🟢 Low Risk
- 🟠 Medium Risk
- 🔴 High Risk

---

## 🧠 Explainable AI with SHAP

The platform uses **SHAP (SHapley Additive exPlanations)** to explain individual machine learning predictions.

The explainability interface shows:

- Features influencing the prediction
- Positive impact on churn risk
- Negative impact on churn risk
- SHAP impact values
- Top factors influencing the prediction

This makes the model more interpretable and helps users understand **why a customer was predicted to churn**.

---

## 📁 Batch Prediction

Users can upload a customer CSV file and generate predictions for multiple customers at once.

The batch prediction system provides:

- Number of customers analyzed
- Churn predictions
- Churn probabilities
- Risk levels
- High-risk customer identification
- Risk distribution visualization
- Prediction results table
- CSV download functionality

---

# 🧠 Machine Learning Workflow

The project follows a complete machine learning pipeline:

```text
Business & Data Understanding
            ↓
Exploratory Data Analysis
            ↓
Feature Engineering
            ↓
Data Preprocessing
            ↓
Baseline Model Training
            ↓
Model Evaluation
            ↓
Hyperparameter Tuning
            ↓
Final Model Comparison
            ↓
Model Selection
            ↓
SHAP Explainability
            ↓
Customer Prediction
            ↓
Batch Prediction
            ↓
Streamlit Deployment