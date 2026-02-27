import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Ensure artifacts folder exists
os.makedirs("../artifacts", exist_ok=True)

# Load Car Evaluation dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data"
columns = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
car = pd.read_csv(url, names=columns)

# Encode categorical features
label_encoders = {}
for col in car.columns:
    le = LabelEncoder()
    car[col] = le.fit_transform(car[col])
    label_encoders[col] = le

# Split features and target
X = car.drop("class", axis=1)
y = car["class"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and encoders
model_path = os.path.join("../artifacts", "model.pkl")
encoders_path = os.path.join("../artifacts", "encoders.pkl")
joblib.dump(model, model_path)
joblib.dump(label_encoders, encoders_path)

print("Model and encoders saved to artifacts/")