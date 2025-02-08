import numpy as np
import pandas as pd

def generate_radio_data(num_days=7, num_samples_per_day=1440, min_rssi=-100, max_rssi=-50):
    """Simulate radio-based occupancy data."""
    data = []
    for day in range(num_days):
        rssi_values = np.random.uniform(min_rssi, max_rssi, size=num_samples_per_day)
        occupancy = (rssi_values > -70).astype(int)  # Threshold for occupancy
        data.append(pd.DataFrame({"RSSI": rssi_values, "Occupancy": occupancy}))
    return data

# Save simulated data
radio_data = generate_radio_data()
radio_data[0].to_csv("synthetic_radio_data.csv", index=False)
