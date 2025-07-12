from flask import Flask, render_template, request
import pickle
import os
import sys

# Fix path for utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.feature_extractor import extract_features

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
model_path = os.path.join(BASE_DIR, 'model', 'phishing_model.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form['url']
        features = extract_features(url)
        prediction = model.predict([features])[0]
        result = "Phishing Website ⚠️" if prediction == 1 else "Legitimate Website ✅"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
