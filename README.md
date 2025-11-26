<p align="center">
  <img src="https://img.shields.io/badge/P600%20-RETINOPATHY%20PREDICTION-blueviolet?style=for-the-badge" />
</p>

<h1 align="center">🩺 Diabetic Retinopathy Prediction (P600 Machine Learning Project)</h1>

<p align="center">
   Predicting diabetic retinopathy using clinical features with an end-to-end ML pipeline and Streamlit web deployment.
</p>

## 🛠 Tech Stack

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Numpy-Data-blue?logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-yellow?logo=pandas" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML%20Model-orange?logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/CatBoost-Classifier-orange?logo=catboost" />
  <img src="https://img.shields.io/badge/Streamlit-WebApp-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter" />
</p>

## 🚀 Key Features

### ✔ End-to-End Machine Learning Pipeline
Complete workflow including data cleaning, preprocessing, EDA, feature engineering, model building, and evaluation.

### ✔ High-Accuracy Prediction Model
Implemented and evaluated multiple ML models.  
Final selected model: **CatBoost Classifier** (excellent performance on structured medical data).

### ✔ Fully Deployed Web Application
Interactive **Streamlit web app** for real-time Diabetic Retinopathy prediction using user input values.

### ✔ Clean & Professional Project Structure
Organized into:
- `Dataset/`
- `Notebooks/`
- `Models/`
- `App/`
- `assets/images/`

### ✔ Dataset of 6000 Patients
Balanced medical dataset with features like age, blood pressure, cholesterol, prognosis, etc.

### ✔ Visual Output
Prediction results + probability chart displayed interactively.

### ✔ Production-Ready Code
Reusable model pipeline, modular code, and environment setup using `requirements.txt`.

---
## 🛠 Tech Stack

**Languages & Libraries**
- Python  
- NumPy  
- Pandas  
- Matplotlib / Seaborn  
- Scikit-Learn  
- CatBoost  
- Streamlit  

**Tools & Platforms**
- Git & GitHub  
- VS Code  
- Jupyter Notebook  
- Windows 10  

**Project Type**
- Machine Learning  
- Classification Model  
- Healthcare Analytics  

## 🔄 Project Workflow
Business Understanding →
Data Collection →
Data Cleaning & Preprocessing →
EDA & Insights →
Feature Engineering →
Model Building (LR, RF, CatBoost) →
Model Evaluation →
Best Model Selection (CatBoost) →
Streamlit Deployment →
Final Web Application


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
```


---

## 📸 Application Screenshots

<p align="center">
  <img src="assets/images/app_ui.png" width="600" />
</p>

<p align="center">
  <img src="assets/images/app_ss.png" width="600" />
</p>

<p align="center">
  <img src="assets/images/app_ss2.png" width="600" />
</p>
---

---

## 👤 **Author – Swayam Moon**

<p align="left">
  <img src="https://img.shields.io/badge/Created%20By-Swayam%20Moon-blueviolet?style=for-the-badge" />
</p>

Hi! I'm **Swayam Moon**, a passionate **Machine Learning & Data Science Enthusiast** who loves building real-world ML solutions—especially healthcare-related prediction systems.  
I focus on creating fully functional, deployment-ready ML apps with clean structure & professional workflows.

---

### 🌟 **About Me**
- 🎯 Focus Areas: Machine Learning, Healthcare Analytics, Model Deployment  
- 🧠 Skills: Python, Pandas, NumPy, EDA, Streamlit, CatBoost, Scikit-Learn  
- 🧩 Interests: Problem Solving, End-to-End DS Pipelines, UI/UX for ML Apps  
- 🚀 Always learning & improving  

---

### 🔗 **Connect With Me**

<p align="left">
  <a href="mailto:swayammoon9373@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Email-swayammoon9373%40gmail.com-red?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>

  <a href="https://github.com/SwayamMoon" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-SwayamMoon-black?style=for-the-badge&logo=github" />
  </a>

  <a href="https://www.linkedin.com/in/swayam-moon-374373238" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Swayam%20Moon-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
</p>

---

⭐ *If you found this project helpful or impressive, please consider giving it a star — it motivates me to build more amazing ML projects!* ⭐

