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

## Model Performance
The linear SVM model performs exceptionally well on this highly structured dataset:
* **Overall Accuracy:** `96.3%`
* **Precision/Recall/F1-Score:** Consistently high across all three distinct wine classes (ranging from `0.93` to `1.00`), indicating robust and balanced classification with minimal overlap.

---

## Setup and Execution

### Prerequisites
Ensure your Python environment has the required scientific computing libraries installed. You can install them collectively via pip:
```bash
pip install pandas matplotlib seaborn scikit-learn
