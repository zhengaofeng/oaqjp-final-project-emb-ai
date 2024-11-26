from flask import Flask,
from EmotionDetection.emotion_detection import emotion_detector

app=Flask(__main__)

@app.route("")