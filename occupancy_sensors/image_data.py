import numpy as np
import pandas as pd

def generate_image_data(num_days=7, num_samples_per_day=1440):
    """Simulate image-based occupancy data."""
    data = []
    for day in range(num_days):
        people_count = np.random.poisson(lam=5, size=num_samples_per_day)  # Avg 5 people
        confidence_scores = np.random.uniform(0.5, 1.0, size=num_samples_per_day)  # Confidence > 50%
        data.append(pd.DataFrame({"People_Count": people_count, "Confidence": confidence_scores}))
    return data

# Save simulated data
image_data = generate_image_data()
image_data[0].to_csv("synthetic_image_data.csv", index=False)
