
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Save model artifact
joblib.dump(
    {
        "model": model,
        "target_names": iris.target_names.tolist()
    },
    "model.joblib"
)

print("Model trained and saved successfully!")
