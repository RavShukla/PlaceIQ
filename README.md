# PlaceIQ

> Machine Learning Powered Student Placement Prediction System

PlaceIQ is an end-to-end **Data Science and Machine Learning project** that predicts student placement outcomes based on academic performance, practical experience, aptitude, soft skills, and placement preparation.

The goal of PlaceIQ was not just to train a model inside a Jupyter Notebook, but to build a complete ML application — from **data analysis and model training to Flask integration, interactive frontend development, and deployment**.

---

## About the Project

Student placement depends on multiple factors rather than a single academic score.

PlaceIQ analyzes different aspects of a student's profile and uses a trained Machine Learning classification model to predict the likely placement outcome.

The project demonstrates the complete lifecycle of a Data Science application:

```text
Data
  ↓
Exploratory Data Analysis
  ↓
Data Preprocessing
  ↓
Feature Analysis
  ↓
Model Training
  ↓
Model Evaluation
  ↓
Model Serialization
  ↓
Flask Integration
  ↓
Interactive Web Application
  ↓
Deployment
```

---

## Features

- Machine Learning based placement prediction
- Interactive student profile form
- 10 student profile features
- Real-time predictions
- Flask backend integration
- Responsive frontend
- Saved ML model integration
- Input validation
- Clean and interactive UI
- End-to-end ML application
- Single full-stack deployment

---

## Machine Learning Model

PlaceIQ treats student placement prediction as a **Binary Classification problem**.

### Final Model

**Logistic Regression**

The model was trained and evaluated using **Scikit-learn**.

The final application uses:

```text
scikit-learn==1.6.1
```

to maintain compatibility with the serialized trained model.

---

## Model Input Features

The prediction model analyzes **10 student profile factors**:

| # | Feature |
|---|---|
| 1 | CGPA |
| 2 | SSC Marks |
| 3 | HSC Marks |
| 4 | Internships |
| 5 | Projects |
| 6 | Workshops / Certifications |
| 7 | Aptitude Test Score |
| 8 | Soft Skills Rating |
| 9 | Extracurricular Activities |
| 10 | Placement Training |

These features are passed to the trained model to generate the final placement prediction.

---

## How PlaceIQ Works

```text
Student
   ↓
Enters Profile Information
   ↓
HTML / CSS / JavaScript Frontend
   ↓
Flask Backend
   ↓
Input Validation & Preparation
   ↓
Serialized ML Model
   ↓
Logistic Regression Prediction
   ↓
Placement Result
   ↓
Displayed on Frontend
```

The frontend collects the student's profile information.

Flask receives the input and prepares it in the format expected by the trained model.

The serialized Machine Learning model performs inference and returns the predicted placement outcome to the frontend.

---

## Tech Stack

### Data Science & Machine Learning

- Python
- NumPy
- Pandas
- Scikit-learn
- Jupyter Notebook
- Joblib / Pickle

### Backend

- Flask
- Gunicorn

### Frontend

- HTML5
- CSS3
- JavaScript

### Deployment & Version Control

- Git
- GitHub
- Render

---

## Project Structure

```text
PlaceIQ/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── backend/
│   ├── models/
│   │   ├── placement_model.pkl
│   │   └── model_features.pkl
│   │
│   ├── routes/
│   ├── services/
│   └── utils/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_data_preprocessing.ipynb
│   ├── 04_model_training.ipynb
│   ├── 05_model_evaluation.ipynb
│   └── 06_model_explainability.ipynb
│
├── templates/
│   ├── index.html
│   ├── predict.html
│   └── about.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    ├── js/
    │   └── main.js
    │
    └── assets/
        ├── favicon.ico
        └── gaurav.jpg
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/RavShukla/PlaceIQ.git
```

Move into the project:

```bash
cd PlaceIQ
```

---

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run PlaceIQ

```bash
python app.py
```

Flask will start the development server.

Open the address displayed in your terminal, usually:

```text
http://127.0.0.1:5000
```

---

## Requirements

The production application uses:

```text
Flask
gunicorn
numpy
pandas
scikit-learn==1.6.1
joblib
```

---

## Pages

PlaceIQ contains three main sections:

### Home

Introduces PlaceIQ and explains how the placement prediction system works.

### Predict

Allows students to enter their profile information and generate a placement prediction.

### About

Explains the project and introduces the developer behind PlaceIQ.

---

## Project Objective

The main objective of PlaceIQ was to build a **complete Machine Learning application**, rather than stopping after model training.

A Machine Learning model becomes much more valuable when it can actually be used.

PlaceIQ therefore focuses on the complete process:

```text
Data
→ Analysis
→ Machine Learning
→ Evaluation
→ Model Serialization
→ Backend Integration
→ Frontend
→ Deployment
```

---

## Disclaimer

PlaceIQ provides a **Machine Learning based estimate**, not a guarantee of placement.

Actual placement outcomes may depend on many additional factors including:

- Technical skills
- Interview performance
- Communication
- Company requirements
- Job availability
- Market conditions
- Individual performance

The prediction should therefore be treated as an analytical insight rather than a definitive placement decision.

---

## Developer

### Gaurav Shukla

**Data Scientist & Machine Learning Engineer**

I'm focused on transforming data into practical and intelligent applications.

My interests include **Data Science, Machine Learning, predictive modelling, AI, model integration, and end-to-end ML product development**.

I enjoy working across the complete Machine Learning lifecycle — from understanding and analyzing data to training models, evaluating their performance, integrating them with backend systems, and turning them into applications people can actually use.

PlaceIQ represents that approach: taking a Machine Learning problem from dataset exploration all the way to a working and deployable application.

---

## Connect With Me

**GitHub**

https://github.com/RavShukla

**LinkedIn**

https://www.linkedin.com/in/gauravshukla2006

**Portfolio**

https://portfolio-ten-xi-zdxqp8eq2i.vercel.app/

---

## Repository

https://github.com/RavShukla/PlaceIQ

---

If you found this project interesting, consider giving the repository a ⭐.

**Designed & Developed by Gaurav Shukla**
