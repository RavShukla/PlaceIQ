REQUIRED_FEATURES = [
    "CGPA",
    "Internships",
    "Projects",
    "Workshops/Certifications",
    "AptitudeTestScore",
    "SoftSkillsRating",
    "ExtracurricularActivities",
    "PlacementTraining",
    "SSC_Marks",
    "HSC_Marks"
]


def validate_student_data(data):
    """
    Validate incoming student data.

    Returns:
        (True, None) if valid
        (False, error_message) if invalid
    """

    if not isinstance(data, dict):
        return False, "Invalid request data."

    # Check missing fields
    missing_fields = [
        feature
        for feature in REQUIRED_FEATURES
        if feature not in data
    ]

    if missing_fields:
        return False, f"Missing fields: {', '.join(missing_fields)}"

    # Check empty values
    for feature in REQUIRED_FEATURES:
        if data[feature] is None or data[feature] == "":
            return False, f"{feature} cannot be empty."

    return True, None