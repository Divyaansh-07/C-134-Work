from flask import Flask, render_template, url_for, request, jsonify
from text_sentiment_prediction import predicted_emotion,predicted_emotion_imagUrl
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    input_text=request.json.get("text")
    if not input_text:
        response={
            'status':"error",
            "message":'Please enter to predict emotion'
        }
        return jsonify(response)
    else:
        response={
            'status':"success",
            "data":{
                "predicted_emotion":predicted_emotion,
                "predicted_emotion_Url":predicted_emotion_imagUrl
            }
        }
        return jsonify(response)
app.run(debug=True)