from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
import joblib

app = Flask(__name__) 

app.static_folder = 'static'


# Load the pre-trained models
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
naive_bayes_model = joblib.load('bernoulli_naive_bayes_model.pkl')
svm_model = joblib.load('linear_svc_model.pkl')
logistic_regression_model = joblib.load('logistic_regression_model.pkl')

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    """Analyze the sentiment of the input sentence."""
    sentence = request.form['sentence']
    
    # Predict sentiment
    results = predict_sentiment(sentence)
    
    return jsonify(results)

def predict_sentiment(sentence):
    """Predict sentiment using pre-trained models."""
    # Transform the input sentence using the TF-IDF vectorizer
    sentence_transformed = tfidf_vectorizer.transform([sentence])
    
    # Make predictions using all three models
    prediction_naive_bayes = naive_bayes_model.predict(sentence_transformed)[0]
    prediction_svm = svm_model.predict(sentence_transformed)[0]
    prediction_logistic_regression = logistic_regression_model.predict(sentence_transformed)[0]
    
    # Convert predictions to human-readable format
    sentiment_result = {
        'Naive Bayes': 'Positive' if prediction_naive_bayes == 1 else 'Negative',
        'Support Vector Machine': 'Positive' if prediction_svm == 1 else 'Negative',
        'Logistic Regression': 'Positive' if prediction_logistic_regression == 1 else 'Negative'
    }
    
    return sentiment_result

if __name__ == '__main__':
    app.run(debug=True)
