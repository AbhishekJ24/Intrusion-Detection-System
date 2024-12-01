from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import data_preprocessing
from joblib import dump
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

files = [
    "Intrusion-Detection-System/app/server/archive/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
    "Intrusion-Detection-System/app/server/archive/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
    "Intrusion-Detection-System/app/server/archive/Friday-WorkingHours-Morning.pcap_ISCX.csv", 
    "Intrusion-Detection-System/app/server/archive/Monday-WorkingHours.pcap_ISCX.csv",
    "Intrusion-Detection-System/app/server/archive/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
    "Intrusion-Detection-System/app/server/archive/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv", 
    "Intrusion-Detection-System/app/server/archive/Tuesday-WorkingHours.pcap_ISCX.csv",
    "Intrusion-Detection-System/app/server/archive/Wednesday-workingHours.pcap_ISCX.csv"
]

logging.info("Loading and preprocessing data...")
X, y = data_preprocessing.preprocess_data(files)

# Split data
logging.info("Splitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
logging.info("Training XGBoost model...")
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Predict and evaluate
logging.info("Evaluating model...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
logging.info(f"XGBoost Accuracy: {accuracy}")

# Save the model
logging.info("Saving the trained model...")
dump(model, "Intrusion-Detection-System/app/server/models/xgb_model.joblib")
