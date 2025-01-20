from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

app = Flask(__name__)

# Load saved models
def load_models():
    # Load the label encoder and KNN model from disk
    label_encoder = joblib.load('models/label_encoder.pkl')
    knn_model = joblib.load('models/knn_model.pkl')
    return label_encoder, knn_model

# Custom function to handle unseen labels
def transform_with_default(label_encoder, data, default_value=-1):
    try:
        return label_encoder.transform(data)
    except ValueError:
        unseen_labels = [label for label in data if label not in label_encoder.classes_]
        transformed_data = [
            label_encoder.transform([label])[0] if label not in unseen_labels else default_value
            for label in data
        ]
        return np.array(transformed_data)

def recommend_items(input_data):
    # Load models
    label_encoder, knn_model = load_models()

    # Preprocess input data
    input_data['event'] = transform_with_default(label_encoder, [input_data['event']])

    # Prepare features
    X_input = pd.DataFrame([input_data], columns=['visitorid', 'event', 'property'])

    # Make predictions using KNN
    recommended_itemids = knn_model.predict(X_input)
    return recommended_itemids.tolist()

@app.route('/')
def home():
    return render_template('index.html')  # Serve the index.html page

@app.route('/recommend', methods=['POST'])
def recommend():
    input_data = request.json  # Get data from POST request
    recommended_itemids = recommend_items(input_data)  # Process the recommendation
    return jsonify({'recommended_items': recommended_itemids}), 200  # Return as JSON

if __name__ == '__main__':
    app.run(debug=True)
