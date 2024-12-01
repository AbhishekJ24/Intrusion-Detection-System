import time
import numpy as np
from joblib import load
from features import extract_features
from preprocess import preprocess_live_data
from capture import capture_traffic
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load trained model
logging.info("Loading the trained model...")
model = load("models/xgb_model.joblib")

def analyze_traffic(live_data):
    if live_data.shape[0] == 0:
        logging.info("No live data to predict.")
        return []
    predictions = model.predict(live_data)
    return predictions

def monitor_network(interface="Wi-Fi", duration=5, sleep_duration=1):
    logging.info(f"Monitoring network on {interface}...")
    
    while True:
        logging.info("Capturing traffic...")
        packets = capture_traffic(interface=interface, capture_duration=duration)
        
        if len(packets) == 0:
            logging.warning("No packets captured.")
            time.sleep(sleep_duration)
            continue
        
        packet_features = extract_features(packets)
        if packet_features.size > 0:
            logging.info("preprocessing packets...")
            live_data = preprocess_live_data(packet_features)

            logging.info("analyzing traffic...")
            predictions = analyze_traffic(live_data)
            
            if np.any(predictions == 1):
                logging.warning("Alert: Cyber attack detected!")
            else:
                logging.info("No attack detected.")
        else:
            logging.info("No relevant features extracted from packets.")
        
        time.sleep(sleep_duration)

if __name__ == "__main__":
    monitor_network(interface="Wi-Fi", duration=5)
