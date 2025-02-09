import numpy as np
import pandas as pd


def generate_voc_data(num_days=7, occupancy_correlation=True):
    """Simulates volatile organic compound (VOC) levels with occupancy influence."""
    data = []
    start_time = pd.Timestamp("2023-01-01 00:00:00")

    for day in range(num_days):
        timestamps = [start_time + pd.Timedelta(minutes=i) for i in range(1440)]
        voc_levels = []

        for i in range(1440):
            base_voc = np.random.uniform(100, 500)  # Normal VOC range
            if occupancy_correlation:
                base_voc += np.random.uniform(50, 200)  # Activities increase VOC
            voc_levels.append(base_voc)

        df = pd.DataFrame({"Timestamp": timestamps, "VOC_Level": voc_levels})
        data.append(df)
        start_time += pd.Timedelta(days=1)

    return data

voc_data = generate_voc_data()
voc_data[0].to_csv("synthetic_voc_data.csv", index=False)
print("VOC data saved!")
