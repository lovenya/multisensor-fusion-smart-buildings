import numpy as np
import pandas as pd


def generate_threshold_data(num_days=7, num_samples_per_day=1440):
    """Simulate threshold/mechanical sensor data."""
    data = []
    for day in range(num_days):
        door_state = np.random.choice([0, 1], size=num_samples_per_day, p=[0.8, 0.2])  # 20% door open
        data.append(pd.DataFrame({"Door_Open": door_state}))
    return data

# Save simulated data
threshold_data = generate_threshold_data()
threshold_data[0].to_csv("synthetic_threshold_data.csv", index=False)
