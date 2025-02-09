import numpy as np
import pandas as pd
import argparse

def generate_environmental_data(num_days=7, scope="single_room", occupancy_correlation=True,
                                external_temp=True, hvac_enabled=True, weather_dependency=True):
    """Simulates environmental sensor data for a single room, multiple rooms, or entire building."""
    
    start_time = pd.Timestamp("2023-01-01 00:00:00")
    num_samples_per_day = 1440  # 1 sample per minute
    num_rooms = {"single_room": 1, "multiple_rooms": 5, "entire_building": 10}[scope]
    
    all_data = []
    
    for room_id in range(num_rooms):
        for day in range(num_days):
            timestamps = [start_time + pd.Timedelta(minutes=i) for i in range(num_samples_per_day)]
            
            # CO2 Levels
            co2_levels = [400]
            for i in range(1, num_samples_per_day):
                change = np.random.uniform(0, 5)
                if occupancy_correlation:
                    change += np.random.choice([0, 10], p=[0.7, 0.3])  # More CO2 when occupied
                if hvac_enabled and np.random.rand() < 0.3:
                    change -= np.random.uniform(5, 15)  # HVAC reduces CO2
                co2_levels.append(np.clip(co2_levels[-1] + change, 400, 1000))

            # Light Levels
            light_levels = []
            for i in range(num_samples_per_day):
                hour = (timestamps[i].hour + timestamps[i].minute / 60)
                base_light = 50 if hour < 6 or hour > 18 else 300  # Night vs. Day
                if occupancy_correlation and np.random.rand() < 0.5:
                    base_light += 100  # Lights ON if occupied
                light_levels.append(base_light + np.random.uniform(-10, 10))

            # Air Velocity
            air_velocity = [np.random.uniform(0.1, 1.0) + (np.random.uniform(0, 1.0) if weather_dependency else 0) 
                            for _ in range(num_samples_per_day)]

            # Particulate Matter (PM2.5)
            pm_levels = [np.random.uniform(5, 50) + (np.random.uniform(0, 30) if weather_dependency else 0)
                         for _ in range(num_samples_per_day)]

            # Temperature & Humidity
            temp_levels = []
            humidity_levels = []
            for i in range(num_samples_per_day):
                base_temp = np.random.uniform(18, 24)  # Indoor range
                base_humidity = np.random.uniform(30, 50)  # Humidity %
                if external_temp:
                    base_temp += np.random.uniform(-5, 5)  # Outdoor influence
                temp_levels.append(base_temp)
                humidity_levels.append(base_humidity)

            # VOC Levels
            voc_levels = []
            for i in range(num_samples_per_day):
                base_voc = np.random.uniform(100, 500)
                if occupancy_correlation:
                    base_voc += np.random.uniform(50, 200)  # Human activity increases VOC
                voc_levels.append(base_voc)

            # Create DataFrame
            df = pd.DataFrame({
                "Timestamp": timestamps,
                "Room_ID": f"Room_{room_id+1}" if num_rooms > 1 else "Room_1",
                "CO2_Level": co2_levels,
                "Light_Intensity": light_levels,
                "Air_Velocity": air_velocity,
                "PM2.5_Level": pm_levels,
                "Temperature": temp_levels,
                "Humidity": humidity_levels,
                "VOC_Level": voc_levels
            })

            all_data.append(df)
            start_time += pd.Timedelta(days=1)

    # Concatenate all room data
    final_data = pd.concat(all_data, ignore_index=True)
    
    # Save to CSV
    filename = f"synthetic_environmental_data_{scope}.csv"
    final_data.to_csv(filename, index=False)
    print(f"Environmental data saved to {filename}!")

# CLI Argument Parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate synthetic environmental sensor data.")
    parser.add_argument("--days", type=int, default=7, help="Number of days to generate data for.")
    parser.add_argument("--scope", type=str, choices=["single_room", "multiple_rooms", "entire_building"],
                        default="single_room", help="Choose between single room, multiple rooms, or entire building.")
    parser.add_argument("--occupancy_correlation", action="store_true", default=True,
                        help="Enable correlation with occupancy data.")
    parser.add_argument("--no_occupancy_correlation", dest="occupancy_correlation", action="store_false",
                        help="Disable correlation with occupancy data.")
    parser.add_argument("--external_temp", action="store_true", default=True, help="Include external temperature.")
    parser.add_argument("--no_external_temp", dest="external_temp", action="store_false",
                        help="Exclude external temperature.")
    parser.add_argument("--hvac_enabled", action="store_true", default=True, help="Enable HVAC for CO2 regulation.")
    parser.add_argument("--no_hvac", dest="hvac_enabled", action="store_false", help="Disable HVAC effect.")
    parser.add_argument("--weather_dependency", action="store_true", default=True, help="Link air velocity to weather.")
    parser.add_argument("--no_weather_dependency", dest="weather_dependency", action="store_false",
                        help="Do not link air velocity to weather.")

    args = parser.parse_args()

    # Run the function with CLI parameters
    generate_environmental_data(num_days=args.days, scope=args.scope, occupancy_correlation=args.occupancy_correlation,
                                external_temp=args.external_temp, hvac_enabled=args.hvac_enabled,
                                weather_dependency=args.weather_dependency)
