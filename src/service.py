from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import FileResponse

from src.model_manager import ModelManager
from src.utils import read_yaml_file
import uvicorn
from fastapi.staticfiles import StaticFiles


class InputText(BaseModel):
    text: str


app = FastAPI()
app.mount("../static/", StaticFiles(directory="static"), name="static")


config = read_yaml_file("config/config.yaml")

# Parameters
sentiments = config["sentiments"]
intents = config["intents"]
sample_data_path = config["sample_data_path"]
bucket_name = config["bucket_name"]
model_name = config["model_name"]
host = config["host"]
port = config["port"]


# Model Manager to handle to download and load models from Local, GCS Bucket or Huggingface Hub
model_manager = ModelManager(bucket_name, model_name, local_model_path="resources/")
zero_shot_classifier = model_manager.check_and_download_model()

@app.get("/")
async def homepage():
    # Return HTML content for the homepage
    return FileResponse("static/homepage.html")

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


from typing import List


@app.post("/bulk_predict/")
async def bulk_predict(input_texts: List[InputText]):
    results = []

    for input_text in input_texts:
        result_dict = {"sentiment": "", "intent": ""}

        try:
            sentiment_result = zero_shot_classifier.classify(input_text.text, sentiments)
            intent_result = zero_shot_classifier.classify(input_text.text, intents)

            top_sentiment = sentiment_result["labels"][0] if sentiment_result["labels"] else None
            top_intent = intent_result["labels"][0] if intent_result["labels"] else None

            result_dict = {"sentiment": top_sentiment, "intent": top_intent}

            results.append(result_dict)

        except Exception as e:
            # Log or handle the exception as needed
            results.append({"error": str(e)})

    return results


def main():
    uvicorn.run(app, host=host, port=port)


if __name__ == '__main__':
    main()
