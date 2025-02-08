import numpy as np
import pandas as pd

def generate_wifi_data(num_days=7, num_samples_per_day=1440, min_rssi=-90, max_rssi=-30):
    """Simulate WiFi RSSI data and connected device counts."""
    data = []
    for day in range(num_days):
        rssi_values = np.random.uniform(min_rssi, max_rssi, size=num_samples_per_day)
        connected_devices = np.random.poisson(lam=3, size=num_samples_per_day)  # Avg 3 devices
        data.append(pd.DataFrame({"RSSI": rssi_values, "Connected_Devices": connected_devices}))
    return data

# Save simulated data
wifi_data = generate_wifi_data()
wifi_data[0].to_csv("synthetic_wifi_data.csv", index=False)
