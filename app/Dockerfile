FROM python:3.9-slim

WORKDIR /app

# Copy app code (including model.pkl and main.py)
COPY . /app

# Create models directory (optional since file already inside)
RUN mkdir -p /app/models

# ✅ No need to copy from ../models anymore
# If model.pkl is already in /app, just move it into models folder
RUN mv /app/model.pkl /app/models/model.pkl

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn joblib scikit-learn dill

# Start FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
