const predictionForm = document.getElementById("predictionForm");
const resultSection = document.getElementById("predictionResult");
const predictionText = document.getElementById("predictionText");
const probabilityText = document.getElementById("probabilityText");


if (predictionForm) {

    predictionForm.addEventListener("submit", async (event) => {

        event.preventDefault();

        const submitButton = predictionForm.querySelector(
            'button[type="submit"]'
        );

        // Collect form values
        const formData = new FormData(predictionForm);

        const studentData = {
            CGPA: Number(formData.get("CGPA")),
            Internships: Number(formData.get("Internships")),
            Projects: Number(formData.get("Projects")),
            "Workshops/Certifications": Number(
                formData.get("Workshops/Certifications")
            ),
            AptitudeTestScore: Number(
                formData.get("AptitudeTestScore")
            ),
            SoftSkillsRating: Number(
                formData.get("SoftSkillsRating")
            ),
            ExtracurricularActivities: Number(
                formData.get("ExtracurricularActivities")
            ),
            PlacementTraining: Number(
                formData.get("PlacementTraining")
            ),
            SSC_Marks: Number(formData.get("SSC_Marks")),
            HSC_Marks: Number(formData.get("HSC_Marks"))
        };


        try {

            // Loading state
            submitButton.disabled = true;
            submitButton.textContent = "Analyzing...";


            const response = await fetch("/api/predict", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(studentData)

            });


            const result = await response.json();


            if (!response.ok) {
                throw new Error(
                    result.error || "Prediction failed."
                );
            }


            // Convert model output to readable text
            const prediction =
                Number(result.prediction) === 1
                    ? "Likely to be Placed"
                    : "Placement Risk";


            predictionText.textContent = prediction;


            // Probability
            if (
                result.probability !== undefined &&
                result.probability !== null
            ) {

                const probability =
                    (Number(result.probability) * 100).toFixed(1);

                probabilityText.textContent =
                    `Model confidence: ${probability}%`;

            } else {

                probabilityText.textContent = "";

            }


            // Reveal result section
            resultSection.hidden = false;

            resultSection.scrollIntoView({
                behavior: "smooth",
                block: "center"
            });

        } catch (error) {

            console.error(error);

            resultSection.hidden = false;

            predictionText.textContent =
                "Unable to generate prediction.";

            probabilityText.textContent =
                error.message;

        } finally {

            submitButton.disabled = false;
            submitButton.textContent =
                "Analyze My Profile";

        }

    });

}