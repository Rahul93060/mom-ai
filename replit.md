# MOM AI - Maternal Health Risk Prediction

## Overview

MOM AI is a Django web application that predicts maternal health risk levels (low, mid, high) using a trained Random Forest machine learning model. Users input health parameters (age, blood pressure, blood sugar, body temperature, heart rate) through a web form, and the system returns a risk prediction. The project combines a scikit-learn ML pipeline with a Django frontend — it's essentially a 3-page app: Home, Prediction Form, and Result.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Project Structure
- **Django Project**: `django_project/` contains settings, URL routing, WSGI/ASGI configs
- **Predictor App**: `predictor/` is the single Django app handling all functionality
- **ML Pipeline**: `train_model.py` at the project root trains and exports the model
- **Pickle Files**: `mom_ai_model.pkl`, `label_encoder.pkl`, and `feature_names.pkl` are serialized ML artifacts stored at the project root

### Backend (Django)
- **Framework**: Django 5.0 with a single app called `predictor`
- **No database usage**: The app doesn't use Django models or a database for its core functionality. The default SQLite may be configured but isn't essential. No migrations are needed for app logic.
- **Views**: Two function-based views — `home` (landing page) and `predict` (handles form + prediction)
- **Forms**: A single Django form (`MaternalHealthForm`) with 6 fields matching the ML model's training features: Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate
- **ML Model Loading**: The trained RandomForest model and LabelEncoder are loaded from pickle files at module import time in `views.py`
- **Settings**: `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` are dynamically set from the `REPLIT_DOMAINS` environment variable for Replit compatibility

### Frontend
- **Templates**: 3 HTML templates in `predictor/templates/predictor/` — `home.html`, `form.html`, `result.html`
- **Styling**: Bootstrap 5 via CDN, with minimal custom CSS. A gradient hero section on the home page.
- **No JavaScript framework** — server-rendered HTML with Django template tags

### Machine Learning Pipeline
- **Algorithm**: RandomForestClassifier from scikit-learn
- **Training Script**: `train_model.py` — can use a CSV dataset (`maternal health high risk pregnancy dataset 1.csv`) or generates synthetic data if the file is missing
- **Target Variable**: `RiskLevel` with 3 classes (low risk, mid risk, high risk), label-encoded
- **Features**: Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate
- **Serialization**: Model, label encoder, and feature names are saved as `.pkl` files using pickle
- **Important**: The `train_model.py` script must be run before starting the Django server to generate the pickle files. If pickle files are missing, the server will crash on startup.

### URL Routing
- `/` — Home page
- `/predict/` — Prediction form (GET) and result processing (POST)
- `/admin/` — Django admin (standard, not customized)

### Running the Application
1. Run `python train_model.py` to generate model pickle files
2. Run `python manage.py runserver 0.0.0.0:5000` to start the Django server
3. The app serves on port 5000

## External Dependencies

### Python Packages
- **Django 5.0** — Web framework
- **scikit-learn** — Machine learning (RandomForestClassifier, LabelEncoder)
- **pandas** — Data manipulation for training
- **numpy** — Numerical operations for predictions
- **pickle** (stdlib) — Model serialization

### Frontend CDN
- **Bootstrap 5.3** — CSS framework loaded from `cdn.jsdelivr.net`

### Environment Variables
- **REPLIT_DOMAINS** — Required; used to configure `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`. This is automatically set by Replit.

### No External Services
- No database connection required (no Postgres, no external DB)
- No external APIs consumed
- No authentication system in use
- All ML inference runs locally using pickle-serialized model files