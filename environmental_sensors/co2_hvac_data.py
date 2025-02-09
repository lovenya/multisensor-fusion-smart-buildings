import numpy as np
import pandas as pd
import argparse

def generate_co2_data(num_days=7, occupancy_correlation=True, hvac_enabled=True):
    """Simulates CO2 levels per minute with optional occupancy and HVAC influence."""
    data = []
    start_time = pd.Timestamp("2023-01-01 00:00:00")
    
    for day in range(num_days):
        timestamps = [start_time + pd.Timedelta(minutes=i) for i in range(1440)]
        co2_levels = [400]  # Baseline CO2
        for i in range(1, 1440):
            change = np.random.uniform(0, 5)
            if occupancy_correlation:
                change += np.random.choice([0, 10], p=[0.7, 0.3])  # More CO2 when occupied
            if hvac_enabled and np.random.rand() < 0.3:
                change -= np.random.uniform(5, 15)  # Ventilation effect
            co2_levels.append(np.clip(co2_levels[-1] + change, 400, 1000))
        
        df = pd.DataFrame({"Timestamp": timestamps, "CO2_Level": co2_levels})
        data.append(df)
        start_time += pd.Timedelta(days=1)
    
    return data

co2_data = generate_co2_data()
co2_data[0].to_csv("synthetic_co2_data.csv", index=False)
print("CO2 data saved!")
