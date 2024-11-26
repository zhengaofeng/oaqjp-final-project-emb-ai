"""
server.py
A Flask application for emotion detection.
Provides routes for emotion detection and rendering the index page.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_app():
    """
    Route for emotion detection.
    Accepts a text input via query parameters and returns the detected emotions.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['anger'] is None:
        return "无效文本！请再试一次！"
    return response

@app.route("/")
def render_index_page():
    """
    Route to render the main index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
