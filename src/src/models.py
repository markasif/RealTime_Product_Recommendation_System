import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Load the data
df = pd.read_csv('your_data.csv')

# Label Encoding the 'event' column
label_encoder = LabelEncoder()
df['event'] = label_encoder.fit_transform(df['event'])

# Save the encoder for future use
joblib.dump(label_encoder, 'models/label_encoder.pkl')

# Train a KNN model
X = df[['visitorid', 'event', 'property']]
y = df['itemid']
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# Save the trained model for future use
joblib.dump(knn, 'models/knn_model.pkl')
