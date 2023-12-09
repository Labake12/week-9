from flask import Flask, request, jsonify
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the saved model
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load("bow.pkl")
# create a route that manages user request and does sentiment prediction
@app.route('/ping')
def home():
    return 'Welcome to Sentiment Analysis API!'
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']
    vectorized_text = vectorizer.transform([text])
    prediction = model.predict(vectorized_text)[0]
    return jsonify({'sentiment': prediction})

if __name__ == '__main__':
    app.run()