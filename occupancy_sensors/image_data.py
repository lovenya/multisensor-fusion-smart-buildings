import numpy as np
import pandas as pd


def generate_image_data(num_days=7, num_samples_per_day=1440):
    """Simulate image-based occupancy detection with timestamps."""
    data = []
    start_time = pd.Timestamp("2025-01-01 00:00:00")

    for day in range(num_days):
        timestamps = [start_time + pd.Timedelta(minutes=i) for i in range(num_samples_per_day)]
        people_count = np.random.poisson(lam=5, size=num_samples_per_day)  # Avg 5 people
        confidence_scores = np.random.uniform(0.5, 1.0, size=num_samples_per_day)  # Confidence > 50%
        df = pd.DataFrame({"Timestamp": timestamps, "People_Count": people_count, "Confidence": confidence_scores})
        data.append(df)
        start_time += pd.Timedelta(days=1)

    return data


image_data = generate_image_data()
image_data[0].to_csv("synthetic_image_data.csv", index=False)
