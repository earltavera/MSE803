Housing Price Analysis: Decoding Value Beyond Square Footage
Project Overview
This project performs a Descriptive Analysis on a housing dataset of 545 properties to identify the key drivers of market value. While property size is a fundamental factor, this study explores how amenities (like Air Conditioning) and location prestige create significant price premiums.

Key Findings (The "Story")
The analysis reveals that housing value is driven by a hierarchy of factors:

The Physical Baseline: There is a moderate correlation between land area and price, but size alone does not dictate the final valuation.

The Luxury Factor: Amenities like Air Conditioning and Furnishing Status are the strongest drivers of "Premium" pricing. Houses with AC average $6.01M, compared to $4.19M for those without.

Location Premium: Properties in "Preferred Areas" command an average premium of $1.4M, regardless of their physical specs.

Data Quality
Dataset Size: 545 rows, 13 columns.

Completeness: 100% (Zero missing values detected during the data integrity check).

Tech Stack
Language: Python 3.x

Libraries: - Pandas: For data loading and descriptive aggregation.

Matplotlib & Seaborn: For statistical data visualization.

Visualizations
The repository includes scripts to generate the following insights:

Price vs. Area: A scatter plot visualizing the base correlation of size and cost.

The AC Premium: A bar chart illustrating the price gap between conditioned and non-conditioned homes.

Location Impact: A comparison of valuations across different neighborhoods.

How to Run
Clone the repository:

Bash
git clone https://github.com/yourusername/housing-analysis.git
Install dependencies:

Bash
pip install pandas seaborn matplotlib
Run the analysis:

Bash
python housing_analysis.py
Author
Earl Tavera Master of Software Engineering Student | Yoobee College
