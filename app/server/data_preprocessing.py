#pre process the dataset and perform feature selection using pca
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder, StandardScaler
from joblib import dump

def preprocess_data(file_paths):
    # Load and concatenate data
    data = pd.concat([pd.read_csv(file) for file in file_paths], axis=0)
    
    data.columns = data.columns.str.strip()  # Remove any leading/trailing spaces in column names

    # Encode labels
    label_encoder = LabelEncoder()
    data['Label'] = label_encoder.fit_transform(data['Label'])

    # Replace infinite values with NaN
    data.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Impute missing values (NaN) with the mean of each column
    data.fillna(data.mean(), inplace=True)

    # Separate features and target variable
    X = data.drop('Label', axis=1)
    y = data['Label']
    
    # Feature scaling
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(X)
    
    # PCA for feature reduction
    pca = PCA(n_components=20)  # Adjust components as needed
    principal_components = pca.fit_transform(scaled_features)

    dump(scaler, "scaler.joblib")
    dump(pca, "pca.joblib")
    
    return principal_components, y

if __name__ == "__main__":
    files = [
        "Intrusion-Detection-System/app/server/archive/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
        "Intrusion-Detection-System/app/server/archive/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv","Intrusion-Detection-System/app/server/archive/Friday-WorkingHours-Morning.pcap_ISCX.csv", "Intrusion-Detection-System/app/server/archive/Monday-WorkingHours.pcap_ISCX.csv","Intrusion-Detection-System/app/server/archive/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv","Intrusion-Detection-System/app/server/archive/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv", "Intrusion-Detection-System/app/server/archive/Tuesday-WorkingHours.pcap_ISCX.csv","Intrusion-Detection-System/app/server/archive/Wednesday-workingHours.pcap_ISCX.csv"
    ]
    X, y = preprocess_data(files)
    print(f"Data shape after PCA: {X.shape}")
