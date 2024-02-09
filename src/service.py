from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from classifier import ZeroShotClassifier


class InputText(BaseModel):
    text: str

app = FastAPI()

# Provide the local path to the pre-trained model
model_path = 'C:/Users/alaed/Documents/GitHub/interview/resources/models--facebook--bart-base/snapshots/aadd2ab0ae0c8268c7c9693540e9904811f36177'
zero_shot_classifier = ZeroShotClassifier(model_path)

@app.post("/predict/")
async def predict(input_text: InputText):
    candidate_labels = ["science", "technology", "history", "politics"]
    try:
        classification_result = zero_shot_classifier.classify(input_text.text, candidate_labels)
        return classification_result["labels"][0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
