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
*Visualization of a machine learning classification model's decision boundaries.

Based on the axis labels ("Sepal Length" and "Sepal Width"), this is almost certainly plotting data from the famous Iris dataset, which is often used to teach machine learning concepts.

Here is a breakdown of what the different parts of the image represent:

The Axes (Features): The horizontal axis represents "Sepal Length" and the vertical axis represents "Sepal Width". These are the two features (out of four in the original dataset) the model is using to make its predictions. By only using two features, we can visualize the results on a 2D graph.

The Markers (Data Points): The individual shapes (red dots, blue squares, and green triangles) represent the actual data points from the dataset.

There are three distinct classes (labeled 0, 1, and 2), which typically correspond to the three Iris flower species: Setosa, Versicolor, and Virginica.

The Background Colors (Prediction Regions): The shaded background areas (light red, light blue, light green) show how the trained machine learning model interprets the space.

If you were to introduce a completely new flower with a specific sepal length and width, the color of the region it falls into dictates what class the model will predict for it.

The Lines (Decision Boundaries): The places where the background colors meet are the decision boundaries. These are the specific thresholds where the model switches its prediction from one class to another.

Model Type Analysis: Because the decision boundaries are curved and somewhat complex (rather than straight lines), we can tell that the underlying model is a non-linear classifier. This means it is capable of finding more intricate patterns than a simple linear model. Common models that produce boundaries like this include Support Vector Machines (SVM) with an RBF kernel or k-Nearest Neighbors (k-NN).

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
