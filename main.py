from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from roman_tokenizer import roman_tokenizer, loadFromPickle
from keras.preprocessing.sequence import pad_sequences
from flask_cors import CORS

model = load_model('deep_sentiment_model.keras')
if model:
    print("Model Loaded!")
vocab = loadFromPickle('vocab.pkl')
app = Flask(__name__)
CORS(app)

@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    input_data = request.json
    input_sentence = input_data.get('sentence')

    input_sentence = roman_tokenizer(input_sentence)
    input_sequence = [vocab.get(token, 0) for token in input_sentence]
    input_sequence = pad_sequences([input_sequence], maxlen=100, padding='post', truncating='post')

    predicted_probabilities = model.predict(input_sequence)
    predicted_sentiment = np.argmax(predicted_probabilities)

    sentiment_labels = ['Negative', 'Neutral', 'Positive']
    predicted_sentiment_label = sentiment_labels[predicted_sentiment]

    response = {
        'input_sentence': input_sentence,
        'predicted_sentiment': predicted_sentiment_label
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
