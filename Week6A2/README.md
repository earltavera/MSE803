# Wine Dataset Classification using SVM

This project performs Exploratory Data Analysis (EDA), data cleaning, visualization, and predictive modeling on the classic **Wine Dataset** from the UCI Machine Learning Repository. A linear Support Vector Classifier (SVC) is used to distinguish between three different wine cultivars based on their 13 chemical properties.

---

## Project Features
* **Data Loading:** Configured to fetch the dataset directly from the UCI web repository (or load locally via `wine.data`).
* **Data Cleaning:** Defensively checks for and drops any missing (`NaN`) values and exact duplicate rows.
* **Exploratory Data Analysis (EDA):** Prints dataset dimensions, missing value counts, and duplicate row counts to the console before processing.
* **Visualizations:** Generates insightful visual charts to map class distribution and feature separation.
* **Machine Learning:** Standardizes features (`StandardScaler`) to account for varying measurement scales, then trains a Support Vector Machine (`kernel='linear'`) to classify the wines.
* **Evaluation:** Outputs detailed metrics including Overall Accuracy, a Confusion Matrix, and a comprehensive Classification Report.

---

## Generated Visualizations
Running the script automatically generates and saves the following charts to your working directory:

<img width="600" height="400" alt="wine_class_distribution" src="https://github.com/user-attachments/assets/a68b8c05-c5a2-4058-ac20-adebcb744740" />

* `wine_class_distribution.png`: A bar chart showing the count balance of instances across the three wine classes.

<img width="800" height="600" alt="wine_alcohol_vs_color" src="https://github.com/user-attachments/assets/8d763891-5d1e-48e4-a29e-dd4cd0bf91b3" />

* `wine_alcohol_vs_color.png`: A scatter plot demonstrating how the different wine classes separate based on Alcohol content and Color Intensity.

---

## Data Cleaning Summary

<img width="1171" height="552" alt="output" src="https://github.com/user-attachments/assets/c511342a-9c9f-43e7-8802-5256e1d440af" />

### --- Before Cleaning ---
* **Dataset Size: (178, 14):** This indicates the raw dataset has 178 rows (individual wine samples) and 14 columns. Typically, one column is the target variable (the class or type of wine), and the remaining 13 are features (chemical properties like alcohol content, flavanoids, color intensity, etc.).
* **Duplicates: 0:** There are no identical rows in the dataset.
* **Missing Values: 0 total missing cells:** The dataset is complete; there are no empty cells or NaN (Not a Number) values. This is an ideal scenario in data science.

### --- After Cleaning ---
* **Dataset Size: (178, 14):** Because there were no duplicates or missing values, the data cleaning steps (like dropping duplicates or filling missing values) didn't alter the dataset. The size remains exactly the same.
* **Charts saved...:** This line confirms that the code generated and saved two visualizations locally: one showing the distribution of wine classes and another plotting alcohol content against color intensity.

---

## Model Evaluation Summary
The second half of the output details the performance of the classification model (likely a Support Vector Machine or similar classifier, given previous contexts) on the test portion of the data.

* **Accuracy: 0.9630:** This is the headline metric. It means the model correctly predicted the class of the wine 96.3% of the time on the unseen test dataset.

### The Confusion Matrix
The confusion matrix gives a detailed breakdown of where the model made correct predictions and where it made errors across the three different classes (labeled 1, 2, and 3).

```text
[[18  0  0]  <- Actual Class 1
 [ 1 20  0]  <- Actual Class 2
 [ 0  1 14]] <- Actual Class 3
   ^  ^  ^
   |  |  |
Predicted Class
