from src.model_manager import ModelManager
from src.utils import read_transcript, merge_transcript, read_yaml_file


def main():
    # Read Yaml File
    config = read_yaml_file("config/config.yaml")

    # Parameters
    sentiments = config["sentiments"]
    intents = config["intents"]
    sample_data_path = config["sample_data_path"]
    bucket_name = config["bucket_name"]
    model_name = config["model_name"]

    transcript_data = read_transcript(sample_data_path)
    merged_transcript = merge_transcript(transcript_data)

    model_manager = ModelManager(bucket_name, model_name, local_model_path="resources/")
    zero_shot_classifier = model_manager.check_and_download_model()

    sentiment_result = zero_shot_classifier.classify(merged_transcript, sentiments)
    intent_result = zero_shot_classifier.classify(merged_transcript, intents)

    top_sentiment = sentiment_result["labels"][0] if sentiment_result["labels"] else None
    top_intent = intent_result["labels"][0] if intent_result["labels"] else None

    result_dict = {"sentiment": top_sentiment, "intent": top_intent}

    print(result_dict)


if __name__ == '__main__':
    main()
