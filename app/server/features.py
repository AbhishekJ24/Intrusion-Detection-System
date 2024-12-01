import numpy as np

def extract_features(packets):  
    features = []
    for packet in packets:
        try:
            features.append([
                len(packet),  # Packet length
                int(packet.highest_layer == "TCP"),  # TCP packet
                int(packet.highest_layer == "UDP"),  # UDP packet
                int(packet.highest_layer == "ICMP"), # ICMP packet
                float(packet.sniff_timestamp),      # Timestamp
            ])
        except Exception as e:
            print(f"Error extracting features: {e}")
    return np.array(features)
