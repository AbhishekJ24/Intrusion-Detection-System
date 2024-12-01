from joblib import load
import numpy as np

# Load trained objects
scaler = load("scaler.joblib")
pca = load("pca.joblib")

def preprocess_live_data(packet_features):
    if len(packet_features) == 0:
        return np.empty((0, scaler.mean_.shape[0]))
    scaled_features = scaler.transform(packet_features)
    try:
        reduced_features = pca.transform(scaled_features)
        return reduced_features
    except Exception as e:
        print(f"Error during PCA transformation: {e}")
        return scaled_features

