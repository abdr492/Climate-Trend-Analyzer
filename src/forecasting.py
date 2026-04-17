import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def forecast_temperature(df):
    import numpy as np
    from sklearn.linear_model import LinearRegression

    # Create time index
    df['Time_Index'] = range(len(df))

    X = df[['Time_Index']]
    y = df['Temperature']

    model = LinearRegression()
    model.fit(X, y)

    # Future indices
    future_index = np.array([[len(df)], [len(df)+1], [len(df)+2], [len(df)+3]])

    predictions = model.predict(future_index)

    return model, future_index, predictions


def plot_forecast(df, future_index, predictions):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10,5))

    # Historical
    plt.plot(df['Time_Index'], df['Temperature'],
             label='Historical', marker='o')

    # Future
    plt.plot(future_index, predictions,
             label='Forecast', linestyle='--', marker='x', color='red')

    plt.title("Temperature Forecast")
    plt.xlabel("Time Index")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)

    plt.savefig("outputs/graphs/forecast.png")

    import streamlit as st
    st.pyplot(plt)
    plt.pause(5)
    plt.close()