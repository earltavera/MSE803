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


<img width="1171" height="552" alt="output" src="https://github.com/user-attachments/assets/c511342a-9c9f-43e7-8802-5256e1d440af" />
Data Cleaning Summary
--- Before Cleaning ---

Dataset Size: (178, 14): This indicates the raw dataset has 178 rows (individual wine samples) and 14 columns. Typically, one column is the target variable (the class or type of wine), and the remaining 13 are features (chemical properties like alcohol content, flavanoids, color intensity, etc.).

Duplicates: 0: There are no identical rows in the dataset.

Missing Values: 0 total missing cells: The dataset is complete; there are no empty cells or NaN (Not a Number) values. This is an ideal scenario in data science.

--- After Cleaning ---

Dataset Size: (178, 14): Because there were no duplicates or missing values, the data cleaning steps (like dropping duplicates or filling missing values) didn't alter the dataset. The size remains exactly the same.

Charts saved...: This line confirms that the code generated and saved two visualizations locally: one showing the distribution of wine classes and another plotting alcohol content against color intensity.

Model Evaluation Summary
The second half of the output details the performance of the classification model (likely a Support Vector Machine or similar classifier, given previous contexts) on the test portion of the data.

Accuracy: 0.9630: This is the headline metric. It means the model correctly predicted the class of the wine 96.3% of the time on the unseen test dataset.

The Confusion Matrix
The confusion matrix gives a detailed breakdown of where the model made correct predictions and where it made errors across the three different classes (labeled 1, 2, and 3).

Plaintext
[[18  0  0]  <- Actual Class 1
 [ 1 20  0]  <- Actual Class 2
 [ 0  1 14]] <- Actual Class 3
   ^  ^  ^
   |  |  |
Predicted Class

Row 1 (Actual Class 1): Out of 18 total Class 1 wines, the model predicted all 18 correctly.

Row 2 (Actual Class 2): Out of 21 total Class 2 wines, the model predicted 20 correctly, but mistakenly classified 1 as Class 1.

Row 3 (Actual Class 3): Out of 15 total Class 3 wines, the model predicted 14 correctly, but mistakenly classified 1 as Class 2.

The diagonal elements (18, 20, 14) represent the correct predictions, while the off-diagonal elements (1, 1) represent the errors.

The Classification Report
This report provides deeper metrics for each specific class, which is especially useful if the classes are imbalanced (though they are fairly balanced here).

precision: Out of all the wines the model predicted to be in a certain class, how many actually were?

Example (Class 3): Precision is 1.00 (100%). The model predicted Class 3 14 times (look down the third column of the confusion matrix), and all 14 times it was correct.

recall: Out of all the actual wines in a certain class, how many did the model successfully find?

Example (Class 1): Recall is 1.00 (100%). There were 18 Class 1 wines in the test set, and the model found all of them.

Example (Class 3): Recall is 0.93 (93%). There were 15 actual Class 3 wines, but the model only found 14 of them (missing 1).

f1-score: This is the harmonic mean of precision and recall. It provides a single metric that balances both concerns. Scores of 0.95 to 0.97 are excellent.

support: This is simply the number of actual occurrences of each class in the test dataset (18, 21, and 15, totaling 54 samples).

accuracy: The overall accuracy across all classes (0.96 or 96.3%), matching the top line.

macro avg: The unweighted average of precision, recall, and F1-score across all three classes. It treats all classes equally, regardless of how many samples they have.

weighted avg: The average of those metrics, weighted by the number of samples (support) in each class. This is often the most representative overall metric when classes are unevenly distributed.

In summary, this output indicates you are working with a perfectly clean dataset and your model is highly effective at distinguishing between the three wine cultivars.

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
