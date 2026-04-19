
# Beijing Multi-Site Air Quality Analysis
**MSE803 - Week 2 Assignment 1**

This project performs a comprehensive exploratory data analysis (EDA) on hourly air quality data from multiple monitoring sites in Beijing.

## 📊 About the Data
The dataset captures environmental conditions from March 2013 to February 2017. Each row represents an hourly measurement including:
* **Pollution Levels:** PM2.5, PM10, SO2, NO2, CO, O3
* **Weather Data:** Temperature (TEMP), Pressure (PRES), Dew Point (DEWP)
* **Rainfall:** Precipitation (RAIN)
* **Wind Information:** Wind Direction (wd) and Wind Speed (WSPM)
* **Station:** The name of the monitoring site

## ✅ Tasks Performed

### Task 1: Data Loading & Inspection
* Loaded all CSV datasets from the multi-site directory.
* Merged individual station files into one master dataset.
* Displayed the first 5 rows for data verification.
* Identified column names and data types (Float64, Int64, and Object).
* Counted total rows and columns to ensure data integrity.

### Task 2: Data Cleaning
* Identified missing values across all parameters.
* Handled missing values by replacing them with the **Mean** of the column to maintain statistical consistency.
* Removed any remaining null rows that could not be imputed.

### Task 3: Statistical Analysis
Computed key metrics to understand the distribution of pollutants and weather variables.

#### **Summary Statistics Table**
| Metric | PM2.5 | PM10 | SO2 | NO2 | CO | TEMP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Mean** | 79.71 | 104.54 | 15.84 | 50.59 | 1228.96 | 13.56 |
| **Median** | 57.0 | 84.0 | 8.0 | 45.0 | 900.0 | 14.5 |
| **Std Dev** | 79.94 | 91.05 | 21.44 | 34.60 | 1129.81 | 11.43 |
| **Min** | 2.0 | 2.0 | 0.29 | 1.03 | 100.0 | -19.9 |
| **Max** | 999.0 | 999.0 | 500.0 | 290.0 | 10000.0 | 41.6 |

## 🧠 Simple Insights
* **High Variability:** The high standard deviation in PM2.5 (79.94) compared to the mean (79.71) indicates significant fluctuations in air quality, likely due to seasonal changes or specific pollution events.
* **Data Quality:** Missing values were present, likely due to sensor maintenance or technical issues at the monitoring sites.
* **Extreme Values:** Maximum values for PM2.5 and PM10 reached the 999 limit, indicating periods of extreme "hazardous" air quality.

## 🛠 Tools Used
* **Language:** Python
* **Library:** Pandas (for data manipulation and statistics)

## 🖼️ Output Screenshot
Below is the output generated from the analysis script:

![Analysis Outcome](file:///Users/earltavera/Desktop/MSE803/Week%202/Week2A1/code/week2a1-1.png)

## ▶️ How to Run
1. Ensure you have the datasets in the specified directory.
2. Install the required libraries:
   ```bash
   pip install pandas
