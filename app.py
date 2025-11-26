# ============================================
#      RETINOPATHY PREDICTION WEB APP
#        Model: CatBoost Classifier
# ============================================
import streamlit as st
import pandas as pd
import numpy as np
import dill
import plotly.graph_objects as go

# ---------- PAGE CONFIGURATION ----------
st.set_page_config(
    page_title="Retinopathy Prediction",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CUSTOM CSS STYLING ----------
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            color: #FDFEFE;
            font-size: 42px;
            font-weight: 800;
            margin-bottom: 0px;
        }
        .sub-title {
            text-align: center;
            color: #58D68D;
            font-size: 20px;
            margin-bottom: 30px;
        }
        .result-box {
            background: linear-gradient(145deg, #1B2631, #212F3D);
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            color: #58D68D;
            font-size: 24px;
            font-weight: bold;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.4);
        }
        .footer {
            text-align: center;
            color: grey;
            font-size: 13px;
            margin-top: 50px;
        }
        .stApp {
            background-color: #0E1117;
            color: white;
        }
        .stButton>button {
            color: white;
            background: linear-gradient(90deg, #117A65, #16A085);
            border: none;
            padding: 10px 25px;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #1ABC9C, #48C9B0);
        }
        .stDataFrame {
            background-color: #1C2833;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1 class='main-title'>Retinopathy Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>🧠 Powered by CatBoost Machine Learning Model</h3>", unsafe_allow_html=True)
st.markdown("---")

# ---------- LOAD MODEL ----------
@st.cache_resource
def load_model():
    with open("logistic_model.pkl", "rb") as f:
        return dill.load(f)

model_pipeline = load_model()

# ---------- SIDEBAR INPUT ----------
st.sidebar.header("🩺 Enter Patient Details")

age = st.sidebar.number_input("Age (years)", min_value=1, max_value=100, value=32)
systolic_bp = st.sidebar.number_input("Systolic Blood Pressure (mm Hg)", min_value=60, max_value=200, value=110)
diastolic_bp = st.sidebar.number_input("Diastolic Blood Pressure (mm Hg)", min_value=40, max_value=130, value=70)
cholesterol = st.sidebar.number_input("Cholesterol (mg/dL)", min_value=100, max_value=400, value=180)

st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ Model Information")
st.sidebar.info("""
**Logistic Regression Classifier**  
Trained on health dataset with:  
- Age  
- Systolic BP  
- Diastolic BP  
- Cholesterol  
- Derived features like Pulse Pressure, BP Ratio, Age Group
""")

# ---------- COMPUTE DERIVED FEATURES ----------
pulse_pressure = systolic_bp - diastolic_bp
bp_ratio = systolic_bp / diastolic_bp

age_group = pd.cut(
    [age],
    bins=[0, 40, 60, 80, np.inf],
    labels=['young', 'middle_age', 'senior', 'elderly']
)[0]

age_group_encoded = {
    'young': 0, 'middle_age': 1, 'senior': 2, 'elderly': 3
}[age_group]

# ---------- PREPARE DATAFRAME ----------
input_data = pd.DataFrame([{
    'age': age,
    'systolic_bp': systolic_bp,
    'diastolic_bp': diastolic_bp,
    'cholesterol': cholesterol,
    'pulse_pressure': pulse_pressure,
    'bp_ratio': bp_ratio,
    'age_group_encoded': age_group_encoded
}])

# ---------- SHOW INPUT SUMMARY ----------
st.subheader("🧾 Input Summary")

styled_df = (
    input_data.style
    .set_properties(**{'color': 'black', 'background-color': '#F9F9F9'})
    .highlight_max(axis=0, color='#D1F2EB')
)
st.dataframe(styled_df)

# ---------- PREDICTION ----------
st.markdown("### 🧠 Model Prediction")

# yaha threshold set kar rahe hain: 70% se upar ho to hi Retinopathy bolo
RETINOPATHY_THRESHOLD = 70.0  # percentage

if st.button("🔍 Predict "):

    # probabilities nikaalo
    prediction_proba = model_pipeline.predict_proba(input_data)[0]
    classes = list(model_pipeline.classes_)

    # indices for no_retinopathy & retinopathy
    no_idx, ret_idx = 0, 1

    # string labels
    if "no_retinopathy" in classes and "retinopathy" in classes:
        no_idx = classes.index("no_retinopathy")
        ret_idx = classes.index("retinopathy")
    # numeric labels 0/1
    elif 0 in classes and 1 in classes:
        no_idx = classes.index(0)
        ret_idx = classes.index(1)

    no_prob = round(float(prediction_proba[no_idx]) * 100, 2)
    ret_prob = round(float(prediction_proba[ret_idx]) * 100, 2)

    class_labels = ["No Retinopathy", "Retinopathy Detected"]
    probs = [no_prob, ret_prob]

    # ---- DECISION USING THRESHOLD ----
    # agar Retinopathy probability 70% se kam hai to "No Retinopathy" hi bolo
    if ret_prob >= RETINOPATHY_THRESHOLD:
        # Retinopathy detected
        st.markdown(
            f"<div class='result-box' style='background: linear-gradient(145deg, #FADBD8, #F5B7B1); color:#922B21;'>"
            f"🔴 The model predicts: <b>Retinopathy Detected</b> <br> Confidence: {ret_prob:.2f}%"
            f"</div>",
            unsafe_allow_html=True
        )
    else:
        # No Retinopathy
        st.markdown(
            f"<div class='result-box'>🟢 The model predicts: <b>No Retinopathy</b> <br> Confidence: {no_prob:.2f}%</div>",
            unsafe_allow_html=True
        )

    # ---------- DARK-THEMED BAR GRAPH ----------
    st.markdown("### 📊 Prediction Probability Chart")

    fig = go.Figure(
        data=[go.Bar(
            x=class_labels,
            y=probs,
            text=[f"{p}%" for p in probs],
            textposition='auto',
            marker=dict(
                color=['#2ECC71', '#E74C3C'],  # Green for healthy, Red for retinopathy
                line=dict(color='#D0D3D4', width=1.5)
            )
        )]
    )

    fig.update_layout(
        title="Prediction Probability",
        title_x=0.3,
        xaxis_title="Classes",
        yaxis_title="Probability (%)",
        yaxis_range=[0, 100],
        plot_bgcolor="#1B2631",
        paper_bgcolor="#0E1117",
        font=dict(color="white", size=14),
        xaxis=dict(showgrid=False, color='white'),
        yaxis=dict(showgrid=True, gridcolor="#34495E", color='white'),
        margin=dict(l=40, r=40, t=60, b=40)
    )

    st.plotly_chart(fig, use_container_width=True)
