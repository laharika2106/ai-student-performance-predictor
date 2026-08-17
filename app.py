from model import predict_performance
from ai_recommendation import generate_recommendations


print("=" * 60)
print("       🎓 AI STUDENT PERFORMANCE PREDICTOR")
print("=" * 60)


python_marks = float(input("Enter Python marks: "))
ai_ml_marks = float(input("Enter AI/ML marks: "))
dsa_marks = float(input("Enter DSA marks: "))
attendance = float(input("Enter attendance percentage: "))
study_hours = float(input("Enter study hours per day: "))


# ML prediction
prediction = predict_performance(
    python_marks,
    ai_ml_marks,
    dsa_marks,
    attendance,
    study_hours
)


print("\n" + "=" * 60)
print("                 📊 ML RESULT")
print("=" * 60)

print(f"Predicted Performance: {prediction}")


# Gemini recommendation
print("\n🤖 Generating AI recommendations...")

recommendations = generate_recommendations(
    python_marks,
    ai_ml_marks,
    dsa_marks,
    attendance,
    study_hours,
    prediction
)


print("\n" + "=" * 60)
print("              🤖 AI RECOMMENDATIONS")
print("=" * 60)

print(recommendations)

print("\n" + "=" * 60)
print("             Thank you! 🎓")
print("=" * 60)