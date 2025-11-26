# 🩺 Diabetic Retinopathy Prediction – Machine Learning Project (P600)

A complete end-to-end Machine Learning project developed to predict **Diabetic Retinopathy** using clinical health indicators. This project includes data preprocessing, EDA, feature engineering, model development, evaluation, and deployment using a fully interactive **Streamlit web application**.

---

## 🚀 Project Overview

Diabetic Retinopathy is a major diabetes-related eye disease and a leading cause of blindness. Early prediction can significantly help in clinical decision-making and disease management.  
This project builds a **binary classification model** to predict whether a patient is at risk of retinopathy based on blood pressure, age, and cholesterol levels.

---

## 🎯 Business Objective

To develop a machine learning solution that accurately predicts the presence of diabetic retinopathy (1 = Yes, 0 = No) using patient clinical data.  
The solution must be:

- ✔ Accurate  
- ✔ Interpretable  
- ✔ Deployment-ready  
- ✔ Easy for healthcare practitioners to use  

---

## 📁 Dataset Information

The dataset contains **6000 patient records** with the following features:

| Feature | Description |
|--------|-------------|
| ID | Unique patient identifier |
| Age | Patient’s age |
| Systolic_BP | Upper blood pressure value |
| Diastolic_BP | Lower blood pressure value |
| Cholesterol | Cholesterol level (mg/dl) |
| Prognosis | Target variable (0 = No Retinopathy, 1 = Yes Retinopathy) |

---

## 🔍 Exploratory Data Analysis (EDA)

EDA focuses on:

- Distribution of blood pressure & age  
- Correlation between features  
- Outlier detection  
- Class imbalance distribution  
- Key patterns that influence prognosis  

The insights guided the feature engineering strategy and model selection.

---

## 🔧 Feature Engineering & Preprocessing

- Handling missing values  
- Outlier treatment  
- Scaling numerical features  
- Encoding target variable  
- Splitting data into training & testing  

---

## 🤖 Model Development

Multiple models were tested:

- Logistic Regression  
- Random Forest  
- LightGBM  
- CatBoost Classifier (Final Model)

**CatBoost** was selected due to excellent performance and ability to handle categorical & numerical data efficiently.

---

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | ~90% |
| Precision | High |
| Recall | High |
| ROC-AUC | Strong classifier separation |

CatBoost provided the best balance of accuracy and generalization.

---

## 🌐 Deployment (Streamlit Web App)

The project includes a fully interactive **Streamlit web app** where users can enter patient clinical values and get real-time predictions.

### Run locally:
```bash
pip install -r requirements.txt
streamlit run app.py
