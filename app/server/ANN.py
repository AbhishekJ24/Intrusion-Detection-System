import data_preprocessing
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras  # Use TensorFlow's Keras
from scikeras.wrappers import KerasClassifier
from sklearn.model_selection import KFold, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split

files = [
        "Intrusion-Detection-System/app/server/archive/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
        "Intrusion-Detection-System/app/server/archive/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv","Intrusion-Detection-System/app/server/archive/Friday-WorkingHours-Morning.pcap_ISCX.csv", "Intrusion-Detection-System/app/server/archive/Monday-WorkingHours.pcap_ISCX.csv","Intrusion-Detection-System/app/server/archive/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv","Intrusion-Detection-System/app/server/archive/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv", "Intrusion-Detection-System/app/server/archive/Tuesday-WorkingHours.pcap_ISCX.csv","Intrusion-Detection-System/app/server/archive/Wednesday-workingHours.pcap_ISCX.csv"
    ]
X, y = data_preprocessing.preprocess_data(files)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build ANN model
def create_ann_model(neurons=64, optimizer='adam'):
    model = keras.Sequential()
    model.add(keras.layers.Dense(neurons, activation='relu', input_dim=X_train.shape[1]))
    model.add(keras.layers.Dense(neurons // 2, activation='relu'))
    model.add(keras.layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
    return model

model = KerasClassifier(model=create_ann_model, verbose=0)
# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Predict and evaluate
y_pred = (model.predict(X_test) > 0.5).astype(int)
print(f"ANN Accuracy: {accuracy_score(y_test, y_pred)}")
