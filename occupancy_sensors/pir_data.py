import numpy as np
import pandas as pd


def generate_pir_data(num_days=7, num_samples_per_day=1440):
    """Simulate PIR sensor motion detection with timestamps."""
    data = []
    start_time = pd.Timestamp("2025-01-01 00:00:00")

    for day in range(num_days):
        timestamps = [start_time + pd.Timedelta(minutes=i) for i in range(num_samples_per_day)]
        motion_detected = np.random.choice([0, 1], size=num_samples_per_day, p=[0.7, 0.3])
        df = pd.DataFrame({"Timestamp": timestamps, "Motion_Detected": motion_detected})
        data.append(df)
        start_time += pd.Timedelta(days=1)

    return data

pir_data = generate_pir_data()
pir_data[0].to_csv("synthetic_pir_data.csv", index=False)
