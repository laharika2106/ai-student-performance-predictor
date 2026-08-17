import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

import joblib


# Load dataset
df = pd.read_csv("data/student_performance.csv")

print("Dataset loaded successfully!")
print(df.head())


# Features and target
X = df[
    [
        "Python",
        "AI_ML",
        "DSA",
        "Attendance",
        "Study_Hours"
    ]
]

y = df["Performance"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train model
model.fit(X_train, y_train)

print("\nModel training completed!")


# Predictions
y_pred = model.predict(X_test)


# Evaluation
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy:.2%}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Save model
joblib.dump(model, "performance_model.pkl")

print("\nModel saved as performance_model.pkl")