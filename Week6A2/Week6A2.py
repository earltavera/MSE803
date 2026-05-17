import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Attribute names from wine.names
column_names = [
    'Class', 'Alcohol', 'Malic_acid', 'Ash', 'Alcalinity_of_ash',  
    'Magnesium', 'Total_phenols', 'Flavanoids', 'Nonflavanoid_phenols', 
    'Proanthocyanins', 'Color_intensity', 'Hue', 'OD280/OD315_of_diluted_wines', 'Proline'
]

# The URL of the dataset (or use your local 'wine.data' path)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"

# Load the dataset directly from the web
df = pd.read_csv(url, header=None, names=column_names)

# --- BASIC DATA ANALYSIS & CLEANING ---
print("--- Before Cleaning ---")
print(f"Dataset Size: {df.shape}")
print(f"Duplicates: {df.duplicated().sum()}")
print(f"Missing Values:\n{df.isnull().sum().sum()} total missing cells")

# Clean Data: Drop Duplicates
df.drop_duplicates(inplace=True)

# Clean Data: Drop Missing Values (if any)
df.dropna(inplace=True)

print("\n--- After Cleaning ---")
print(f"Dataset Size: {df.shape}")

# --- VISUALIZATION ---
# 1. Class Distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Class', palette='Set2')
plt.title('Distribution of Wine Classes')
plt.tight_layout()
plt.savefig('wine_class_distribution.png')
plt.clf()

# 2. Scatter Plot: Alcohol vs Color Intensity
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Alcohol', y='Color_intensity', hue='Class', palette='Set1', style='Class', s=100)
plt.title('Wine Separation: Alcohol vs Color Intensity')
plt.xlabel('Alcohol Content')
plt.ylabel('Color Intensity')
plt.tight_layout()
plt.savefig('wine_alcohol_vs_color.png')
plt.clf()

print("\nCharts saved as 'wine_class_distribution.png' and 'wine_alcohol_vs_color.png'.\n")

# --- ML PIPELINE ---
# Split features and target
X = df.drop('Class', axis=1)
y = df['Class']

# Standardize the features (recommended in wine.names for classifiers not scale invariant)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into training and testing sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42, stratify=y)

# Initialize and train the SVM model (using a linear kernel)
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = svm_model.predict(X_test)

# Compute the metrics before printing
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}\n")
print("Confusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(class_report)
print(f"\nModel Accuracy after cleaning: {accuracy:.4f}")