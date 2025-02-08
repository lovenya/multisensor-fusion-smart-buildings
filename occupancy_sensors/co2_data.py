import numpy as np
import pandas as pd


def generate_co2_data(num_days=7, num_samples_per_day=1440, baseline=400, max_co2=1000):
    """Simulate CO2 levels with timestamps."""
    data = []
    start_time = pd.Timestamp("2025-01-01 00:00:00")

    for day in range(num_days):
        timestamps = [start_time + pd.Timedelta(minutes=i) for i in range(num_samples_per_day)]
        co2_levels = [baseline]  # Start at baseline
        for i in range(1, num_samples_per_day):
            co2_levels.append(co2_levels[-1] + np.random.uniform(0, 5) * (np.random.choice([0, 1], p=[0.7, 0.3])))

        df = pd.DataFrame({"Timestamp": timestamps, "CO2_Level": co2_levels})
        data.append(df)
        start_time += pd.Timedelta(days=1)

    return data

co2_data = generate_co2_data()
co2_data[0].to_csv("synthetic_co2_data.csv", index=False)
