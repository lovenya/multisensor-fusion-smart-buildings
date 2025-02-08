import numpy as np
import pandas as pd


def generate_integrated_sensor_data(num_days=7, num_samples_per_day=1440):
    """Simulate integrated sensor data with timestamps."""
    data = []
    start_time = pd.Timestamp("2025-01-01 00:00:00")

    for day in range(num_days):
        timestamps = [start_time + pd.Timedelta(minutes=i) for i in range(num_samples_per_day)]

        occupancy = np.random.choice([0, 1], size=num_samples_per_day, p=[0.7, 0.3])

        pir_data = (occupancy & np.random.choice([0, 1], size=num_samples_per_day, p=[0.6, 0.4]))
        co2_data = [400]
        for i in range(1, num_samples_per_day):
            co2_data.append(co2_data[-1] + (occupancy[i] * np.random.uniform(5, 15)) - np.random.uniform(1, 5))
        co2_data = np.clip(co2_data, 400, 1000)

        wifi_devices = np.where(occupancy == 1, np.random.poisson(3, num_samples_per_day), 0)
        radio_rssi = np.where(pir_data == 1, np.random.uniform(-70, -50, num_samples_per_day), np.random.uniform(-90, -70, num_samples_per_day))
        door_state = np.random.choice([0, 1], size=num_samples_per_day, p=[0.9, 0.1])
        image_people_count = np.where(occupancy == 1, np.random.poisson(2, num_samples_per_day), 0)

        day_data = pd.DataFrame({
            "Timestamp": timestamps,
            "Occupancy": occupancy,
            "PIR": pir_data,
            "CO2_Level": co2_data,
            "WiFi_Devices": wifi_devices,
            "Radio_RSSI": radio_rssi,
            "Door_Open": door_state,
            "Image_People_Count": image_people_count
        })
        data.append(day_data)
        start_time += pd.Timedelta(days=1)

    return data

integrated_data = generate_integrated_sensor_data()
integrated_data[0].to_csv("integrated_sensor_data.csv", index=False)


