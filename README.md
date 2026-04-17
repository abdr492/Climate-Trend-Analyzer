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

Raw Climate Data  
        │  
        ▼  
Data Loading  
        │  
        ▼  
Preprocessing (Date parsing, feature creation)  
        │  
        ▼  
Anomaly Detection (Z-score method)  
        │  
        ▼  
Forecasting Models (Linear Regression + LSTM)  
        │  
        ▼  
Visualization + Streamlit Dashboard  

---

## 📁 Folder Structure

Climate-Trend-Analyzer/
│
├── app/
│   └── app.py
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── anomaly.py
│   ├── forecasting.py
│   ├── lstm_model.py
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

Step 1: Clone Repository  
git clone https://github.com/abdr492/Climate-Trend-Analyzer.git  
cd Climate-Trend-Analyzer  

Step 2: Create Virtual Environment  
python -m venv venv  
venv\Scripts\activate  

Step 3: Install Dependencies  
pip install -r requirements.txt  

Step 4: Run Dashboard  
streamlit run app/app.py  

---

## 📊 Dashboard Features

- KPI Metrics (Avg Temp, Max Temp, Anomalies)  
- Temperature Trend Analysis  
- Anomaly Detection Visualization  
- Moving Average Smoothing  
- Monthly Analysis (Bar Charts)  
- Distribution Analysis (Donut Chart)  
- Feature Relationship & Correlation  
- Forecasting (ML Model)  
- Deep Learning Forecast (LSTM)  
- Multi-page Navigation UI  

---

## 📊 Results

Forecasting  
- ML model captures general trend patterns  
- LSTM captures temporal dependencies  

Anomaly Detection  
- Successfully identifies extreme temperature spikes  

Visualization  
- Interactive charts improve interpretability  
- Multi-page UI enhances user experience  

---

## 🚧 Challenges & Solutions

| Challenge | Solution |
|----------|--------|
| Missing features (CO₂, rainfall) | Dynamic feature handling |
| Small dataset issues | Fallback visualizations |
| Duplicate charts error | Unique Streamlit keys |
| UI clutter | Sidebar navigation |

---

## 🔮 Future Improvements

- Add CO₂ and rainfall datasets  
- Integrate real-time climate APIs  
- Add geographic map visualization  
- Deploy dashboard online (Streamlit Cloud)  
- Improve LSTM accuracy with larger dataset  

---

## 🎓 Learning Outcomes

- Time-series data analysis  
- Anomaly detection techniques  
- ML vs Deep Learning comparison  
- Dashboard development using Streamlit  
- Handling real-world data limitations  

---

## 👨‍💻 Author

Abdul Rahman Anas  
B.E CSE (AI & ML)  
Lords Institute of Engineering & Technology  

---

## ⭐ If you found this useful, consider starring the repository!
