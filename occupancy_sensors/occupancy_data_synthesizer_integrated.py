import numpy as np
import pandas as pd


def generate_integrated_sensor_data(num_days=7, num_samples_per_day=1440):
    """Simulate integrated sensor data."""
    data = []
    for day in range(num_days):
        # Initialize occupancy state
        occupancy = np.random.choice(
            [0, 1], size=num_samples_per_day, p=[0.7, 0.3]
        )  # 30% occupancy

        # PIR sensor: Motion detected when occupied
        pir_data = occupancy & np.random.choice(
            [0, 1], size=num_samples_per_day, p=[0.6, 0.4]
        )

        # CO2: Gradual buildup when occupied
        co2_data = [400]  # Starting CO2 level
        for i in range(1, num_samples_per_day):
            co2_data.append(
                co2_data[-1]
                + (occupancy[i] * np.random.uniform(5, 15))
                - np.random.uniform(1, 5)
            )
        co2_data = np.clip(co2_data, 400, 1000)  # CO2 levels cap

        # WiFi: Number of connected devices increases with occupancy
        wifi_devices = np.where(
            occupancy == 1, np.random.poisson(3, num_samples_per_day), 0
        )

        # Radio: Signal disturbances increase with motion
        radio_rssi = np.where(
            pir_data == 1,
            np.random.uniform(-70, -50, num_samples_per_day),
            np.random.uniform(-90, -70, num_samples_per_day),
        )

        # Threshold sensor: Random door open/close events
        door_state = np.random.choice(
            [0, 1], size=num_samples_per_day, p=[0.9, 0.1]
        )  # 10% door open

        # Image-based: People count when occupied
        image_people_count = np.where(
            occupancy == 1, np.random.poisson(2, num_samples_per_day), 0
        )

        # Combine into a single dataframe
        day_data = pd.DataFrame(
            {
                "Occupancy": occupancy,
                "PIR": pir_data,
                "CO2_Level": co2_data,
                "WiFi_Devices": wifi_devices,
                "Radio_RSSI": radio_rssi,
                "Door_Open": door_state,
                "Image_People_Count": image_people_count,
            }
        )
        data.append(day_data)

    return data


# Generate and save integrated data
integrated_data = generate_integrated_sensor_data()
integrated_data[0].to_csv("integrated_sensor_data.csv", index=False)
