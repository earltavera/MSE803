# Salary Prediction Using Regression Analysis

This project demonstrates the implementation, evaluation, and comparison of **Linear Regression** and **Polynomial Regression** models to forecast salaries based on years of professional experience. It utilizes data preprocessing, statistical outlier detection, and performance evaluation metrics to find the most robust predictive model.

---

## 📋 Project Overview

When predicting metrics like compensation, relationships can often be non-linear due to diminishing returns, career jumps, or compounding skill sets over time. This repository explores how structural model changes (Linear vs. Polynomial degrees) impact prediction errors both within known sample limits and during external extrapolation.

### Key Objectives:
1. Conduct data cleaning and check for statistical outliers using the Interquartile Range (IQR) method.
2. Implement and evaluate a baseline **Linear Regression** model.
3. Implement and evaluate **Polynomial Regression** models (Degrees 2 & 3).
4. Outline and describe core error evaluation metrics ($MAE$, $MSE$, $RMSE$).
5. Extrapolate predictions for individuals with 14, 14.5, and 15 years of experience.

---

## 📊 Dataset Summary & Preprocessing

The underlying dataset (`salary-dataset.csv`) consists of target records containing two main variables:
- **YearsExperience**: Continuous independent variable ranging from 1.2 to 13.0 years.
- **Salary**: Target continuous dependent variable ranging from $37,732 to $138,821.

### Preprocessing Steps:
- **Data Cleansing**: Dropped raw, unindexed data columns (`Unnamed: 0`). Verified that the dataset contains zero null or missing values.
- **Outlier Assessment**: Applied the IQR outlier check formula ($Q1 - 1.5 \times IQR$ to $Q3 + 1.5 \times IQR$). All records fell entirely within healthy statistical boundaries; no data points were trimmed.
- **Validation Splitting**: The records were split into an 80% training set and a 20% validation test set to guarantee an unbiased performance evaluation.

---

## 📉 Error Metrics Explained

To accurately measure model performance, three mathematical metrics are evaluated on the test predictions:

1. **Mean Absolute Error (MAE)**
   $$MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$
   *The average magnitude of errors regardless of direction. It provides a direct representation of how off the predictions are on average, matching the target currency unit ($).*

2. **Mean Squared Error (MSE)**
   $$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
   *Squares individual errors before averaging them. This severely penalizes larger variances or errors, highlighting instances where the model misses targets drastically. Measured in squared units ($^2$).*

3. **Root Mean Squared Error (RMSE)**
   $$RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$
   *The square root of MSE. It preserves the outlier-penalizing trait of MSE while converting the final value back into the original, interpretable unit of the target ($).*

---

## 🏆 Performance & Model Comparison

Evaluation metrics achieved on the validation split:

| Metric | Linear Regression | Polynomial Regression (Deg 2) | Polynomial Regression (Deg 3) |
| :--- | :--- | :--- | :--- |
| **MAE** | \$5,802.51 | \$5,435.01 | \$4,295.13 |
| **MSE** | 39,318,711.54 | 37,704,204.94 | 26,546,825.50 |
| **RMSE** | \$6,270.46 | \$6,140.37 | \$5,152.36 |

### Extrapolation Comparison (Future Predictions)
When prompting the models to predict salaries outside the original training maximum (up to 13 years) to targets **14, 14.5, and 15 years**, the following values were generated:

| Experience Level | Linear Regression | Polynomial (Degree 2) | Polynomial (Degree 3) |
| :--- | :--- | :--- | :--- |
| **14.0 Years** | \$153,441.74 | \$149,313.84 | \$138,926.10 |
| **14.5 Years** | \$157,973.48 | \$153,002.59 | \$138,763.90 |
| **15.0 Years** | \$162,505.22 | \$156,632.76 | \$137,905.07 |

### Critical Takeaway:
While **Polynomial Degree 3** achieves the lowest error inside the validation partition, it fails the real-world logic test during extrapolation. Because cubic expressions ($X^3$) can bend erratically beyond data boundaries, it incorrectly predicts that a person with 15 years of experience earns *less* than someone with 14 years. **Polynomial Degree 2** yields a highly accurate curve while maintaining a realistic, upward-trending career salary growth.

---

## 💻 Implementation Code

Below is the structured execution script optimized for **Jupyter Notebooks**:

```python
import numpy as np
import pandas
