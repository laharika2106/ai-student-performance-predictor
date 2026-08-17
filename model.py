import joblib
import pandas as pd


# Load trained model
model = joblib.load("performance_model.pkl")


def predict_performance(
    python_marks,
    ai_ml_marks,
    dsa_marks,
    attendance,
    study_hours
):

    data = pd.DataFrame([
        {
            "Python": python_marks,
            "AI_ML": ai_ml_marks,
            "DSA": dsa_marks,
            "Attendance": attendance,
            "Study_Hours": study_hours
        }
    ])

    prediction = model.predict(data)[0]

    return prediction


# Test prediction
if __name__ == "__main__":

    result = predict_performance(
        python_marks=85,
        ai_ml_marks=82,
        dsa_marks=88,
        attendance=92,
        study_hours=8
    )

    print("Predicted Performance:", result)