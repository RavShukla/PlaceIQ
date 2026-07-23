from flask import Blueprint, request, jsonify

from backend.services.prediction_service import predict_placement
from backend.utils.validation import validate_student_data


prediction_bp = Blueprint("prediction", __name__)


@prediction_bp.route("/api/predict", methods=["POST"])
def predict():
    try:
        # Get JSON sent by frontend
        student_data = request.get_json()

        # Validate input
        is_valid, error = validate_student_data(student_data)

        if not is_valid:
            return jsonify({
                "success": False,
                "error": error
            }), 400

        # Send validated data to ML model
        result = predict_placement(student_data)

        # Return prediction to frontend
        return jsonify({
            "success": True,
            "prediction": result["prediction"],
            "probability": result.get("probability")
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500