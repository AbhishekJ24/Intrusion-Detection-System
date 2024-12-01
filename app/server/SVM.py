from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import data_preprocessing
from joblib import dump


files = [
        "Intrusion-Detection-System/app/server/archive/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
        "Intrusion-Detection-System/app/server/archive/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv","Intrusion-Detection-System/app/server/archive/Friday-WorkingHours-Morning.pcap_ISCX.csv", "Intrusion-Detection-System/app/server/archive/Monday-WorkingHours.pcap_ISCX.csv","Intrusion-Detection-System/app/server/archive/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv","Intrusion-Detection-System/app/server/archive/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv", "Intrusion-Detection-System/app/server/archive/Tuesday-WorkingHours.pcap_ISCX.csv","Intrusion-Detection-System/app/server/archive/Wednesday-workingHours.pcap_ISCX.csv"
    ]
X, y = data_preprocessing.preprocess_data(files)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train SVM model
model = SVC(kernel='rbf', probability=True)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(f"SVM Accuracy: {accuracy_score(y_test, y_pred)}")

dump(model, "Intrusion-Detection-System/app/server/models/svm_model.joblib")