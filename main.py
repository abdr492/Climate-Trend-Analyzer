from src.data_loader import load_data
from src.preprocessing import preprocess
from src.analysis import plot_temperature_trend, plot_anomalies
from src.anomaly import detect_anomalies
from src.forecasting import forecast_temperature, plot_forecast

# Load data
df = load_data("data/raw/climate_large.csv")

# Preprocess
df = preprocess(df)

# Detect anomalies
df = detect_anomalies(df)

# Forecast
model, future_years, predictions = forecast_temperature(df)

print("Future Predictions:")
for year, temp in zip(future_years, predictions):
    print(year[0], "→", round(temp, 2), "°C")

# Plot graphs
plot_temperature_trend(df)
plot_anomalies(df)
plot_forecast(df, future_years, predictions)