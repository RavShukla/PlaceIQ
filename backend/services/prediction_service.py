from pathlib import Path
import joblib
import pandas as pd


# Path to backend/models/
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"


# Load trained model and saved feature names
model = joblib.load(MODEL_DIR / "placement_model.pkl")
model_features = joblib.load(MODEL_DIR / "model_features.pkl")


def predict_placement(student_data):
    """
    Receives student data as a dictionary and returns
    placement prediction and probability.
    """

    # Create DataFrame using the exact features/order
    # used during model training
    input_data = pd.DataFrame(
        [student_data],
        columns=model_features
    )

    # Make prediction
    prediction = model.predict(input_data)[0]

    result = {
        "prediction": int(prediction)
    }

    # Add probability if the trained model supports it
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_data)[0]

        result["probability"] = float(max(probabilities))

    return result