import pandas as pd
import numpy as np

def generate_climate_data():
    # Generate 10 years monthly data
    dates = pd.date_range(start="2010-01-01", end="2020-12-01", freq='MS')

    # Base temperature trend
    base_temp = 25

    temperatures = []

    for i in range(len(dates)):
        # Trend increase over time
        trend = i * 0.05

        # Seasonal variation (sin wave)
        seasonal = 5 * np.sin(2 * np.pi * (i % 12) / 12)

        # Random noise
        noise = np.random.normal(0, 1)

        temp = base_temp + trend + seasonal + noise

        temperatures.append(temp)

    df = pd.DataFrame({
        "Date": dates,
        "Temperature": temperatures
    })

    # Add some anomalies
    df.loc[50, 'Temperature'] += 10
    df.loc[100, 'Temperature'] -= 8

    df.to_csv("data/raw/climate_large.csv", index=False)

    print("Dataset generated successfully!")

if __name__ == "__main__":
    generate_climate_data()