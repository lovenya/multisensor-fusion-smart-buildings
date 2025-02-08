import numpy as np
import pandas as pd


def generate_threshold_data(num_days=7, num_samples_per_day=1440):
    """Simulate threshold/mechanical sensor data with timestamps."""
    data = []
    start_time = pd.Timestamp("2025-01-01 00:00:00")

    for day in range(num_days):
        timestamps = [start_time + pd.Timedelta(minutes=i) for i in range(num_samples_per_day)]
        door_state = np.random.choice([0, 1], size=num_samples_per_day, p=[0.8, 0.2])  # 20% door open
        df = pd.DataFrame({"Timestamp": timestamps, "Door_Open": door_state})
        data.append(df)
        start_time += pd.Timedelta(days=1)

    return data


threshold_data = generate_threshold_data()
threshold_data[0].to_csv("synthetic_threshold_data.csv", index=False)
