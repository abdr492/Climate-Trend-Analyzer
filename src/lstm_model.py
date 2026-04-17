import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def prepare_data(df):
    data = df['Temperature'].values.reshape(-1,1)

    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)

    X, y = [], []

    for i in range(5, len(data_scaled)):
        X.append(data_scaled[i-5:i])
        y.append(data_scaled[i])

    X, y = np.array(X), np.array(y)

    return X, y, scaler


def train_lstm(df):
    X, y, scaler = prepare_data(df)

    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(X.shape[1], 1)))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mse')

    model.fit(X, y, epochs=20, verbose=0)

    return model, scaler


def predict_future(df, model, scaler):
    data = df['Temperature'].values.reshape(-1,1)
    data_scaled = scaler.transform(data)

    last_sequence = data_scaled[-5:]
    predictions = []

    for _ in range(5):
        pred = model.predict(last_sequence.reshape(1,5,1), verbose=0)
        predictions.append(pred[0][0])

        last_sequence = np.append(last_sequence[1:], pred, axis=0)

    predictions = scaler.inverse_transform(np.array(predictions).reshape(-1,1))

    return predictions