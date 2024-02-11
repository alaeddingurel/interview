from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
from transformers import BartTokenizer, BartModel

class ZeroShotClassifier:
    def __init__(self, model_path):
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.zero_shot_classifier = pipeline("zero-shot-classification", model=self.model, tokenizer=self.tokenizer)

    def classify(self, text, candidate_labels):
        result = self.zero_shot_classifier(text, candidate_labels)
        return result


if __name__ == '__main__':

    # facebook/bart-base
    # facebook/bart-large
    # facebook/bart-large-mnli

    #TODO Full path needed maybe there should be function which takes the directory and the directory in the end of the file
    model_path = "facebook/bart-large-mnli"
    zero_shot_classifier = ZeroShotClassifier(model_path)

    input_text = "I'm really interest on the python programming language and the front-end development"

    candidate_labels = ["science", "technology", "history", "politics"]

    classification_result = zero_shot_classifier.classify(input_text, candidate_labels)

    print("Input Text:", input_text)
    print("Predicted Label:", classification_result['labels'])
    print("Confidence Score:", classification_result['scores'])

    #inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")
    #outputs = model(**inputs)

    #last_hidden_states = outputs.last_hidden_state

    #print(last_hidden_states)