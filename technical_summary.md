# MOM AI Project Technical Summary

## 1. Project Overview
- **What it does**
  - This is a Django web app for maternal health risk prediction.
  - It accepts user inputs for age, blood pressure, blood sugar, body temperature, and heart rate.
  - It uses a trained scikit-learn Random Forest model to classify risk as `low`, `mid`, or `high`.
- **Tech stack**
  - Language: Python
  - Framework: Django
  - ML: scikit-learn, pandas, numpy
  - Runtime: Python `>=3.11,<4.0` (from `pyproject.toml`)
  - Frontend: server-rendered Django templates + Bootstrap 5 via CDN
- **Repository type**
  - Single service application
  - Not a monorepo; one Django project with one app plus ML artifacts

---

## 2. Project Structure
- **Main folders and purpose**
  - `/django_project/` — Django project configuration
    - `settings.py`, `urls.py`, `wsgi.py`, `asgi.py`
  - `/predictor/` — main Django app
    - `views.py`, `forms.py`, `urls.py`, `tests.py`, templates, static assets
  - `/attached_assets/` — pasted documents and notes
- **Root files**
  - `manage.py` — Django CLI entry point
  - `pyproject.toml` — Poetry dependency and packaging config
  - `train_model.py` — ML training/export script
  - `mom_ai_model.pkl`, `label_encoder.pkl`, `feature_names.pkl` — trained ML artifacts
  - `db.sqlite3` — default SQLite database file
- **Entry point / main file**
  - `manage.py` is the app entry point for running the server and management commands
  - `django_project/wsgi.py` and `django_project/asgi.py` are deployment entry points
- **Multiple services?**
  - No separate frontend/backend services
  - No workers, queues, or sidecars
  - All functionality lives in one Django-backed web app

---

## 3. Dependencies & Package Management
- **Package manager**
  - Poetry via `pyproject.toml`
  - No `requirements.txt` present
  - No `poetry.lock` found in the repo
- **Key dependencies**
  - `django = "^4.2.0"`
  - `pandas = "^2.0.0"`
  - `scikit-learn = "^1.2.0"`
  - `numpy = "^1.24.0"`
  - `seaborn = "^0.12.0"`
  - `matplotlib = "^3.7.0"`
- **Dev dependencies**
  - None declared in `pyproject.toml`
- **Build tools**
  - Poetry build backend configured: `poetry-core`
  - No webpack/vite/Gradle/etc.

---

## 4. Environment & Configuration
- **Environment variables required**
  - `REPLIT_DEPLOYMENT` — used in code to adjust middleware for Replit deployment
- **Notes on env configuration**
  - No `.env` file found in the repo
  - No config YAML or similar config file present
  - `replit.md` mentions `REPLIT_DOMAINS`, but this is not referenced in `settings.py`
- **Ports**
  - App is expected to run on port `5000` based on docs
  - Standard Django dev server can also run on any configured port

---

## 5. Build & Run Commands
- **Install dependencies**
  - `poetry install`
- **Build project**
  - No separate build step required for Django
  - ML model training step: `python train_model.py`
- **Run locally**
  - `python manage.py runserver 0.0.0.0:5000`
- **Testing**
  - `python manage.py test`
  - Note: `predictor/tests.py` exists but contains only a placeholder and no tests

---

## 6. Database & External Services
- **Database**
  - SQLite (`django.db.backends.sqlite3`) at `db.sqlite3`
  - The app currently does not use any Django models for core prediction flow
- **Third-party APIs/services**
  - None detected
- **Message queues / caches**
  - None detected

---

## 7. Existing Docker / Deployment Setup
- **Docker**
  - No `Dockerfile`
  - No `docker-compose.yml`
- **CI/CD**
  - No GitHub Actions workflows
  - No `.github/workflows/`
  - No Jenkinsfile, GitLab CI, or similar
- **Deployment target**
  - The repo appears intended for Replit deployment based on `replit.md`
- **Cloud provider**
  - No explicit cloud provider config
  - Only Replit-specific environment variable support is referenced

---

## 8. Testing
- **Testing framework**
  - Django built-in test framework
- **Test files location**
  - `predictor/tests.py`
- **Test command**
  - `python manage.py test`

---

## 9. Special Requirements
- **Background jobs / cron**
  - None found
- **File storage**
  - Local disk storage for model artifacts (`.pkl` files)
  - No S3 or external storage configured
- **SSL / reverse proxy**
  - None found
  - No Nginx/Caddy config present
- **Secrets management**
  - None detected
  - Secret key is hardcoded in `django_project/settings.py`

---

## Key Observations for Docker / CI/CD Setup
- Single service: Dockerizing should wrap Python/Poetry + Django + model artifacts
- ML artifacts are required at runtime: `mom_ai_model.pkl` and `label_encoder.pkl`
- The app currently has no production-ready secrets or host configuration
- There is no existing CI file, so GitHub Actions will need to be created from scratch

If desired, a `Dockerfile`, `docker-compose.yml`, and GitHub Actions workflow can be added next.