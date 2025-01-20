import numpy as np
from sklearn.preprocessing import LabelEncoder
import joblib

# Custom function to handle unseen labels
def transform_with_default(label_encoder, data, default_value=-1):
    transformed_data = []
    for label in data:
        try:
            transformed_data.append(label_encoder.transform([label])[0])
        except ValueError:
            transformed_data.append(default_value)
    return np.array(transformed_data)
