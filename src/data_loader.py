import pandas as pd
import numpy as np
import requests
import os

def fetch_sample_climate_data():
    """
    Fetches sample global temperature anomaly data.
    In a real scenario, this would call a NOAA or NASA API.
    Here we generate synthetic data representing global temperature trends.
    """
    years = np.arange(1880, 2025)
    # Simulate a rising trend with some noise
    anomalies = 0.005 * (years - 1880) + np.random.normal(0, 0.1, len(years))
    
    df = pd.DataFrame({
        'Year': years,
        'Anomaly': anomalies
    })
    return df

def save_data(df, filename='data/global_temp_anomalies.csv'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    data = fetch_sample_climate_data()
    save_data(data)
