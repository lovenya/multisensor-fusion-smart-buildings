import numpy as np
import pandas as pd


def generate_co2_data(num_days=7, num_samples_per_day=1440, baseline=400, max_co2=1000):
    """Simulate CO2 levels for occupancy detection."""
    data = []
    for day in range(num_days):
        co2_levels = np.random.uniform(baseline, max_co2, size=num_samples_per_day)
        occupancy = (co2_levels > 500).astype(int)  # Threshold for human presence
        data.append(pd.DataFrame({"CO2_Level": co2_levels, "Occupancy": occupancy}))
    return data

# Save simulated data
co2_data = generate_co2_data()
co2_data[0].to_csv("synthetic_co2_data.csv", index=False)
