import numpy as np
import pandas as pd


def generate_temperature_humidity_data(num_days=7, external_temp=True):
    """Simulates temperature and humidity with optional external temperature."""
    data = []
    start_time = pd.Timestamp("2023-01-01 00:00:00")

    for day in range(num_days):
        timestamps = [start_time + pd.Timedelta(minutes=i) for i in range(1440)]
        temp_levels = []
        humidity_levels = []

        for i in range(1440):
            base_temp = np.random.uniform(18, 24)  # Indoor range
            base_humidity = np.random.uniform(30, 50)  # Humidity %

            if external_temp:
                base_temp += np.random.uniform(-5, 5)  # External temp fluctuation

            temp_levels.append(base_temp)
            humidity_levels.append(base_humidity)

        df = pd.DataFrame({"Timestamp": timestamps, "Temperature": temp_levels, "Humidity": humidity_levels})
        data.append(df)
        start_time += pd.Timedelta(days=1)

    return data

temp_humidity_data = generate_temperature_humidity_data()
temp_humidity_data[0].to_csv("synthetic_temp_humidity_data.csv", index=False)
print("Temperature & Humidity data saved!")
