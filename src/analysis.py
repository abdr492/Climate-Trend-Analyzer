import matplotlib.pyplot as plt

# Function 1: Temperature Trend
def plot_temperature_trend(df):
    import matplotlib.pyplot as plt
    import streamlit as st

    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Temperature'], marker='o')

    plt.title("Climate Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)

    st.pyplot(plt)   # ✅ IMPORTANT


# Function 2: Anomaly Detection Plot
def plot_anomalies(df):
    import matplotlib.pyplot as plt
    import streamlit as st

    plt.figure(figsize=(10,5))

    plt.plot(df['Date'], df['Temperature'], label='Temperature', color='blue')

    anomalies = df[df['Anomaly'] == True]

    plt.scatter(
        anomalies['Date'],
        anomalies['Temperature'],
        color='red',
        s=150,
        label='Anomaly'
    )

    plt.title("Anomaly Detection in Temperature")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)

    st.pyplot(plt)   # ✅ IMPORTANT