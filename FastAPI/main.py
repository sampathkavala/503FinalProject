from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.cluster import KMeans
import joblib
from custom_features import feature_engineering
app = FastAPI()


# final_model_experiment_7.pkl

final_pipeline_expt7 = joblib.load("../Model/final_model_experiment_7.pkl")
best_threshold = 0.27


class Payload(BaseModel):
    Age: int
    Duration: int
    Campaign: int
    Pdays: int
    Previous: int
    EmpVarRate: float
    ConsPriceIdx: float
    ConsConfIdx: float
    Euribor3m: float
    NrEmployed: float

    Job: str
    Marital_Status: str
    Education: str
    Default_Status: str
    Housing: str
    Loan: str
    Contact: str
    Month: str
    DayOfWeek: str
    Poutcome: str

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "Name": "Sri Satya Sai Sampath Kavala",
        "Project": "Term Loan Subscription Prediction",
        "Model": "Exp7"
    }


@app.post("/predict")
def predict(payload: Payload):
    # 3) Convert incoming JSON -> DataFrame
    #    Using payload.dict() or payload.model_dump() for pydantic v2
    #    Then each item is a single-row df
   

    df = pd.DataFrame([payload.model_dump()])

    # 4) Probability for "yes" class
    pos_class_proba = final_pipeline_expt7.predict_proba(df)[:, 1]

    # 5) Compare to custom threshold
    binary_class = (pos_class_proba >= best_threshold).astype(int)

    # 6) Optional: Map 0->"no", 1->"yes"
    map_class = {0: "no", 1: "yes"}
    predicted_label = map_class[binary_class[0]]

    # 7) Return a JSON response with final label, probability, threshold, etc.
    return {
        "Subscribed": predicted_label,       # e.g. "no" or "yes"
    }