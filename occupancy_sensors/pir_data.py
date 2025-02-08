import numpy as np
import pandas as pd


def generate_pir_data(num_days=7, num_samples_per_day=1440):
    """Simulate PIR sensor data."""
    data = []
    for day in range(num_days):
        motion_detected = np.random.choice([0, 1], size=num_samples_per_day, p=[0.7, 0.3])  # 30% chance of motion
        false_positives = np.random.choice([0, 1], size=num_samples_per_day, p=[0.98, 0.02])  # 2% chance of false positive
        motion_detected = np.maximum(motion_detected, false_positives)
        data.append(pd.DataFrame({"Motion_Detected": motion_detected}))
    return data

# Save simulated data
pir_data = generate_pir_data()
pir_data[0].to_csv("synthetic_pir_data.csv", index=False)
