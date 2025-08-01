import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained model
with open("salary_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page config
st.set_page_config(
    page_title="Employee Salary Prediction",
    page_icon="💼",
    layout="centered"
)

# Add a sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown("### 👩‍💼 Salary Predictor")
    st.info("This tool estimates employee salary based on experience, education, and job profile.")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f7f7f7;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title & description
st.title("💼 Employee Salary Predictor")
st.markdown("Fill in the details below to predict the estimated **salary** of an employee.")

# Input section
with st.form("salary_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("📅 Age", 20, 60, 30)
        gender = st.selectbox("🧑‍🤝‍🧑 Gender", ["Male", "Female"])
        education = st.selectbox("🎓 Education", ["Bachelor's", "Master's", "PhD"])

    with col2:
        job_title = st.selectbox("💼 Job Title", [
            'Software Engineer', 'Data Analyst', 'Senior Manager', 'Sales Associate',
            'Director', 'Marketing Analyst', 'Product Manager', 'Sales Manager',
            'Marketing Coordinator', 'Senior Scientist', 'Software Developer',
            'HR Manager', 'Financial Analyst', 'Project Manager', 'Customer Service',
            'Operations Manager', 'Marketing Manager', 'Senior Engineer',
            'Data Entry Clerk', 'Sales Director', 'Business Analyst',
            'VP of Operations', 'IT Support', 'Recruiter', 'Financial Manager'
        ])
        experience = st.slider("📈 Years of Experience", 0, 30, 5)

    submitted = st.form_submit_button("🚀 Predict Salary")

if submitted:
    input_df = pd.DataFrame([[gender, education, job_title, age, experience]],
                            columns=['Gender', 'Education', 'Job Title', 'Age', 'YearsExperience'])

    prediction = model.predict(input_df)[0]
    st.success(f"💰 Estimated Salary: ₹ {int(prediction):,}")
