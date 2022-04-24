from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from predictor import model_predictor
from fastapi.middleware.cors import CORSMiddleware

model=model_predictor()

class input_val(BaseModel):
    Open: float
    High: float
    Low: float
    Sentiment: int


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/predict")
async def predict(input_val:input_val):
    new_input_val={
            'Open' : [input_val.Open],
            'High': [input_val.High],
            'Low' : [input_val.Low],
            'Sentiment' : [input_val.Sentiment],
        }
    m=model.predict(input_val=new_input_val)
    return m
    





