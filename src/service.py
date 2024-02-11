from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.model_manager import ModelManager
from src.utils import read_yaml_file
import uvicorn


class InputText(BaseModel):
    text: str


app = FastAPI()

config = read_yaml_file("config/config.yaml")

# Parameters
sentiments = config["sentiments"]
intents = config["intents"]
sample_data_path = config["sample_data_path"]
bucket_name = config["bucket_name"]
model_name = config["model_name"]

model_manager = ModelManager(bucket_name, model_name, local_model_path="../resources/")
zero_shot_classifier = model_manager.check_and_download_model()
# print(model)
#
# zero_shot_classifier = ZeroShotClassifier(model_path)


@app.post("/predict/")
async def predict(input_text: InputText):

    result_dict = {"sentiments": "", "intents": ""}

    try:
        sentiment_result = zero_shot_classifier.classify(input_text.text, sentiments)
        intent_result = zero_shot_classifier.classify(input_text.text, intents)

        top_sentiment = sentiment_result["labels"][0] if sentiment_result["labels"] else None
        top_intent = intent_result["labels"][0] if intent_result["labels"] else None

        result_dict = {"sentiment": top_sentiment, "intent": top_intent}

        return result_dict

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def main():
    uvicorn.run(app, host="127.0.0.1", port=8002)


if __name__ == '__main__':
    main()
