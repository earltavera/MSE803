---

# 📖 Activity 2`

# Student Knowledge Level Modeling: End-to-End Analysis

An end-to-end Machine Learning and Data Analysis project leveraging the **User Modeling Dataset** to investigate student study habits, segment learners, and build highly accurate classification pipelines to predict academic knowledge levels.

---

## 📌 Executive Summary

Understanding how self-regulated study behaviors translate into actual domain mastery is a core challenge in educational data science. This project analyzes **403 student records** across 5 continuous behavioral and performance metrics to model and predict a learner's knowledge status (`UNS`). 

Through exploratory data analysis and unsupervised clustering, we demonstrate that **study time and material repetition alone do not guarantee comprehension**. By deploying tree-based ensemble algorithms, we achieved a **92.41% classification accuracy** on unseen test data, identifying objective exam performance as the overwhelming determinant of academic mastery.

---

## 🗂️ Dataset Architecture

The project utilizes the **User Modeling Dataset**, comprising 403 total student records split into training ($N=258$) and testing ($N=145$) sets. Each instance is defined by five real-valued continuous attributes $[0, 1]$ and one nominal target label:

| Attribute | Code | Description | Data Type |
| :--- | :---: | :--- | :---: |
| **Study Time (Goal)** | `STG` | Degree of study time dedicated to goal object materials | Continuous $[0,1]$ |
| **Repetitions (Goal)** | `SCG` | Number of revisitations/repetitions for goal materials | Continuous $[0,1]$ |
| **Study Time (Related)** | `STR` | Degree of study time dedicated to related objects | Continuous $[0,1]$ |
| **Exam Score (Related)**| `LPR` | Exam performance on related objects | Continuous $[0,1]$ |
| **Exam Score (Goal)** | `PEG` | Exam performance on goal objects | Continuous $[0,1]$ |
| **Knowledge Level** | `UNS` | **Target Variable:** Nominal mastery classification | Categorical (4 Classes) |

---

## 🧹 Data Preprocessing & Cleaning

Data hygiene protocols were executed prior to exploratory and predictive modeling:

1. **Header Whitespace Removal**: Stripped irregular leading/trailing spaces across feature strings (e.g., `' UNS'` $\rightarrow$ `'UNS'`).
2. **Artifact Truncation**: Dropped empty trailing metadata columns (`Unnamed: 6`, `Unnamed: 7`) present in the raw spreadsheet exports.
3. **Target Label Harmonization**: Resolved string casing mismatches across partitions (`'very_low'` vs `'Very Low'`). Target classes were standardized into an ordered hierarchy:
   * **Low**: 129 students (**32.0%**)
   * **Middle**: 122 students (**30.3%**)
   * **High**: 102 students (**25.3%**)
   * **Very Low**: 50 students (**12.4%**)
4. **Validation Check**: Verified **0 missing values (`NaN`)** and confirmed full feature rank across all dimensions.

---

## 📊 Exploratory Data Analysis (EDA)

* **Behavioral Independence**: Time investments (`STG`, `SCG`, `STR`) display near-zero linear correlation with each other ($r < 0.08$). Learners exhibit diverse study personas—high repetition does not imply high initial study duration.
* **The Assessment Anchor**: Exam performances (`PEG` and `LPR`) show the strongest direct separation across target classes. 

---

## ⚙️ Methodology & Results

### 1. Unsupervised Segmentation ($k$-Means)
Features were standardized via $z$-score normalization ($\mu=0, \sigma=1$). Optimal cluster capacity was evaluated using the **Silhouette Coefficient**:
* $k=2$: `0.182`
* $k=3$: `0.171`
* $k=4$: `0.172`
* $k=5$: **`0.183` (Optimal Geometric Separation)**

Mapping unsupervised $k=4$ Euclidean clusters against true nominal labels revealed significant boundary overlap, confirming that student proficiency operates on complex, non-linear competency thresholds rather than simple spatial density.

### 2. Supervised Classification Modeling
Using the predefined split (258 Train / 145 Test), four distinct predictive engines were trained and evaluated:

| Classification Model | Test Accuracy | Macro F1-Score | Analytical Takeaway |
| :--- | :---: | :---: | :--- |
| **Logistic Regression** | `68.97%` | `0.57` | Linear decision boundaries failed entirely on minority classes (*Very Low* Precision = 0%). |
| **Decision Tree (CART)** | `86.21%` | `0.86` | Strong baseline; successfully captures orthogonal feature splits. |
| **Gradient Boosting** | `91.72%` | `0.92` | Exceptional generalization across edge-case boundaries. |
| **Random Forest** | **`92.41%`** | **`0.92`** | **Champion Model:** Achieved **100% Precision & Recall** on *High* mastery learners. |

#### Champion Model Confusion Matrix Breakdown (Test Partition):
* **High (`n=39`)**: 39 Correct | 0 False Positives | 0 False Negatives
* **Middle (`n=34`)**: 30 Correct | Confused 4 instances as *Low*
* **Low (`n=46`)**: 43 Correct | Confused 3 instances as *Middle*
* **Very Low (`n=26`)**: 22 Correct | Confused 4 instances as *Low*

---

## 💡 Key Analytical Insights

1. **The Dominance of Objective Assessment**: Mean Decrease Impurity (Gini importance) establishes **`PEG` (Goal Exam Score)** as the primary driver of student classification, holding **62.7%** of total predictive weight. **`LPR` (Related Exam Score)** adds **16.5%**. Together, actual test evaluations account for **79.2%** of model decisions.
2. **The "Effort Disconnect"**: Raw study metrics (`STG` = 8.1%, `SCG` = 7.3%, `STR` = 5.5%) hold minimal standalone predictive value. Long study hours do not reliably translate to high knowledge categorization unless converted directly into assessment performance.
3. **Non-Linear Mastery Gateways**: The sharp jump in performance from linear models (`68.97%`) to non-linear decision forests (`92.41%`) illustrates that educational mastery is gated by discrete cognitive breakthroughs rather than gradual linear accumulations.

---

## 💻 Quickstart & Reproducibility Pipeline

Run the complete, self-contained analytical pipeline directly from your Python terminal:

```bash
# 1. Clone repository & install dependencies
pip install pandas numpy scikit-learn matplotlib seaborn
