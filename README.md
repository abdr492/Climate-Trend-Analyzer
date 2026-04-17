# 🌍 Climate Trend Analyzer Dashboard
Industry-Level Climate Analytics & Forecasting System  
Built with Python, Machine Learning, Deep Learning, and Streamlit  

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-yellow?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical-blue?logo=numpy)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikit-learn)
![TensorFlow](https://img.shields.io/badge/TensorFlow-LSTM-orange?logo=tensorflow)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-purple?logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Project Overview

This project simulates a production-level climate analytics system used for:

- Monitoring temperature trends over time  
- Detecting anomalies in climate patterns  
- Forecasting future temperature using ML & Deep Learning  
- Visualizing insights through an interactive dashboard  

The system is built on time-series climate data and demonstrates how data science can be applied to environmental monitoring and prediction.

---

## 🌍 Real-World Problem Solved

| Problem | Impact | Solution |
|--------|-------|--------|
| Unpredictable temperature spikes | Environmental risk | Anomaly Detection |
| Lack of future climate insights | Poor planning | ML + LSTM Forecasting |
| Raw data complexity | Hard to interpret | Interactive Dashboard |
| No trend visibility | Weak analysis | Time-Series Visualization |

---

## 📊 Key Insights Generated

- Average Temperature Trends over time  
- Seasonal variations across months  
- Detection of extreme anomalies  
- Smoothed long-term patterns (Moving Average)  
- Forecasted future temperature trends  

---

## 🧠 Tech Stack

| Component | Technology |
|----------|-----------|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly, Matplotlib |
| Machine Learning | Scikit-learn |
| Deep Learning | TensorFlow / Keras (LSTM) |
| Dashboard | Streamlit |

---

## 🏗️ System Architecture

```text
Raw Climate Data
        │
        ▼
┌─────────────────────┐
│   Data Loading      │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│   Preprocessing     │  ← Date parsing, feature creation
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  Anomaly Detection  │  ← Z-score method
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Forecasting Models  │  ← Linear Regression
│ + LSTM Model        │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Visualization       │  ← Plotly charts
│ + Streamlit UI      │
└─────────────────────┘

---

## 📁 Folder Structure

Climate-Trend-Analyzer/
│
├── app/
│   └── app.py                  ← Streamlit dashboard
│
├── src/
│   ├── data_loader.py          ← Load dataset
│   ├── preprocessing.py        ← Data cleaning & feature creation
│   ├── anomaly.py              ← Anomaly detection logic
│   ├── forecasting.py          ← ML forecasting model
│   ├── lstm_model.py           ← Deep learning model
│
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│   ├── graphs/
│   └── reports/
│
├── requirements.txt
├── README.md
├── .gitignore
---

## ⚙️ Installation & Setup

### 📥 Step 1: Clone Repository
git clone https://github.com/abdr492/Climate-Trend-Analyzer.git  
cd Climate-Trend-Analyzer  

### 🧪 Step 2: Create Virtual Environment
python -m venv venv  
venv\Scripts\activate  

### 📦 Step 3: Install Dependencies
pip install -r requirements.txt  

### ▶️ Step 4: Run Dashboard
streamlit run app/app.py  

---

## 📊 Dashboard Features

### 📌 Core Features
- KPI Metrics (Avg Temp, Max Temp, Anomalies)  
- Temperature Trend Visualization  
- Anomaly Detection Graph  

### 📊 Advanced Features
- Moving Average Trend  
- Monthly Analysis (Bar Chart)  
- Distribution (Donut Chart)  
- Correlation Heatmap  
- Feature Relationship Analysis  

### 🔮 Forecasting
- Machine Learning Forecast  
- LSTM Deep Learning Forecast  

---

## 📊 Results

### 📈 Forecasting Performance
- ML captures general trends  
- LSTM captures time dependencies  

### ⚠️ Anomaly Detection
- Detects extreme temperature spikes  

### 📊 Visualization Impact
- Improves data interpretation  
- Enhances user experience  

---

## 🚧 Challenges & Solutions

### 🛠 Issues Faced
| Challenge | Solution |
|----------|--------|
| Missing features | Dynamic feature selection |
| Small dataset | Fallback graphs |
| Duplicate charts | Unique Streamlit keys |
| UI clutter | Sidebar navigation |

---

## 🔮 Future Improvements

### 🚀 Enhancements
- Add CO₂ and rainfall data  
- Integrate real-time APIs  
- Add map-based visualization  
- Deploy dashboard online  
- Improve LSTM accuracy  

---

## 🎓 Learning Outcomes

### 🧠 Skills Gained
- Time-series analysis  
- Anomaly detection techniques  
- ML vs Deep Learning understanding  
- Streamlit dashboard development  
- Handling real-world data issues  

---

## 👨‍💻 Author

### 👤 Abdul Rahman Anas  
B.E CSE (AI & ML)  
Lords Institute of Engineering & Technology  

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
