import streamlit as st
import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_configuration(page_title="AI Multi-Disease Diagnostic", layout="wide")

# --- MOCK MODEL LOADING (For Demo Purposes) ---
# In a real scenario, you'd use: model = pickle.load(open('model.pkl', 'rb'))
def mock_predict(data, disease_type):
    # Stimulate a probability for the demo
    import numpy as np
    return np.random.uniform(0.1, 0.8)

# --- UI HEADER ---
st.title("Ai-Health-Analyzer")
st.markdown("Enter your vitals below for a comprehensive risk assessment.")

# --- SIDEBAR / INPUT ---
with st.sidebar:
    st.header("Patient Demographics")
    age = st.number_input("age", 1,120, 25)
    gender = st.selectbox("gender", ["male", "female"])
    bmi = st.slider("BMI", 10.0, 50.0, 22.5)

    st.header("Clinical Vitals")
    glucose = st.slider("glucose", 50, 300, 100)
    bp = st.number_input("Blood Pressure (systolic)", 80, 200, 120)
    chol = st.number_input("cholestrol", 100, 400, 180)

# --- PROCESSING ---
if st.button("Analyze Health Profile"):
    col1, col2 = st.columns(2)

    # Example Feature Vector
    input_data = pd.DataFrame([[age, bmi, glucose, bp, chol]],
                              columns=['age', 'BMI', 'Glucose', 'BP', 'Cholesterol'])

    with col1:
        st.subheader("Risk Assessment")

        # Diabetes Check
        d_risk = mock_predict(input_data, "diabetese")
        st.write(f"Diabetes Risk: {d_risk*100:.1f}%")
        st.progress(d_risk)

        # Heart Disease Check
        h_risk = mock_predict(input_data, "heart")
        st.write(f"Heart Disease Risk: {h_risk*100:.1f}%")
        st.progress(h_risk)

    with col2:
        st.subheader("Why this score? (SHAP)")
        # SHAP visualization (Mock)
        fig, ax = plt.subplots()
        features = ['Glucose', 'Age', 'BMI']
        importance = [0.4, 0.2, 0.1]
        ax.barh(features, importance, color='teal')
        st.pyplot(fig)

    # --- DOCTOR BOOKING ---
    st.divider()
    st.subheader("Direct Specialist consult")
    st.info("Based on your profile, we recommend speaking with a doctor.")
    st.link_button("Book Appointment via Zocdoc", "https://www.zocdoc.com")                                 