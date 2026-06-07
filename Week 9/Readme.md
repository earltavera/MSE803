# Week 9 - Activity 1: Fitness App User Segmentation using K-Means

## 📌 Project Overview
This project focuses on performing unsupervised machine learning (**K-Means Clustering**) on historical user behavioral data from a fitness mobile application using the dataset **Fitness_App_User_Data.xlsx**. The objective is to discover latent user archetypes based on engagement metrics, isolate high-churn-risk behavior groups, and offer data-driven structural recommendations to maximize customer retention and user loyalty.

---

## 🛠️ Data Cleaning & Preprocessing

Before feeding data into the clustering engine, data cleaning steps were performed on the 200 records in `Fitness_App_User_Data.xlsx`:

1. **Missing Values & Duplicates:** A structural validation scan confirmed **zero (0)** null parameters and **zero (0)** duplicate rows across the entire dataset.
2. **Data Inconsistency Remediation:** During the exploratory data analysis (EDA) phase, a significant data entry anomaly was identified: **User #36** possessed a negative session length (`Avg_Session_Duration_Min = -5.5`). Because negative physical durations are logically impossible, this value was safely converted using its absolute value (`5.5`) to eliminate skewed training points.
3. **Feature Selection:** To group users cleanly by operational lifestyle activity rather than standard demographic identifiers, three primary behavioral features were extracted:
   * `Workouts_per_Week`
   * `Avg_Session_Duration_Min`
   * `Steps_per_Day`
4. **Feature Scaling:** Since metrics vary wildly in scale (e.g., weekly workouts range from 0 to 6, whereas daily steps scale in the thousands), data features were transformed using `StandardScaler` ($Z$-score normalization) to prevent the step metrics from disproportionately biasing distance calculations.

---

## 📊 Clustering Methodology & Key Insights

### The Elbow Method
Using Within-Cluster Sum of Squares (WCSS) across cluster parameters ($K = 1$ to $10$), the optimal structural inflection point ("the elbow") was verified at **$K = 3$**. This balances mathematical variance compression without overcomplicating business application.

<img width="653" height="353" alt="Screenshot 2026-06-07 at 12 19 12 PM" src="https://github.com/user-attachments/assets/dba4cd90-fb06-46f7-9c80-ef51a54ecd3f" />

### Generated Cluster Profiles

Following execution of the `KMeans(n_clusters=3, random_state=42)` model, the 200 fitness app users fell into three explicit behavioral buckets:

| Performance Metric | Cluster 0: The Dedicated Enthusiasts | Cluster 1: The Long-Session Casuals | Cluster 2: The Fast & Light Users |
| :--- | :--- | :--- | :--- |
| **Segment Size** | 85 Users | 65 Users | 50 Users |
| **Workouts / Week** | **High** (~4.89) | **Low** (~1.57) | **Low** (~1.72) |
| **Avg Session Duration** | **Moderate** (~44.38 min) | **High** (~56.78 min) | **Low** (~26.63 min) |
| **Steps / Day** | **High** (~9,685) | **Moderate** (~7,684) | **Moderate** (~7,850) |
| **Observed Churn Rate** | **Extremely Low** (~7.06%) | **High Risk** (~20.00%) | **High Risk** (~20.00%) |

---

## 📈 Summary of Presentation Slides

This repository includes a 3-slide visual presentation pitch mapping the operational findings to core executive decisions:

* **Slide 1: Data Preprocessing & Pipeline Architecture**
  * Details the dataset profiles, structural transformations, addressing the anomalous negative metric for User #36, and features normalization workflows.
  * Displays the Elbow Curve chart justifying selecting $K=3$ clusters.
* **Slide 2: Behavioral Persona Discovery Matrix**
  * Breaks down the quantitative differences between *Dedicated Enthusiasts*, *Long-Session Casuals*, and *Fast & Light Users*.
  * Highlights how engagement rates directly inversely correlate with the recorded user churn metrics.
* **Slide 3: Strategic Value & Marketing Retention Roadmap**
  * **Retaining Cluster 1 & 2 (20% Churn):** Prescribes targeted push notifications mid-week encouraging quick milestone accomplishments and short-burst fitness content to bridge their lower workout frequencies.
  * **Leveraging Cluster 0 (7.06% Churn):** Outlines customer-advocacy premium conversion schemes to upsell subscription frameworks to our most highly active users.

---

## 📂 Repository Tree Structure

```text
├── Fitness_App_User_Data.xlsx      # Original raw dataset
├── clustering_analysis.py          # Production Python script for pipeline & execution
├── Elbow_Curve.png                 # Generated matplotlib visual elbow plot
├── Presentation_Slides.pdf         # Completed 3-slide stakeholder deck
└── README.md                       # Documentation file (This file)
