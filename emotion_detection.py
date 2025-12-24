import json
import requests

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    """
    Sends text to the Watson NLP EmotionPredict endpoint and returns a formatted dictionary:
    anger, disgust, fear, joy, sadness and dominant_emotion.
    """
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, headers=HEADERS, json=payload)

    # Convert response text (JSON string) to dictionary
    response_dict = json.loads(response.text)

    # Navigate to emotions scores in the returned structure
    # (This is the typical structure for this lab’s Watson response)
    emotions = response_dict["emotionPredictions"][0]["emotion"]

    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
    }

    dominant_emotion = max(scores, key=scores.get)

    # Required output format
    scores["dominant_emotion"] = dominant_emotion
    return scores

