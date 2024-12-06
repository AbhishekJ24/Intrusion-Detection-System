import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def process_dataset(file_path, label_column=' Label', n_top_features=10):
    df = pd.read_csv(file_path)
    label_encoder = LabelEncoder()
    df[label_column] = label_encoder.fit_transform(df[label_column])
    X = df.drop([label_column], axis=1)
    y = df[label_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf_model = RandomForestClassifier(random_state=42, n_jobs=-1)
    rf_model.fit(X_train, y_train)
    feature_importances = rf_model.feature_importances_
    features = X.columns
    feature_importance_df = pd.DataFrame({
        ' Feature': features,
        ' Importance': feature_importances
    }).sort_values(by='Importance', ascending=False)
    return feature_importance_df.head(n_top_features)


dataset_files = [
    'app/server/data/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv', 
    'app/server/data/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv',
    'app/server/data/Friday-WorkingHours-Morning.pcap_ISCX.csv',
    'app/server/data/Monday-WorkingHours.pcap_ISCX.csv',
    'app/server/data/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv', 
    'app/server/data/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv', 
    'app/server/data/Tuesday-WorkingHours.pcap_ISCX.csv', 
    'app/server/data/Wednesday-workingHours.pcap_ISCX.csv'
]



all_top_features = pd.DataFrame()

for dataset in dataset_files:
    top_features = process_dataset(dataset, label_column='Label', n_top_features=10)
    all_top_features = pd.concat([all_top_features, top_features])

final_top_features = all_top_features.drop_duplicates(subset=['Feature']).sort_values(by='Importance', ascending=False)
final_top_features.to_csv('app/server/data/top_features_across_datasets.csv', index=False)

