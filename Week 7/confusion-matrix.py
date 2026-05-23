import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix

# 1. Define the true labels and predicted labels based on the 30 test records
# Coding: 1 = Sick (Positive), 0 = Healthy (Negative)

# True labels: 15 Sick, 15 Healthy
y_true = [1] * 15 + [0] * 15

# Predicted labels:
# - 2 Sick predicted as Healthy (False Negatives) -> Changing two 1s to 0s
# - 1 Healthy predicted as Sick (False Positive) -> Changing one 0 to a 1
y_pred = ([1] * 13 + [0] * 2) + ([1] * 1 + [0] * 14)

# 2. Generate the confusion matrix array
cm = confusion_matrix(y_true, y_pred, labels=[1, 0])

# 3. Plot the confusion matrix using Seaborn
plt.figure(figsize=(6, 5))
labels = ["Sick (Pos)", "Healthy (Neg)"]

# Create a heatmap
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=labels,
    yticklabels=labels,
    cbar=False,
    annot_kws={"size": 14, "weight": "bold"},
)

# Formatting the plot layout
plt.title("Healthcare Model Confusion Matrix", fontsize=14, pad=15)
plt.xlabel("Actual Class", fontsize=12)
plt.ylabel("Predicted Class", fontsize=12)
plt.tight_layout()

# Display the figure
plt.show()

# 4. Print the performance metrics report
print("--- Classification Metrics Report ---")
print(classification_report(y_true, y_pred, target_names=labels))