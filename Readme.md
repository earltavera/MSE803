# Heart Disease Data Analysis & Predictive Modeling

This project focuses on performing exploratory data analysis (EDA) and developing a predictive machine learning model using the UCI Heart Disease dataset. The goal is to identify key clinical features that correlate with heart disease and build a reliable classification model to assist in early detection.

---

## 1. Rationale Behind the Solution

Heart disease remains one of the leading causes of mortality globally. Early and accurate diagnosis can significantly improve patient outcomes. 

* **Clinical Relevance:** By identifying which medical metrics (e.g., cholesterol, maximum heart rate, ECG results) are most predictive of cardiovascular issues, healthcare providers can better stratify patient risk.
* **Data-Driven Decisions:** Rather than relying solely on intuitive heuristics, this solution leverages machine learning to detect complex, non-linear interactions between risk factors.
* **Actionable Insights:** The pipeline is designed not just to output a "yes/no" prediction, but to highlight *why* a patient is flagged as high-risk through feature importance metrics.

---

## 2. Development Process

The project is executed in a structured, five-stage data science pipeline:

## [Data Ingestion] ➔ [Data Cleaning & Preprocessing] ➔ [EDA & Visualization] ➔ [Model Training & Evaluation] ➔ [Deployment/Insights]

1.  **Data Ingestion & Inspection:** Loading the dataset from the local path (`/MSE803/Week 10/Activity 2/heart+disease`) and inspecting data types, shape, and missing values.
2.  **Data Preprocessing:** * Handling missing or anomalous values (e.g., replacing standard placeholders like `?` with NaN and imputing them).
    * Encoding categorical variables (like `sex`, `cp` [chest pain type], `restecg`) using One-Hot Encoding.
    * Scaling numerical features (like `age`, `trestbps` [blood pressure], `chol`) using standard scaling to optimize model convergence.
3.  **Exploratory Data Analysis (EDA):** Visualizing distributions and statistical correlations to understand the underlying data structure.
4.  **Model Training:** Training baseline classifiers (e.g., Logistic Regression, Random Forest, and Gradient Boosting) and tuning hyperparameters using Stratified K-Fold Cross-Validation to prevent overfitting.
5.  **Evaluation:** Metrics-driven evaluation focusing heavily on **Recall (Sensitivity)** alongside Accuracy and F1-Score, ensuring that the model minimizes dangerous false negatives (missing an actual heart disease case).

---

## 3. Data Visualization Strategy

To translate raw numbers into clinical insights, the analysis utilizes the following core visualizations:

* **Correlation Matrix (Heatmap):** A Seaborn heatmap to display Pearson correlation coefficients between numerical features and the target variable, identifying strong predictors at a glance.
* **Distribution & Risk Profiles:** Histograms and Kernel Density Estimate (KDE) plots comparing features like `thalach` (max heart rate) and `age` across healthy vs. diseased patients.
* **Categorical Groupings:** Bar charts showing the prevalence of heart disease across different chest pain types (`cp`) and genders (`sex`), exposing demographic disparities in the data.
* **Receiver Operating Characteristic (ROC) Curve:** A plot of the True Positive Rate against the False Positive Rate to visually assess and compare model performance across different thresholds.

---

## 4. Expected Results & Insights

Based on standard benchmarks for the UCI Heart Disease dataset, the analysis typically yields the following outcomes:

### Key Findings
* **Major Predictors:** Features like chest pain type (`cp`), maximum heart rate achieved (`thalach`), and ST depression induced by exercise (`oldpeak`) consistently emerge as the strongest predictors of heart disease.
* **Demographic Trends:** Higher age groups and specific chest pain presentations (e.g., asymptomatic chest pain that later reveals underlying ischemia) show statistically higher rates of positive diagnoses.

### Model Performance Metrics

| Model | Accuracy | Recall (Sensitivity) | F1-Score | AUC-ROC |
| :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | ~83% | ~81% | ~82% | 0.88 |
| **Random Forest** | ~85% | ~84% | ~85% | 0.91 |
| **Gradient Boosting** | ~86% | ~85% | ~86% | 0.92 |

*Ensemble methods (Random Forest/Gradient Boosting) generally yield the best performance due to their ability to capture complex feature interactions without assuming linear relationships.*

---

## 5. How to Run the Analysis

### Prerequisites
Ensure you have Python installed along with the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
