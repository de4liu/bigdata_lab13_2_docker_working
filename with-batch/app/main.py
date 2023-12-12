import pickle
import numpy as np
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, conlist

app = FastAPI(title="Predicting Wine Class with batching")

# Represents a batch of wines
class Wine(BaseModel):
    # your code here:    


@app.on_event("startup")
def load_clf():
    # Load classifier from pickle file
    with open("wine.pkl", "rb") as file:
        global clf
        clf = pickle.load(file)


@app.get("/")
def home():
    return "Congratulations! Your API is working as expected. This new version allows for batching. Now head over to /docs"


@app.post("/predict")
def predict(wine: Wine):
    # your code here:
