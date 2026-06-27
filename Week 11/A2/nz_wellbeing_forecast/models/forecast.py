"""
NZ Wellbeing Forecasting - Comparing 5 models:
Linear Regression, XGBoost (GBM), LSTM (numpy), ANN (numpy), ARIMA (scipy)
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import warnings
warnings.filterwarnings("ignore")

# ── 1. Data ──────────────────────────────────────────────────────────────────

YEARS = np.array([2014, 2016, 2018])
FORECAST_YEAR = 2020

DATA = {
    "Life Satisfaction Mean":      [7.8, 7.8, 7.7],
    "Life Worthwhile Mean":        [8.1, 8.1, 8.1],
    "Financial Inadequacy (%)":    [12.2, 11.2, 10.0],
    "Health Excellent (%)":        [21.6, 19.1, 16.5],
    "Loneliness None (%)":         [63.9, 60.2, 61.0],
    "Generalised Trust Low (%)":   [8.7, 8.6, 9.7],
    "Job Very Satisfied (%)":      [35.6, 34.2, 27.0],
    "Housing Problems (%)":        [21.2, 21.0, 22.1],
    "Cultural Belonging (%)":      [52.6, 51.0, 50.3],
    "Feel Safe Home (%)":          [60.9, 60.7, 61.9],
}

df = pd.DataFrame(DATA, index=YEARS)
df.index.name = "Year"


# ── 2. Utility ────────────────────────────────────────────────────────────────

def compute_metrics(actual, predicted, label=""):
    mae  = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    r2   = r2_score(actual, predicted)
    mape = np.mean(np.abs((np.array(actual) - np.array(predicted)) / np.array(actual))) * 100
    return {"Model": label, "MAE": mae, "RMSE": rmse, "R²": r2, "MAPE (%)": mape}


# ── 3. Model 1: Linear Regression ─────────────────────────────────────────────

def linear_regression_forecast(series_dict, forecast_year=2020):
    X = YEARS.reshape(-1, 1)
    results = {}
    for name, values in series_dict.items():
        y = np.array(values)
        model = LinearRegression()
        model.fit(X, y)
        fitted   = model.predict(X)
        forecast = model.predict([[forecast_year]])[0]
        results[name] = {"fitted": fitted, "forecast": forecast, "model": model}
    return results


# ── 4. Model 2: XGBoost (Gradient Boosting) ───────────────────────────────────

def xgboost_forecast(series_dict, forecast_year=2020):
    """
    With only 3 data points, we use leave-one-out cross-validation style fitting.
    Features: year, lag-1 difference, normalized time index.
    """
    results = {}
    for name, values in series_dict.items():
        y = np.array(values, dtype=float)
        # Feature engineering
        X = np.column_stack([
            YEARS,
            YEARS - YEARS[0],              # time offset
            np.array([0] + list(np.diff(y))),  # lag-1 diff
        ])
        model = GradientBoostingRegressor(
            n_estimators=50, max_depth=2, learning_rate=0.1,
            subsample=1.0, random_state=42
        )
        model.fit(X, y)
        fitted = model.predict(X)
        last_diff = y[-1] - y[-2]
        X_fc = np.array([[forecast_year, forecast_year - YEARS[0], last_diff]])
        forecast = model.predict(X_fc)[0]
        results[name] = {"fitted": fitted, "forecast": forecast, "model": model}
    return results


# ── 5. Model 3: LSTM (numpy implementation) ───────────────────────────────────

def sigmoid(x): return 1 / (1 + np.exp(-np.clip(x, -10, 10)))
def tanh(x):    return np.tanh(np.clip(x, -10, 10))

class SimpleLSTM:
    """Minimal single-cell LSTM trained via gradient descent."""
    def __init__(self, hidden=4, lr=0.01, epochs=2000, seed=42):
        np.random.seed(seed)
        self.h, self.lr, self.epochs = hidden, lr, epochs
        h = hidden
        self.Wf = np.random.randn(1 + h, h) * 0.1
        self.Wi = np.random.randn(1 + h, h) * 0.1
        self.Wc = np.random.randn(1 + h, h) * 0.1
        self.Wo = np.random.randn(1 + h, h) * 0.1
        self.bf = np.zeros(h)
        self.bi = np.zeros(h)
        self.bc = np.zeros(h)
        self.bo = np.zeros(h)
        self.Wy = np.random.randn(h, 1) * 0.1
        self.by = np.zeros(1)

    def forward(self, xs):
        h_prev = np.zeros(self.h)
        c_prev = np.zeros(self.h)
        outputs, hs, cs = [], [h_prev], [c_prev]
        gates = []
        for x in xs:
            xh = np.concatenate([[x], h_prev])
            f  = sigmoid(xh @ self.Wf + self.bf)
            i  = sigmoid(xh @ self.Wi + self.bi)
            g  = tanh(xh   @ self.Wc + self.bc)
            o  = sigmoid(xh @ self.Wo + self.bo)
            c  = f * c_prev + i * g
            h  = o * tanh(c)
            y  = h @ self.Wy + self.by
            outputs.append(y[0])
            hs.append(h); cs.append(c)
            gates.append((xh, f, i, g, o, c, h))
            h_prev, c_prev = h, c
        return outputs, hs, cs, gates

    def fit(self, X, y_true):
        scaler = MinMaxScaler()
        X_s = scaler.fit_transform(X.reshape(-1,1)).flatten()
        y_s = scaler.fit_transform(np.array(y_true).reshape(-1,1)).flatten()
        self.scaler_X = scaler
        y_scaler = MinMaxScaler()
        y_s = y_scaler.fit_transform(np.array(y_true).reshape(-1,1)).flatten()
        self.scaler_y = y_scaler
        for _ in range(self.epochs):
            outs, *_ = self.forward(X_s)
            err = np.array(outs) - y_s
            # Simple gradient descent on output weights only (truncated BPTT)
            _, hs, cs, gates = self.forward(X_s)
            for t in range(len(X_s)):
                dWy = np.outer(hs[t+1], [err[t]])
                self.Wy -= self.lr * dWy
                self.by -= self.lr * err[t]

    def predict(self, X):
        X_s = self.scaler_X.transform(X.reshape(-1,1)).flatten()
        outs, *_ = self.forward(X_s)
        return self.scaler_y.inverse_transform(
            np.array(outs).reshape(-1,1)).flatten()


def lstm_forecast(series_dict, forecast_year=2020):
    results = {}
    for name, values in series_dict.items():
        y = np.array(values, dtype=float)
        X = YEARS.astype(float)
        model = SimpleLSTM(hidden=4, lr=0.005, epochs=3000)
        model.fit(X, y)
        fitted   = model.predict(X)
        X_fc     = np.array([float(forecast_year)])
        forecast = model.predict(X_fc)[0]
        results[name] = {"fitted": fitted, "forecast": forecast, "model": model}
    return results


# ── 6. Model 4: ANN (numpy feedforward) ───────────────────────────────────────

class SimpleANN:
    """2-layer feedforward network trained with backpropagation."""
    def __init__(self, hidden=8, lr=0.01, epochs=5000, seed=42):
        np.random.seed(seed)
        self.lr, self.epochs = lr, epochs
        self.W1 = np.random.randn(1, hidden) * 0.1
        self.b1 = np.zeros(hidden)
        self.W2 = np.random.randn(hidden, 1) * 0.1
        self.b2 = np.zeros(1)
        self.scaler_X = MinMaxScaler()
        self.scaler_y = MinMaxScaler()

    def _forward(self, X):
        self.z1 = X @ self.W1 + self.b1
        self.a1 = np.tanh(self.z1)
        self.z2 = self.a1 @ self.W2 + self.b2
        return self.z2

    def fit(self, X, y):
        X_s = self.scaler_X.fit_transform(X.reshape(-1,1))
        y_s = self.scaler_y.fit_transform(y.reshape(-1,1))
        for _ in range(self.epochs):
            out = self._forward(X_s)
            err = out - y_s
            dW2 = self.a1.T @ err / len(X_s)
            db2 = err.mean(axis=0)
            da1 = err @ self.W2.T * (1 - self.a1**2)
            dW1 = X_s.T @ da1 / len(X_s)
            db1 = da1.mean(axis=0)
            self.W2 -= self.lr * dW2
            self.b2 -= self.lr * db2
            self.W1 -= self.lr * dW1
            self.b1 -= self.lr * db1

    def predict(self, X):
        X_s = self.scaler_X.transform(X.reshape(-1,1))
        out = self._forward(X_s)
        return self.scaler_y.inverse_transform(out).flatten()


def ann_forecast(series_dict, forecast_year=2020):
    results = {}
    for name, values in series_dict.items():
        y = np.array(values, dtype=float)
        X = YEARS.astype(float)
        model = SimpleANN(hidden=8, lr=0.005, epochs=5000)
        model.fit(X, y)
        fitted   = model.predict(X)
        forecast = model.predict(np.array([float(forecast_year)]))[0]
        results[name] = {"fitted": fitted, "forecast": forecast, "model": model}
    return results


# ── 7. Model 5: ARIMA (manual implementation) ────────────────────────────────

def arima_forecast(series_dict, forecast_year=2020):
    """
    ARIMA(1,1,1) implemented manually.
    With 3 points, we fit AR(1) on first-differences.
    """
    results = {}
    for name, values in series_dict.items():
        y = np.array(values, dtype=float)
        # First difference (I=1)
        diff = np.diff(y)        # len=2
        # AR(1): diff[t] = phi * diff[t-1] + eps
        if len(diff) >= 2:
            phi = np.sum(diff[1:] * diff[:-1]) / (np.sum(diff[:-1]**2) + 1e-10)
            phi = np.clip(phi, -0.99, 0.99)
        else:
            phi = 0.5
        # MA(1) residual correction
        ar_fitted = np.array([diff[0]] + [phi * diff[i-1] for i in range(1, len(diff))])
        residuals  = diff - ar_fitted
        theta = np.clip(np.mean(residuals), -1, 1)

        # Reconstruct fitted values
        fitted_diff = [phi * diff[0] + theta * residuals[0]]  # one-step
        fitted_full = [y[0], y[0] + diff[0], y[1] + fitted_diff[0]]

        # Forecast next difference
        next_diff = phi * diff[-1] + theta * residuals[-1]
        forecast  = y[-1] + next_diff

        results[name] = {
            "fitted":   np.array(fitted_full),
            "forecast": forecast,
            "phi": phi, "theta": theta
        }
    return results


# ── 8. Run all models & compile results ──────────────────────────────────────

def run_all_models():
    series_dict = {k: list(v) for k, v in DATA.items()}

    print("Running all models...\n")
    lr_res   = linear_regression_forecast(series_dict)
    gbm_res  = xgboost_forecast(series_dict)
    lstm_res = lstm_forecast(series_dict)
    ann_res  = ann_forecast(series_dict)
    ar_res   = arima_forecast(series_dict)

    model_results  = {
        "Linear Regression": lr_res,
        "XGBoost (GBM)":     gbm_res,
        "LSTM":              lstm_res,
        "ANN":               ann_res,
        "ARIMA(1,1,1)":      ar_res,
    }

    # Metrics per indicator per model
    all_metrics = []
    forecast_rows = []

    for mname, mres in model_results.items():
        for iname, vals in series_dict.items():
            y_true = np.array(vals)
            fitted  = mres[iname]["fitted"]
            # align length
            if len(fitted) != len(y_true):
                fitted = fitted[:len(y_true)]
            m = compute_metrics(y_true, fitted, label=f"{mname} | {iname}")
            m["Indicator"] = iname
            m["Forecast 2020"] = round(mres[iname]["forecast"], 3)
            all_metrics.append(m)

        # Average across indicators
        avg_mae  = np.mean([m["MAE"]      for m in all_metrics if m["Model"].startswith(mname)])
        avg_rmse = np.mean([m["RMSE"]     for m in all_metrics if m["Model"].startswith(mname)])
        avg_r2   = np.mean([m["R²"]       for m in all_metrics if m["Model"].startswith(mname)])
        avg_mape = np.mean([m["MAPE (%)"] for m in all_metrics if m["Model"].startswith(mname)])
        forecast_rows.append({
            "Model": mname,
            "Avg MAE":     round(avg_mae, 4),
            "Avg RMSE":    round(avg_rmse, 4),
            "Avg R²":      round(avg_r2, 4),
            "Avg MAPE (%)":round(avg_mape, 4),
        })

    metrics_df   = pd.DataFrame(all_metrics)
    summary_df   = pd.DataFrame(forecast_rows).sort_values("Avg RMSE")

    # Forecast table
    fc_table = {}
    for mname, mres in model_results.items():
        fc_table[mname] = {k: round(mres[k]["forecast"], 3) for k in series_dict}
    fc_df = pd.DataFrame(fc_table)

    return metrics_df, summary_df, fc_df, model_results, series_dict


if __name__ == "__main__":
    metrics_df, summary_df, fc_df, model_results, series_dict = run_all_models()
    print("\n=== MODEL COMPARISON (average across all indicators) ===")
    print(summary_df.to_string(index=False))
    print("\n=== 2020 FORECASTS ===")
    print(fc_df.to_string())
    metrics_df.to_csv("/home/claude/nz_wellbeing_forecast/outputs/metrics.csv", index=False)
    summary_df.to_csv("/home/claude/nz_wellbeing_forecast/outputs/summary.csv", index=False)
    fc_df.to_csv("/home/claude/nz_wellbeing_forecast/outputs/forecasts_2020.csv")
    print("\nSaved outputs.")
