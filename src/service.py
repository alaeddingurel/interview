from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.classifier import ZeroShotClassifier
from src.model_manager import ModelManager
import uvicorn


class InputText(BaseModel):
    text: str


app = FastAPI()

# Provide the local path to the pre-trained model
model_path = '/resources/models--facebook--bart-basea/snapshots/aadd2ab0ae0c8268c7c9693540e9904811f36177'

model_manager = ModelManager("bart-model", "models--facebook--bart-base", local_model_path="../resources/")
model_manager.check_and_download_model()

zero_shot_classifier = ZeroShotClassifier(model_path)


@app.post("/predict/")
async def predict(input_text: InputText):
    candidate_labels = ["science", "technology", "history", "politics"]
    try:
        classification_result = zero_shot_classifier.classify(input_text.text, candidate_labels)
        return classification_result["labels"][0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def main():
    uvicorn.run(app, host="127.0.0.1", port=8001)


if __name__ == '__main__':
    main()
