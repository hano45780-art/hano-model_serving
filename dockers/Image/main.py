import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
model = joblib.load("model.joblib")

species = ["setosa", "versicolor", "virginica"]


class IrisRequest(BaseModel):
    data: list[float]


@app.post("/predict")
def predict(request: IrisRequest):
    if len(request.data) != 4:
        raise HTTPException(
            status_code=400,
            detail="data에는 꽃 특성값 4개를 입력해야 합니다."
        )

    prediction = int(model.predict([request.data])[0])

    return {
        "prediction": prediction,
        "species": species[prediction],
    }