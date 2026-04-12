Week 1 - Activity 1: Descriptive Analysis via Data Aggregation

Project Overview
This project performs a descriptive analysis on a sales dataset to identify trends and performance metrics across different product categories. Using Python and Pandas, we aggregated raw transaction data to calculate total revenue, average sales, and volume per category.

Dataset Summary
The analysis focuses on three main categories (A, B, and C) using the following metrics:
- **sales_sum**: Total revenue generated.
- **sales_mean**: Average revenue per transaction.
- **sales_count**: Total number of transactions.
- **quantity_sum**: Total number of items sold.

| Category | Total Sales | Avg Sales | Count | Total Quantity |
| :--- | :--- | :--- | :--- | :--- |
| **A** | $18,010 | $545.76 | 33 | 282 |
| **B** | $22,154 | $615.39 | 36 | 343 |
| **C** | $18,213 | $587.52 | 31 | 273 |

Key Insights (The "Story")
- **Category B** is the market leader, contributing the highest volume and value to the business.
- **Category C** shows higher efficiency than A, producing more revenue despite having the fewest number of transactions.
- **Category A** represents a high-frequency but low-value segment, suggesting a need for "upselling" strategies.

Visualizations
The following chart illustrates the comparison between revenue and quantity across the segments:
![Sales Summary](sales_summary.png)# MSE803
