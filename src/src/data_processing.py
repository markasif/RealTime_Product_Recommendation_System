import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    # Label Encoding the 'event' column
    label_encoder = LabelEncoder()
    df['event'] = label_encoder.fit_transform(df['event'])
    
    # Save the encoder for future use
    import joblib
    joblib.dump(label_encoder, 'models/label_encoder.pkl')
    
    # Drop the 'timestamp_x' and 'timestamp_y' columns as they are not useful for KNN
    df = df.drop(columns=['timestamp_x', 'timestamp_y'])
    
    return df, label_encoder
