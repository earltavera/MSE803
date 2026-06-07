import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Load Data
df = pd.read_excel('/Users/earltavera/Desktop/MSE803/Week 9/Fitness_App_User_Data.xlsx')

# 2. Data Cleaning
print("Initial Missing Values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# Correct the negative value in Avg_Session_Duration_Min (User_ID 36)
df['Avg_Session_Duration_Min'] = df['Avg_Session_Duration_Min'].abs()

# 3. Feature Selection & Scaling
# Selecting behavior-based numerical metrics for clustering
features = ['Workouts_per_Week', 'Avg_Session_Duration_Min', 'Steps_per_Day']
X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Finding Optimal Clusters via Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot the Elbow Method
plt.figure(figsize=(8, 4))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('Elbow Method to Determine Optimal Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# 5. Applying K-Means (Optimal Clusters = 3)
optimal_clusters = 3
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# 6. Profile the Clusters
cluster_profile = df.groupby('Cluster')[features + ['Age', 'Churned']].mean()
print("\nCluster Profiles (Averages):")
print(cluster_profile)

# Count users per cluster
print("\nUser Count per Cluster:\n", df['Cluster'].value_counts())