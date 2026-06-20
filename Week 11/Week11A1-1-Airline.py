import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from xgboost import XGBRegressor
from statsmodels.tsa.arima.model import ARIMA

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

# Fix random seeds for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# ==========================================
# 1. DATA UNDERSTANDING & PREPROCESSING
# ==========================================
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
df = pd.read_csv(url, parse_dates=['Month'])
df.columns = ['Month', 'Passengers']
df.set_index('Month', inplace=True)

# Log transformation to stabilize increasing variance (multiplicative seasonality)
df['Log_Passengers'] = np.log(df['Passengers'])

# ==========================================
# 2. FEATURE ENGINEERING (For ML/DL Models)
# ==========================================
def create_lag_features(data, lag=12):
    X, y = [], []
    for i in range(len(data) - lag):
        X.append(data[i:(i + lag)])
        y.append(data[i + lag])
    return np.array(X), np.array(y)

LAG_WINDOW = 12
series_data = df['Log_Passengers'].values
X, y = create_lag_features(series_data, LAG_WINDOW)

# Split into Train and Test sets (Last 24 months held out for evaluation)
TEST_SIZE = 24
train_idx = len(X) - TEST_SIZE

X_train, X_test = X[:train_idx], X[train_idx:]
y_train, y_test = y[:train_idx], y[train_idx:]

# Scale inputs specifically for neural networks (ANN & LSTM)
scaler = MinMaxScaler(feature_range=(0, 1))
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Reshape for LSTM [samples, timesteps, features]
X_train_lstm = X_train_scaled.reshape((X_train_scaled.shape[0], X_train_scaled.shape[1], 1))
X_test_lstm = X_test_scaled.reshape((X_test_scaled.shape[0], X_test_scaled.shape[1], 1))

# Helper metric calculation function
def calculate_metrics(y_true, y_pred):
    # Inverse log transform to evaluate on original passenger scale
    y_true_exp = np.exp(y_true)
    y_pred_exp = np.exp(y_pred)
    
    rmse = np.sqrt(mean_squared_error(y_true_exp, y_pred_exp))
    mae = mean_absolute_error(y_true_exp, y_pred_exp)
    r2 = r2_score(y_true_exp, y_pred_exp)
    mape = np.mean(np.abs((y_true_exp - y_pred_exp) / y_true_exp)) * 100
    return {"RMSE": rmse, "MAE": mae, "R2": r2, "MAPE": mape}, y_pred_exp

results = {}
predictions_scaled_or_logged = {}

# ==========================================
# 3. MODEL DEVELOPMENT & EVALUATION
# ==========================================

# Model 1: Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
results['Linear Regression'], pred_lr = calculate_metrics(y_test, lr_model.predict(X_test))

# Model 2: XGBoost
xgb_model = XGBRegressor(n_estimators=100, max_depth=4, learning_rate=0.05, random_state=42)
xgb_model.fit(X_train, y_train)
results['XGBoost'], pred_xgb = calculate_metrics(y_test, xgb_model.predict(X_test))

# Model 3: Artificial Neural Network (ANN)
ann_model = Sequential([
    Dense(64, activation='relu', input_dim=LAG_WINDOW),
    Dense(32, activation='relu'),
    Dense(1)
])
ann_model.compile(optimizer='adam', loss='mse')
ann_model.fit(X_train_scaled, y_train, epochs=150, batch_size=8, verbose=0)
results['ANN'], pred_ann = calculate_metrics(y_test, ann_model.predict(X_test_scaled).flatten())

# Model 4: Long Short-Term Memory (LSTM)
lstm_model = Sequential([
    LSTM(50, activation='relu', input_shape=(LAG_WINDOW, 1), return_sequences=False),
    Dense(1)
])
lstm_model.compile(optimizer='adam', loss='mse')
lstm_model.fit(X_train_lstm, y_train, epochs=200, batch_size=8, verbose=0)
results['LSTM'], pred_lstm = calculate_metrics(y_test, lstm_model.predict(X_test_lstm).flatten())

# Model 5: ARIMA (Configured with structural drift using order (1,1,1))
# Note: Traditional ARIMA uses structural indexes. We fit directly on the train log values.
history = list(df['Log_Passengers'].values[:-TEST_SIZE])
arima_preds = []
for t in range(TEST_SIZE):
    model_arima = ARIMA(history, order=(1, 1, 1))
    model_fit = model_arima.fit()
    output = model_fit.forecast()
    arima_preds.append(output[0])
    history.append(df['Log_Passengers'].values[-TEST_SIZE + t])

results['ARIMA'], pred_arima = calculate_metrics(df['Log_Passengers'].values[-TEST_SIZE:], np.array(arima_preds))

# ==========================================
# 4. REPORTING PERFORMANCE
# ==========================================
df_results = pd.DataFrame(results).T
print("\n=== MODEL PERFORMANCE COMPARISON ===")
print(df_results.round(3))
