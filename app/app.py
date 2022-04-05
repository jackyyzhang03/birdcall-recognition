from flask import Flask, render_template, request, jsonify, make_response
from predictor import Predictor
from audio_utils import AudioUtils
import os

predictor = Predictor('weights.pt')
app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.post('/')
def predict():
    file = request.files['audio']
    spectrogram = AudioUtils.get_spectrogram(file)
    prediction, probabilities = predictor.predict(spectrogram)
    response = make_response(
        jsonify({'prediction': prediction, 'probabilities': probabilities}))
    response.headers["Content-Type"] = "application/json"
    return response


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="localhost", port=port)
