import numpy as np
import pandas as pd

import numpy as np
import pandas as pd


def generate_wifi_data(num_days=7, num_samples_per_day=1440, min_rssi=-90, max_rssi=-30):
    """Simulate WiFi RSSI data and connected device counts with timestamps."""
    data = []
    start_time = pd.Timestamp("2025-01-01 00:00:00")

    for day in range(num_days):
        timestamps = [start_time + pd.Timedelta(minutes=i) for i in range(num_samples_per_day)]
        rssi_values = np.random.uniform(min_rssi, max_rssi, size=num_samples_per_day)
        connected_devices = np.random.poisson(lam=3, size=num_samples_per_day)  # Avg 3 devices
        df = pd.DataFrame({"Timestamp": timestamps, "RSSI": rssi_values, "Connected_Devices": connected_devices})
        data.append(df)
        start_time += pd.Timedelta(days=1)

    return data

wifi_data = generate_wifi_data()
wifi_data[0].to_csv("synthetic_wifi_data.csv", index=False)
