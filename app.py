from flask import Flask, render_template

from backend.routes.prediction_routes import prediction_bp


app = Flask(__name__)


# API routes
app.register_blueprint(prediction_bp)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict")
def predict_page():
    return render_template("predict.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)