"""
Flask web server for the Emotion Detection application.

Routes:
- /                 : Renders the UI page.
- /emotionDetector  : Returns formatted emotion scores for the given text.
"""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

# Pylint may flag Flask's conventional 'app' variable name as invalid-name.
# Disabling only this rule helps keep a clean 10/10 score.
# pylint: disable=invalid-name
app = Flask(__name__)


@app.route("/")
def home():
    """Render the main application page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Run emotion detection on the provided text and return a formatted response.

    Query parameter:
      - textToAnalyze: The text input to be analyzed.

    Returns:
      - A formatted string with the emotion scores and dominant emotion,
        or an error message for invalid/blank input.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )


def main():
    """Run the Flask development server on localhost:5000."""
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
