
from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.model import predict_species

app = FastAPI(
    title="Iris ML Prediction API",
    description="An ML application deployed using a CI/CD pipeline",
    version="1.0.0"
)


class IrisInput(BaseModel):
    sepal_length: float = Field(gt=0)
    sepal_width: float = Field(gt=0)
    petal_length: float = Field(gt=0)
    petal_width: float = Field(gt=0)


@app.get("/")
def home():
    return {"message": "ML API is running!"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: IrisInput):
    features = [
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]

    return predict_species(features)
