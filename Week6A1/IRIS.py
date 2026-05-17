import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# --- 1. Load and Explore Data ---
df = pd.read_csv('/Users/earltavera/Desktop/MSE803/Week 6/Iris.csv')
print(df.head())

print("\n--- INFO ---")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nSpecies distribution:")
print(df['Species'].value_counts())

print("\nDuplicates (ignoring Id):")
print(df.drop(columns=['Id']).duplicated().sum())
print(df[df.drop(columns=['Id']).duplicated(keep=False)])

# --- 2. Clean and Save Data ---
# Drop the 'Id' column as it's not an input feature
df_clean = df.drop(columns=['Id'])
df_clean.to_csv('cleaned_iris_from_csv.csv', index=False)

# --- 3. Visualize Data ---
# Petal Metrics Chart
plt.clf()
sns.scatterplot(data=df, x='PetalLengthCm', y='PetalWidthCm', hue='Species', style='Species', palette='Set1')
plt.title('Iris Species Separation by Petal Metrics (from Iris.csv)')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.tight_layout()
plt.savefig('iris_csv_petal_chart.png')

# Sepal Metrics Chart
plt.clf()
sns.scatterplot(data=df, x='SepalLengthCm', y='SepalWidthCm', hue='Species', style='Species', palette='Set1')
plt.title('Iris Species Separation by Sepal Metrics (from Iris.csv)')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.tight_layout()
plt.savefig('iris_csv_sepal_chart.png')
plt.clf()

# --- 4. Split Features and Target ---
X = df_clean.drop(columns=['Species'])
y = df_clean['Species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# --- 5. Train Model ---
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# --- 6. Predict and Evaluate ---
y_pred = model.predict(X_test)

print("\n--- Evaluation Metrics ---")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nClasses Order:", model.classes_)