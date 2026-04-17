import pandas as pd

def preprocess(df):
    # Convert Date column
    df['Date'] = pd.to_datetime(df['Date'])

    # Sort data
    df = df.sort_values('Date')

    # Handle missing values
    df['Temperature'] = df['Temperature'].fillna(df['Temperature'].mean())

    # Extract Year and Month
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month

    return df