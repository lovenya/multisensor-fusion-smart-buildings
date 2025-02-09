import numpy as np
import pandas as pd


def generate_pm_data(num_days=7, pollution_effect=True):
    """Simulates particulate matter (PM2.5) data per minute with pollution impact."""
    data = []
    start_time = pd.Timestamp("2023-01-01 00:00:00")

    for day in range(num_days):
        timestamps = [start_time + pd.Timedelta(minutes=i) for i in range(1440)]
        pm_levels = []
        
        for i in range(1440):
            base_pm = np.random.uniform(5, 50)  # Indoor baseline PM level
            if pollution_effect:
                base_pm += np.random.uniform(0, 30)  # Pollution variation
            pm_levels.append(base_pm)

        df = pd.DataFrame({"Timestamp": timestamps, "PM2.5_Level": pm_levels})
        data.append(df)
        start_time += pd.Timedelta(days=1)

    return data

pm_data = generate_pm_data()
pm_data[0].to_csv("synthetic_pm_data.csv", index=False)
print("Particulate Matter data saved!")
