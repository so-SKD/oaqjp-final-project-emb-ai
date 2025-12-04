"""
Flask web application for sentiment analysis using Watson NLP API.
The application takes text input, processes it using sentiment analysis, 
and returns the sentiment label and score to the user.
"""

# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Analyzes the sentiment of the input text and returns a formatted string 
    with the sentiment label and score. 
    If the input is invalid, an error message is returned.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Call emotion detector function w/in given text
    result = emotion_detector(text_to_analyze)

    #Check if dominant emotion is none
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Prepare response in spec'd format
    emotions = result
    response = (
    f"For the given statement, the system response is 'anger': {emotions['anger']}, "
    f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, "
    f"'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. "
    f"The dominant emotion is {emotions['dominant_emotion']}."
)

    return response

@app.route("/")
def render_index_page():
    """
    Renders the index page (HTML) for the sentiment analysis web interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    