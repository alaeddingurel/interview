from src.model_manager import ModelManager
from src.utils import read_transcript, merge_transcript, read_yaml_file


def evaluate(config, zero_shot_classifier):
    """
    This function just makes a sample evaluation for Task 1
    """

    # Parameters
    sentiments = config["sentiments"]
    intents = config["intents"]
    sample_data_path = config["sample_data_path"]

    transcript_data = read_transcript(sample_data_path)
    merged_transcript = merge_transcript(transcript_data)

    # print("evaluating1...")
    # model_manager = ModelManager(bucket_name, model_name, local_model_path="resources/")
    # zero_shot_classifier = model_manager.check_and_download_model()
    # print("evaluating2...")

    sentiment_result = zero_shot_classifier.classify(merged_transcript, sentiments)
    intent_result = zero_shot_classifier.classify(merged_transcript, intents)

    top_sentiment = sentiment_result["labels"][0] if sentiment_result["labels"] else None
    top_intent = intent_result["labels"][0] if intent_result["labels"] else None

    result_dict = {"sentiment": top_sentiment, "intent": top_intent}

    print(result_dict)
