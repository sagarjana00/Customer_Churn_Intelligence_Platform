# ⚙️ Customer Churn Intelligence Platform — Setup Guide

This guide explains how to set up, run, test, and deploy the **Customer Churn Intelligence Platform** locally.

---

## 📋 Prerequisites

Before setting up the project, make sure the following are installed:

- Python 3.10 or later
- Git
- pip
- VS Code or another code editor
- Jupyter Notebook or JupyterLab

Verify the installations:

```bash
python --version
git --version
pip --version
```

---

## 📥 1. Clone the Repository

```bash
git clone https://github.com/sagarjana00/Customer_Churn_Intelligence_Platform.git
cd Customer_Churn_Intelligence_Platform
```

---

## 🐍 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activation, your terminal should show something similar to:

```text
(.venv)
```

---

## 📦 3. Install Dependencies

Make sure the virtual environment is activated.

```bash
pip install -r requirements.txt
```

The requirements file contains the libraries needed for the machine learning workflow and Streamlit application, including NumPy, Pandas, Scikit-learn, XGBoost, SHAP, Matplotlib, Seaborn, Plotly, Streamlit, Jupyter, and supporting packages.

---

## 📁 4. Project Structure

```text
Customer_Churn_Intelligence_Platform/
│
├── app.py
├── requirements.txt
├── README.md
├── SETUP.md
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── *.ipynb
│
├── models/
│
├── pages/
│   ├── Home_Page.py
│   ├── 1_Dataset_Explorer.py
│   ├── 2_Interactive_EDA.py
│   ├── 3_Model_Comparison.py
│   ├── 4_Customer_Prediction.py
│   ├── 5_Batch_Prediction.py
│   └── 6_SHAP_Explainability.py
│
├── utils/
│   ├── data_loader.py
│   ├── paths.py
│   ├── prediction.py
│   └── style.py
│
├── assets/
│   ├── images/
│   ├── icons/
│   └── styles/
│
├── results/
└── reports/
```

---

## 📊 5. Dataset Setup

The project uses a customer churn dataset containing customer demographic, service, contract, and billing information.

The expected customer features include:

```text
gender
SeniorCitizen
Partner
Dependents
tenure
PhoneService
MultipleLines
InternetService
OnlineSecurity
OnlineBackup
DeviceProtection
TechSupport
StreamingTV
StreamingMovies
Contract
PaperlessBilling
PaymentMethod
MonthlyCharges
TotalCharges
```

The target variable is:

```text
Churn
```

Place the raw dataset inside:

```text
data/raw/
```

Processed datasets can be stored inside:

```text
data/processed/
```

The paths used by the application are defined in:

```text
utils/paths.py
```

---

## 🧹 6. Data Preparation

The notebooks contain the data preparation and machine learning workflow.

The general workflow is:

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Missing Value Handling
     ↓
Data Type Correction
     ↓
Feature Engineering
     ↓
Categorical Encoding
     ↓
Numerical Processing
     ↓
Train/Test Split
     ↓
Model Training
```

The preprocessing pipeline used by the application should remain consistent with the preprocessing used during model training.

---

## 📓 7. Running the Jupyter Notebooks

The `notebooks/` directory contains the main machine learning workflow and is an important part of the project.

Start Jupyter Notebook:

```bash
jupyter notebook
```

or JupyterLab:

```bash
jupyter lab
```

Open the notebooks from:

```text
notebooks/
```

Run the notebooks in their intended workflow order.

The notebooks cover areas such as:

- Data understanding
- Exploratory data analysis
- Feature engineering
- Data preprocessing
- Baseline model training
- Model evaluation
- Hyperparameter tuning
- Model comparison
- SHAP analysis

---

## 🤖 8. Model Files

Trained models and preprocessing objects used by the Streamlit application are stored in:

```text
models/
```

The application loads these objects through:

```text
utils/data_loader.py
```

If models are regenerated, make sure the files expected by `utils/data_loader.py` are available in the `models/` directory.

The model and preprocessing pipeline must remain compatible with each other.

---

## 🌐 9. Run the Streamlit Application Locally

After installing dependencies:

```bash
streamlit run app.py
```

Streamlit will provide a local URL similar to:

```text
http://localhost:8501
```

Open the URL in your browser.

---

## 🖥️ 10. Application Navigation

### 🏠 Home

Provides an overview of the Customer Churn Intelligence Platform.

### 📂 Dataset Explorer

Allows users to inspect the customer churn dataset.

### 📊 Analytics

Provides interactive exploratory data analysis and customer behavior insights.

### 🤖 Model Intelligence

Provides model comparison and machine learning evaluation.

### 🎯 Prediction

Allows users to enter information for an individual customer and obtain:

- Churn prediction
- Churn probability
- Risk level
- Retention recommendation

### 🧠 SHAP Explainability

Explains the factors influencing an individual customer's prediction using SHAP.

### 📁 Batch Prediction

Allows users to upload a CSV containing multiple customers and generate:

- Churn predictions
- Churn probabilities
- Risk levels
- High-risk customer identification
- Downloadable prediction results

---

## 🎯 11. Individual Customer Prediction

Navigate to:

```text
Prediction
```

Enter the customer's information and click:

```text
🎯 Predict Customer Churn
```

The application generates:

```text
Customer Information
        ↓
Prediction
        ↓
Churn Probability
        ↓
Risk Level
        ↓
Retention Recommendation
```

After a prediction is generated, the customer input and prediction result are stored in Streamlit session state.

This allows the corresponding SHAP explanation to use the same prediction.

---

## 🧠 12. SHAP Explainability

After generating an individual prediction, click:

```text
🧠 Why This Prediction?
```

The application opens the SHAP explainability page.

The page explains which customer features contributed most strongly to the prediction.

The explanation separates factors into:

```text
Factors Increasing Churn Risk
```

and:

```text
Factors Reducing Churn Risk
```

SHAP impact values are used to provide an interpretable explanation of the model output.

A prediction should be generated before opening the SHAP explanation page.

---

## 📁 13. Batch Prediction

Navigate to:

```text
Batch Prediction
```

Upload a CSV containing the required customer features.

The application validates the uploaded dataset before generating predictions.

The output includes:

- Number of customers analyzed
- Churn predictions
- Churn probabilities
- Risk levels
- High-risk customer identification
- Risk distribution
- Prediction results table
- Downloadable CSV results

---

## 📄 14. Batch Prediction CSV Format

A batch prediction CSV should contain the customer features expected by the preprocessing pipeline.

Example:

```csv
gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges
Female,0,Yes,No,24,Yes,No,DSL,Yes,No,Yes,No,No,No,One year,Yes,Credit card (automatic),65.5,1572.0
Male,0,No,No,5,Yes,Yes,Fiber optic,No,No,No,No,Yes,Yes,Month-to-month,Yes,Electronic check,85.2,426.0
```

Feature names must match the features expected by the trained preprocessing pipeline.

---

## 🔐 15. Environment Variables

If environment variables are required in the future, create a local:

```text
.env
```

file.

Example:

```env
KEY=value
```

Do not commit `.env` files to GitHub.

The project's `.gitignore` excludes `.env`.

---

## 🔒 16. Git Ignore Configuration

Important ignored files and directories include:

```text
.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
.vscode/
.env
```

---

## ☁️ 17. Streamlit Deployment

The production application is deployed using Streamlit.

Live application:

https://customerchurnintelligenceplatform.streamlit.app/

The repository should contain the application entry point:

```text
app.py
```

and the required application directories:

```text
pages/
utils/
assets/
models/
data/
```

Dependencies are installed from:

```text
requirements.txt
```

---

## 🔄 18. Updating the Deployed Application

After making changes locally:

```bash
git status
git add .
git commit -m "Update application"
git push origin main
```

If the Streamlit deployment is connected to the GitHub repository, the deployed application will update from the pushed changes.

---

## 🧪 19. Local Testing Before Deployment

Before pushing changes:

```bash
streamlit run app.py
```

Check that:

- Home page loads correctly
- Sidebar navigation works
- Dataset Explorer loads
- Analytics page works
- Model Comparison loads
- Individual prediction works
- Churn probability is displayed
- Risk classification works
- SHAP explanation opens correctly
- Batch CSV upload works
- Batch predictions are generated
- CSV download works
- Images load correctly
- CSS styling loads correctly
- The application works on different screen sizes

Only push changes after the application has been tested locally.

---

## 🛠️ 20. Common Issues

### Streamlit command not found

Make sure the virtual environment is activated:

```bash
.venv\Scripts\activate
```

Then install Streamlit if necessary:

```bash
pip install streamlit
```

Run:

```bash
streamlit run app.py
```

### ModuleNotFoundError

Install all dependencies:

```bash
pip install -r requirements.txt
```

Also verify that the virtual environment is active.

### Model File Not Found

Check that the trained model files exist inside:

```text
models/
```

Also check the filenames and paths used by:

```text
utils/data_loader.py
```

### Dataset File Not Found

Check that the required dataset exists in:

```text
data/raw/
```

Also verify the paths defined in:

```text
utils/paths.py
```

### SHAP Explanation Not Working

Make sure SHAP is installed:

```bash
pip install shap
```

Make sure a customer prediction has already been generated before opening the SHAP page.

Also verify that the trained model is compatible with the SHAP explainer used by the application.

### Batch Prediction Validation Error

Check that the uploaded CSV contains all required features.

The application validates the uploaded dataset against the features expected by the preprocessing pipeline.

---


## 🚀 23. Quick Start

### Windows

```bash
git clone https://github.com/sagarjana00/Customer_Churn_Intelligence_Platform.git
cd Customer_Churn_Intelligence_Platform
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

### macOS / Linux

```bash
git clone https://github.com/sagarjana00/Customer_Churn_Intelligence_Platform.git
cd Customer_Churn_Intelligence_Platform
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Live Application

**Customer Churn Intelligence Platform**

https://customerchurnintelligenceplatform.streamlit.app/

---

## 📚 GitHub Repository

https://github.com/sagarjana00/Customer_Churn_Intelligence_Platform

