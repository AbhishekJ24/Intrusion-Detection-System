from flask import Flask, jsonify
from flask_cors import CORS  # Import Flask-CORS
from sklearn.ensemble import RandomForestClassifier
import psutil
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize RandomForestClassifier with dummy data
try:
    model = RandomForestClassifier()
    model.fit(
        [
            [0, 0, 0, 0, 0],       # Secure condition
            [100, 100, 100, 1, 1], # Intrusion condition
        ],
        [0, 1]
    )
except Exception as e:
    print(f"Error initializing the model: {e}")
    model = None

def extract_system_data():
    """Extracts system metrics for prediction."""
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        net_io = psutil.net_io_counters()
        bytes_sent = net_io.bytes_sent
        bytes_received = net_io.bytes_recv
        return [cpu_usage, memory_usage, disk_usage, bytes_sent, bytes_received]
    except Exception as e:
        print(f"Error extracting system data: {e}")
        return None

@app.route("/analyze-network", methods=["POST"])
def analyze_network():
    """Analyzes system data and predicts security status."""
    if model is None:
        return jsonify({"message": "Model not loaded. Please check the server."}), 500

    try:
        system_data = extract_system_data()
        if system_data is None:
            return jsonify({"message": "Failed to extract system data."}), 500

        normalized_data = [
            system_data[0],
            system_data[1],
            system_data[2],
            system_data[3] / 1e9,
            system_data[4] / 1e9,
        ]
        prediction = model.predict([normalized_data])[0]
        result = "Intrusion detected!" if prediction == 1 else "Network is secure."
        return jsonify({"message": result, "data": system_data})
    except Exception as e:
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
