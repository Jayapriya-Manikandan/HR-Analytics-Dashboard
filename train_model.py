import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Convert Target Variable
df["Attrition"] = df["Attrition"].map({"Yes": 1, "No": 0})

# Store Label Encoders
encoders = {}

# Encode Categorical Columns
for column in df.select_dtypes(include="object").columns:
    if column != "Attrition":
        encoder = LabelEncoder()
        df[column] = encoder.fit_transform(df[column])
        encoders[column] = encoder

# Split Features and Target
X = df.drop("Attrition", axis=1)
y = df["Attrition"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("=" * 40)
print("HR ATTRITION MODEL")
print("=" * 40)
print(f"Accuracy : {accuracy:.4f}")
print("=" * 40)

# Create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save Model
joblib.dump(model, "model/attrition_model.pkl")

# Save Encoders
joblib.dump(encoders, "model/label_encoders.pkl")

print("Model Saved Successfully!")
print("Location : model/attrition_model.pkl")

print("Encoders Saved Successfully!")
print("Location : model/label_encoders.pkl")