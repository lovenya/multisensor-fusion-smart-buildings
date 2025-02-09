import numpy as np
import pandas as pd


def generate_light_data(num_days=7, occupancy_correlation=True, time_based=True):
    """Simulates light intensity with optional occupancy and time-of-day influence."""
    data = []
    start_time = pd.Timestamp("2023-01-01 00:00:00")
    
    for day in range(num_days):
        timestamps = [start_time + pd.Timedelta(minutes=i) for i in range(1440)]
        light_levels = []
        
        for i in range(1440):
            hour = (timestamps[i].hour + timestamps[i].minute / 60)  # Convert to float hour
            base_light = 50 if hour < 6 or hour > 18 else 300  # Night vs. Day

            if occupancy_correlation and np.random.rand() < 0.5:
                base_light += 100  # Lights ON if occupied

            light_levels.append(base_light + np.random.uniform(-10, 10))  # Small variations

        df = pd.DataFrame({"Timestamp": timestamps, "Light_Intensity": light_levels})
        data.append(df)
        start_time += pd.Timedelta(days=1)
    
    return data

light_data = generate_light_data()
light_data[0].to_csv("synthetic_light_data.csv", index=False)
print("Light data saved!")
