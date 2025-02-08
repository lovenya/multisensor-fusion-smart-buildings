import numpy as np
import pandas as pd


def generate_radio_data(num_days=7, num_samples_per_day=1440, min_rssi=-100, max_rssi=-50):
    """Simulate radio-based occupancy detection with timestamps."""
    data = []
    start_time = pd.Timestamp("2025-01-01 00:00:00")

    for day in range(num_days):
        timestamps = [start_time + pd.Timedelta(minutes=i) for i in range(num_samples_per_day)]
        rssi_values = np.random.uniform(min_rssi, max_rssi, size=num_samples_per_day)
        occupancy = (rssi_values > -70).astype(int)  # Threshold for occupancy
        df = pd.DataFrame({"Timestamp": timestamps, "RSSI": rssi_values, "Occupancy": occupancy})
        data.append(df)
        start_time += pd.Timedelta(days=1)

    return data


radio_data = generate_radio_data()
radio_data[0].to_csv("synthetic_radio_data.csv", index=False)
