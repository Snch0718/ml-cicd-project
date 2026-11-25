
import joblib

artifact = joblib.load("model.joblib")

model = artifact["model"]
target_names = artifact["target_names"]


def predict_species(features):
    prediction = model.predict([features])[0]
    probabilities = model.predict_proba([features])[0]

    return {
        "prediction": target_names[prediction],
        "confidence": float(max(probabilities))
    }
