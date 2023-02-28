from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel 
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version

app = FastAPI()

class TextIn(BaseModel):
    text:str

class PredictionOut(BaseModel):
    language:str
    

@app.get("/")
def home():
    return {"health_check": "okk","model_version":model_version}

@app.post("/predict",response_model=PredictionOut)
def predict(payload:TextIn):
    language=predict_pipeline(payload.text)
    return {"language":language}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "qa": q}