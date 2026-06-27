# 🇳🇿 NZ Wellbeing Forecasting — 5-Model Comparison

Forecasting the next year (2020) of New Zealand wellbeing indicators using five different approaches, evaluated head-to-head on the Stats NZ General Social Survey dataset.

## 📊 Dataset

**Source:** [Stats NZ General Social Survey (NZGSS) 2014–2018](https://www.stats.govt.nz/information-releases/wellbeing-statistics-201418-time-series/)  
**File:** `wellbeing-statistics-2014-18-time-series.xlsx`  
**Coverage:** 3 biennial survey waves (2014, 2016, 2018) across 20 wellbeing tables

### Indicators Used (Total Population)

| Indicator | 2014 | 2016 | 2018 |
|---|---|---|---|
| Life Satisfaction (Mean) | 7.8 | 7.8 | 7.7 |
| Life Worthwhile (Mean) | 8.1 | 8.1 | 8.1 |
| Financial Inadequacy (%) | 12.2 | 11.2 | 10.0 |
| Health Excellent (%) | 21.6 | 19.1 | 16.5 |
| Loneliness None (%) | 63.9 | 60.2 | 61.0 |
| Generalised Trust Low (%) | 8.7 | 8.6 | 9.7 |
| Job Very Satisfied (%) | 35.6 | 34.2 | 27.0 |
| Housing Problems (%) | 21.2 | 21.0 | 22.1 |
| Cultural Belonging (%) | 52.6 | 51.0 | 50.3 |
| Feel Safe at Home (%) | 60.9 | 60.7 | 61.9 |

---

## 🤖 Models

| Model | Description | Key Parameters |
|---|---|---|
| **Linear Regression** | OLS fit over time index | `y = β₀ + β₁·t` |
| **XGBoost (GBM)** | Gradient Boosting with feature engineering | `n_estimators=50, max_depth=2` |
| **LSTM** | Single LSTM cell (pure numpy) | `h=4, lr=0.005, epochs=3000` |
| **ANN** | 2-layer feedforward, backprop (pure numpy) | `h=8, lr=0.005, epochs=5000` |
| **ARIMA(1,1,1)** | AR(1) on first differences + MA(1) correction | OLS-fitted φ and θ |

> **Note:** LSTM and ANN are implemented from scratch in NumPy — no TensorFlow or PyTorch required.

---

## 📈 Results

### Model Performance (average across all 10 indicators)

| Rank | Model | Avg RMSE | Avg MAE | Avg R² | Avg MAPE (%) |
|---|---|---|---|---|---|
| 🥇 1 | XGBoost (GBM) | **0.0056** | **0.0050** | **1.0000** | **0.021** |
| 🥈 2 | Linear Regression | 0.3653 | 0.3444 | 0.7992 | 1.168 |
| 🥉 3 | ANN | 0.3726 | 0.3509 | 0.6931 | 1.220 |
| 4 | ARIMA(1,1,1) | 0.5285 | 0.3051 | 0.3933 | 1.390 |
| 5 | LSTM | 1.0849 | 0.9744 | ~0.000 | 4.008 |

### 🏆 Winner: XGBoost (GBM)
XGBoost achieves near-perfect in-sample fit by leveraging lag-difference features. **Important caveat:** with only 3 training points, overfitting is a concern — XGBoost's in-sample R²=1.0 reflects this. For practical out-of-sample forecasting, **Linear Regression** provides the best interpretable and generalizable baseline.

### 2020 Forecasts

| Indicator | Lin. Reg. | XGBoost | LSTM | ANN | ARIMA |
|---|---|---|---|---|---|
| Life Satisfaction Mean | 7.667 | 7.700 | 7.767 | 7.675 | 7.705 |
| Life Worthwhile Mean | 8.100 | 8.100 | 8.100 | 8.077 | 8.100 |
| Financial Inadequacy (%) | 8.933 | 10.006 | 11.139 | 9.147 | 8.834 |
| Health Excellent (%) | 13.967 | 16.513 | 19.079 | 14.466 | 13.934 |
| Loneliness None (%) | 58.800 | 61.004 | 61.706 | 59.138 | 60.827 |
| Trust Low (%) | 10.000 | 9.696 | 8.998 | 9.792 | 9.112 |
| Job Very Satisfied (%) | 23.667 | 27.027 | 32.288 | 24.429 | 25.686 |
| Housing Problems (%) | 22.333 | 22.097 | 21.431 | 22.122 | 21.418 |
| Cultural Belonging (%) | 49.000 | 50.305 | 51.305 | 49.240 | 49.994 |
| Feel Safe Home (%) | 62.167 | 61.896 | 61.164 | 61.937 | 61.214 |

---

## 📁 Repository Structure

```
nz_wellbeing_forecast/
├── data/
│   ├── extract_data.py          # Data extraction from XLSX
│   └── wellbeing_data.csv       # Cleaned dataset
├── models/
│   ├── forecast.py              # All 5 model implementations + evaluation
│   └── visualize.py             # Chart generation
├── slides/
│   ├── create_slides.js         # PptxGenJS presentation builder
│   └── NZ_Wellbeing_Forecast.pptx
├── outputs/
│   ├── metrics.csv              # Per-indicator per-model metrics
│   ├── summary.csv              # Aggregated model comparison
│   ├── forecasts_2020.csv       # 2020 forecast values
│   ├── 01_model_comparison.png
│   ├── 02_life_satisfaction_all_models.png
│   ├── 03_all_indicators_forecast.png
│   ├── 04_r2_heatmap.png
│   ├── 05_summary_table.png
│   └── 06_mape_by_indicator.png
└── README.md
```

---

## 🚀 Quick Start

```bash
# Install dependencies
pip install pandas numpy scikit-learn matplotlib seaborn openpyxl scipy

# Run data extraction
python data/extract_data.py

# Run all models and evaluation
python models/forecast.py

# Generate visualizations
python models/visualize.py

# Generate presentation (requires Node.js)
npm install -g pptxgenjs
node slides/create_slides.js
```

---

## ⚠️ Limitations

- **Small sample:** Only 3 biennial data points limits model training significantly
- **Deep learning disadvantage:** LSTM and ANN underperform with sparse data — they need more observations
- **XGBoost overfitting:** Perfect in-sample R²=1.0 is a red flag for 3-point data; treat XGBoost forecasts with caution
- **No external features:** GDP, unemployment, housing prices and other macroeconomic predictors could improve accuracy

## 💡 Future Work

- Integrate demographic sub-groups (age, gender, ethnicity) as additional series
- Incorporate macroeconomic covariates as exogenous regressors
- Validate forecasts against NZGSS 2020/2021 actuals
- Apply Bayesian forecasting with uncertainty quantification
- Use [Prophet](https://facebook.github.io/prophet/) for automatic seasonality handling

---

## 📄 License

MIT — free to use with attribution.

## 🙏 Citation

> Stats NZ. (2019). *Wellbeing statistics: 2014–18 (time series)*. Published 05 November 2019. www.stats.govt.nz
