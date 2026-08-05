import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# -------------------------
# Load Data
# -------------------------

df = pd.read_csv("health_data.csv")

model = joblib.load("health_risk_model.pkl")

st.set_page_config(
    page_title="Health Risk Dashboard",
    layout="wide"
)

st.title("🏥 Health Risk Prediction Dashboard")

# ==========================
# Sidebar
# ==========================

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Dataset",
        "Visualizations",
        "Prediction",
        "About"
    ]
)

# ==========================
# Dataset
# ==========================

if menu == "Dataset":

    st.header("Dataset")

    st.write(df.head())

    st.subheader("Shape")

    st.write(df.shape)

    st.subheader("Statistics")

    st.write(df.describe())

# ==========================
# Visualization
# ==========================

elif menu == "Visualizations":

    st.header("Age Distribution")

    fig, ax = plt.subplots()

    ax.hist(df["Age"], bins=15)

    st.pyplot(fig)

    st.header("BMI Distribution")

    fig, ax = plt.subplots()

    ax.hist(df["BMI"], bins=15)

    st.pyplot(fig)

    st.header("Risk Level")

    st.bar_chart(df["RiskLevel"].value_counts())

# ==========================
# Prediction
# ==========================

elif menu == "Prediction":

    st.header("Predict Health Risk")

    age = st.number_input("Age",18,100,40)

    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

    bmi = st.number_input(
        "BMI",
        10.0,
        60.0,
        25.0
    )

    bp = st.number_input(
        "Blood Pressure",
        70,
        220,
        120
    )

    chol = st.number_input(
        "Cholesterol",
        100,
        400,
        180
    )

    glucose = st.number_input(
        "Glucose",
        50,
        300,
        100
    )

    smoking = st.selectbox(
        "Smoking",
        ["Yes","No"]
    )

    exercise = st.slider(
        "Exercise Hours",
        0,
        10,
        3
    )

    diabetes = st.selectbox(
        "Diabetes",
        ["Yes","No"]
    )

    heart = st.selectbox(
        "Heart Disease",
        ["Yes","No"]
    )

    cost = st.number_input(
        "Annual Medical Cost",
        1000,
        300000,
        20000
    )

    if st.button("Predict"):

        patient = pd.DataFrame({

            "Age":[age],
            "Gender":[gender],
            "BMI":[bmi],
            "BloodPressure":[bp],
            "Cholesterol":[chol],
            "Glucose":[glucose],
            "Smoking":[smoking],
            "Exercise":[exercise],
            "Diabetes":[diabetes],
            "HeartDisease":[heart],
            "AnnualMedicalCost":[cost]

        })

        prediction = model.predict(patient)

        st.success(
            f"Predicted Risk Level : {prediction[0]}"
        )

# ==========================
# About
# ==========================

else:

    st.header("About")

    st.write("""
    Health Risk Prediction using Machine Learning

    Algorithms:
    - Logistic Regression
    - Decision Tree
    - Random Forest

    Developed using:
    - Python
    - Streamlit
    - Scikit-Learn
    """)