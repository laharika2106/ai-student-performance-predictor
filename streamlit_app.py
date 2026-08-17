import streamlit as st

from model import predict_performance
from ai_recommendation import generate_recommendations


# Page configuration
st.set_page_config(
    page_title="AI Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)


# Title
st.title("🎓 AI Student Performance Predictor")

st.write(
    "Enter your academic information to predict performance "
    "and receive personalized AI study recommendations."
)


# Input section
st.header("📊 Student Information")

python_marks = st.number_input(
    "Python Marks",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

ai_ml_marks = st.number_input(
    "AI/ML Marks",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

dsa_marks = st.number_input(
    "DSA Marks",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

study_hours = st.number_input(
    "Study Hours Per Day",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)


# Prediction button
if st.button("🚀 Predict Performance"):

    # ML prediction
    prediction = predict_performance(
        python_marks,
        ai_ml_marks,
        dsa_marks,
        attendance,
        study_hours
    )

    st.success(f"📊 Predicted Performance: **{prediction}**")


    # AI recommendations
    with st.spinner("🤖 Generating personalized AI recommendations..."):

        recommendations = generate_recommendations(
            python_marks,
            ai_ml_marks,
            dsa_marks,
            attendance,
            study_hours,
            prediction
        )

    st.subheader("🤖 AI Study Recommendations")

    st.write(recommendations)


# Footer
st.divider()

st.caption(
    "Built with Python, Scikit-learn, Streamlit and Gemini AI"
)