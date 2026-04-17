import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stMetric {
        background-color: #1c1f26;
        padding: 15px;
        border-radius: 10px;
    }
    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

from src.data_loader import load_data
from src.preprocessing import preprocess
from src.analysis import plot_temperature_trend, plot_anomalies
from src.anomaly import detect_anomalies
from src.forecasting import forecast_temperature
from src.lstm_model import train_lstm, predict_future

st.set_page_config(page_title="Climate Analyzer", layout="wide")


# 🔹 Sidebar
st.sidebar.header("⚙️ Controls")

dataset_option = st.sidebar.selectbox(
    "Choose Dataset",
    ["Large Dataset", "Small Dataset"]
)

st.sidebar.title("📊 Navigation")

section = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "Data Analysis",
        "Forecasting",
        "Advanced Analytics"
    ]
)
# Load dataset
if dataset_option == "Large Dataset":
    df = load_data("data/raw/climate_large.csv")
else:
    df = load_data("data/raw/climate.csv")

df = preprocess(df)
df = detect_anomalies(df)

# =========================
# 📊 OVERVIEW
# =========================
if section == "Overview":

    st.title("🌍 Climate Trend Analyzer Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("🌡 Avg Temp", f"{df['Temperature'].mean():.2f} °C")
    col2.metric("🔥 Max Temp", f"{df['Temperature'].max():.2f} °C")
    col3.metric("⚠️ Anomalies", int(df['Anomaly'].sum()))

    st.markdown("###")

    st.subheader("📊 Dataset Preview")
    st.dataframe(df.head().style.background_gradient(cmap='Blues'))


# =========================
# 📊 DATA ANALYSIS
# =========================
elif section == "Data Analysis":

    st.markdown("## 📊 Data Analysis")

    # Trend + Anomaly
    col1, col2 = st.columns(2)

    with col1:
        fig = px.line(df, x='Date', y='Temperature', title="Temperature Trend")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig2 = px.line(df, x='Date', y='Temperature', title="Anomaly Detection")
        anomalies = df[df['Anomaly'] == True]

        fig2.add_scatter(
            x=anomalies['Date'],
            y=anomalies['Temperature'],
            mode='markers',
            marker=dict(color='red', size=8),
            name='Anomaly'
        )

        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("###")

    # Moving Average
    df['Moving_Avg'] = df['Temperature'].rolling(window=12).mean()

    fig_ma = px.line(
        df,
        x='Date',
        y=['Temperature', 'Moving_Avg'],
        title="Smoothed Trend"
    )

    st.plotly_chart(fig_ma, use_container_width=True)

    st.markdown("###")

    # Donut + Bar
    col3, col4 = st.columns(2)

    with col3:
        anomaly_counts = df['Anomaly'].value_counts().reset_index()
        anomaly_counts.columns = ['Anomaly', 'Count']

        fig_pie = px.pie(anomaly_counts, names='Anomaly', values='Count', hole=0.5)
        st.plotly_chart(fig_pie, use_container_width=True)

    with col4:
        monthly_avg = df.groupby('Month')['Temperature'].mean().reset_index()

        fig_bar = px.bar(monthly_avg, x='Month', y='Temperature', color='Temperature')
        st.plotly_chart(fig_bar, use_container_width=True)


# =========================
# 🔮 FORECASTING
# =========================
elif section == "Forecasting":

    st.markdown("## 🔮 Forecasting Models")

    model, future_index, predictions = forecast_temperature(df)

    future_df = pd.DataFrame({
        "Index": future_index.flatten(),
        "Temperature": predictions
    })

    fig_forecast = px.line(
        df,
        x='Date',
        y='Temperature',
        title="Actual vs Forecast"
    )

    fig_forecast.add_scatter(
        x=future_df['Index'],
        y=future_df['Temperature'],
        mode='lines+markers',
        name='Forecast',
        line=dict(color='green')
    )

    st.plotly_chart(fig_forecast, use_container_width=True,key="forecast_chart")

    st.markdown("###")

    # LSTM
    model_lstm, scaler = train_lstm(df)
    lstm_preds = predict_future(df, model_lstm, scaler).flatten()

    future_index_lstm = list(range(len(df), len(df) + len(lstm_preds)))

    fig_lstm = px.line(
        df,
        x='Date',
        y='Temperature',
        title="LSTM Prediction"
    )

    fig_lstm.add_scatter(
        x=future_index_lstm,
        y=lstm_preds,
        mode='lines+markers',
        name='LSTM Forecast',
        line=dict(dash='dash', color='orange')
    )

    st.plotly_chart(fig_lstm, use_container_width=True, key="lstm_chart")


# =========================
# 📊 ADVANCED ANALYTICS
# =========================
elif section == "Advanced Analytics":

    st.markdown("## 📊 Advanced Analytics")

    # Heatmap
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if len(numeric_cols) >= 2:
        corr = df[numeric_cols].corr()

        fig_heatmap = px.imshow(
            corr,
            text_auto=True,
            color_continuous_scale='RdBu_r'
        )

        st.plotly_chart(fig_heatmap, use_container_width=True, key="heatmap")

    else:
        st.info("Limited features - showing trend instead")
        fig_temp = px.line(df, x='Date', y='Temperature')
        st.plotly_chart(fig_temp, use_container_width=True, key="temp_fallback_chart")


    st.markdown("###")

    # Scatter / fallback
    numeric_cols = [col for col in numeric_cols if col != 'Temperature']

    if len(numeric_cols) >= 1:
        fig_scatter = px.scatter(df, x=numeric_cols[0], y='Temperature')
        st.plotly_chart(fig_scatter, use_container_width=True, key="scatter")
    else:
        fig_time = px.line(df, x='Date', y='Temperature')
        st.plotly_chart(fig_time, use_container_width=True, key="time_fallback")
