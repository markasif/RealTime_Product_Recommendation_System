<<<<<<< HEAD
# Real-Time Product Recommendation

This project provides a real-time product recommendation system using the K-Nearest Neighbors (KNN) algorithm. It processes user input (event), trains a KNN model, and recommends the three nearest events.

## Project Structure

- `data/processed/Processed.csv`: Contains the raw data.
- `models/label_encoder.pkl`: Stores the label encoder for categorical column encoding.
- `models/knn_model.pkl`: Stores the trained KNN model.
- `src/data_processing.py`: Handles data preprocessing and label encoding.
- `src/models.py`: Trains the KNN model.
- `src/utils.py`: Utility functions for generating recommendations.
- `app.py`: Flask application to serve the recommendations.
- `templates/`: Contains HTML files for the front-end.
- `requirements.txt`: Lists the dependencies needed to run the app.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
=======
This is project that focused on realtime product recommendation system
>>>>>>> 1bfa13f63c6b1eb542e5f2d3522e09cdc55d9cc6
