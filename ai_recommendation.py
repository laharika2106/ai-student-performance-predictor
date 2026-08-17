import os

import streamlit as st
from dotenv import load_dotenv
from google import genai


# Load local .env file
load_dotenv()


# Get API key from local .env or Streamlit Cloud secrets
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        api_key = None


if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. "
        "Add it to your .env file locally or Streamlit Secrets when deployed."
    )


client = genai.Client(api_key=api_key)


def generate_recommendations(
    python_marks,
    ai_ml_marks,
    dsa_marks,
    attendance,
    study_hours,
    performance
):

    prompt = f"""
You are an AI academic mentor.

Analyze the following student information:

Python marks: {python_marks}
AI/ML marks: {ai_ml_marks}
DSA marks: {dsa_marks}
Attendance: {attendance}%
Study hours per day: {study_hours}
Predicted performance: {performance}

Provide personalized and practical recommendations.

Include:
1. Overall assessment
2. Strong areas
3. Areas that need improvement
4. Five specific recommendations
5. A simple weekly study strategy

Use simple language suitable for a college student.
Do not make medical, financial, or other high-stakes claims.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text