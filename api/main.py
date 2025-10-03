from fastapi import FastAPI
from src.logic import recommend_by_flavor
from src.db import insert_sample_data

app = FastAPI(title="Juice & Shake Recommendation API")

@app.get("/")
def home():
    return {"message": "Welcome to Juice & Shake Recommendation API 🍹"}

@app.post("/insert-sample")
def insert_data():
    return {"status": insert_sample_data()}

@app.get("/recommend/")
def recommend(flavor: str, drink_type: str = None):
    recs = recommend_by_flavor(flavor, drink_type)
    return {"recommendations": recs}
