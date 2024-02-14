from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer


class ZeroShotClassifier:
    """
    A zero-shot classifier that predicts whether various sentiments and intents.
    """

    def __init__(self, model_path):
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.zero_shot_classifier = pipeline("zero-shot-classification", model=self.model, tokenizer=self.tokenizer)

    def classify(self, text, candidate_labels):
        """
        Classify text for given candidate labels.
        """
        result = self.zero_shot_classifier(text, candidate_labels)
        return result
