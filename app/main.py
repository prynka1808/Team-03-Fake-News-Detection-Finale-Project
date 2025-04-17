from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import joblib

# Load trained model and vectorizer
vectorizer, model = joblib.load("models/model.pkl")

app = FastAPI()

class NewsInput(BaseModel):
    text: str

@app.post("/predict")
def predict(news: NewsInput):
    vec = vectorizer.transform([news.text])
    prediction = model.predict(vec)[0]
    return {"prediction": "Fake" if prediction == 1 else "Real"}

# Mount static folder for UI
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")
