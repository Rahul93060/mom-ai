# Use an official Python 3.11 slim image for a smaller base image.
FROM python:3.11-slim AS builder

# Ensure Python output is sent straight to the terminal and not buffered.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install build tools needed during dependency installation, then remove package lists.
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Poetry in the builder stage.
RUN python -m pip install --upgrade pip
RUN pip install poetry

# Copy only dependency metadata first to leverage Docker layer caching.
COPY pyproject.toml /app/

# Install only production dependencies from Poetry.
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-root --no-interaction --no-ansi

# Copy application code and required runtime assets.
COPY . /app

# Final stage: create a smaller runtime image.
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=django_project.settings

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy the installed Python packages from the builder stage.
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy app source and ML artifacts into the runtime image.
COPY --from=builder /app /app

# Expose port 5000 for the Django app.
EXPOSE 5000

# Run the Django development server on the requested port.
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
