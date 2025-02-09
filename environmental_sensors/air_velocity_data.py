import numpy as np
import pandas as pd


def generate_air_velocity_data(num_days=7, weather_dependency=True):
    """Simulates air velocity data per minute with optional weather influence."""
    data = []
    start_time = pd.Timestamp("2023-01-01 00:00:00")
    
    for day in range(num_days):
        timestamps = [start_time + pd.Timedelta(minutes=i) for i in range(1440)]
        air_velocity = []
        
        for i in range(1440):
            base_velocity = np.random.uniform(0.1, 1.0)  # Indoor Airflow Range
            if weather_dependency:
                base_velocity += np.random.uniform(0, 1.0)  # Weather-affected variations
            air_velocity.append(base_velocity)

        df = pd.DataFrame({"Timestamp": timestamps, "Air_Velocity": air_velocity})
        data.append(df)
        start_time += pd.Timedelta(days=1)
    
    return data

air_velocity_data = generate_air_velocity_data()
air_velocity_data[0].to_csv("synthetic_air_velocity_data.csv", index=False)
print("Air velocity data saved!")
