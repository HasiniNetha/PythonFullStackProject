from fastapi import FastAPI, Query
from src.logic import recommend_by_flavor
from src.db import insert_sample_data, check_connection

app = FastAPI(title="🥤 Juice & Shake Recommendation API")

@app.get("/")
def home():
    return {"message": "Welcome to the Juice & Shake Recommendation API 🍹"}

@app.get("/check")
def check():
    return {"status": check_connection()}

@app.post("/insert-sample")
def insert_data():
    status = insert_sample_data()
    return {"status": status}

@app.get("/recommend/")
def recommend(flavor: str = Query(..., description="Enter a flavor"), drink_type: str = Query(None, description="Enter type (Shake, Juice, Drink, or Any)")):
    recommendations = recommend_by_flavor(flavor, drink_type)
    return {"recommendations": recommendations}
