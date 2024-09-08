# Sentiment Analysis of Roman Urdu

This project is a Flask API that predicts the sentiment (positive, negative, or neutral) of Roman Urdu text using a custom tokenizer and a pre-trained TensorFlow model. The model processes the Roman Urdu input, tokenizes it, and provides sentiment predictions.

## Features
- Predicts sentiment of Roman Urdu text (positive, negative, neutral)
- Uses a custom tokenizer (`roman_tokenizer`)
- Flask API for easy integration with web and mobile apps
- CORS enabled for cross-origin requests

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.7+
- Flask
- TensorFlow
- NumPy
- Keras Preprocessing
- Flask-CORS

### Installing Dependencies
Install the required Python libraries using `pip`:

```bash
pip install -r requirements.txt
