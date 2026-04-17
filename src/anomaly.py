def detect_anomalies(df):
    mean_temp = df['Temperature'].mean()
    std_temp = df['Temperature'].std()

    # 🔥 Make it more sensitive
    upper_limit = mean_temp + 1 * std_temp
    lower_limit = mean_temp - 1 * std_temp

    df['Anomaly'] = ((df['Temperature'] > upper_limit) |
                     (df['Temperature'] < lower_limit))

    return df