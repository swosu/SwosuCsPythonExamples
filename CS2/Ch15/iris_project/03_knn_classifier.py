# ============================================
# 03_knn_classifier.py
# Building and Evaluating a k-NN Classifier
# ============================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets, neighbors, metrics
from sklearn.model_selection import train_test_split
from datetime import datetime
import os

# --- Load the Iris dataset ---
iris = datasets.load_iris()

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df["target"] = iris.target

# --- Train/test split ---
iris_train_ftrs, iris_test_ftrs, iris_train_tgt, iris_test_tgt = train_test_split(
    iris.data, iris.target, test_size=0.25, random_state=42
)

print(f"Training samples: {iris_train_ftrs.shape[0]}, Test samples: {iris_test_ftrs.shape[0]}")

# --- Build a k-NN classifier (k=3) ---
knn = neighbors.KNeighborsClassifier(n_neighbors=3)
knn.fit(iris_train_ftrs, iris_train_tgt)

# --- Predict on test set ---
preds = knn.predict(iris_test_ftrs)

# --- Evaluate accuracy ---
accuracy = metrics.accuracy_score(iris_test_tgt, preds)
print(f"\n✅ 3-NN Model Accuracy: {accuracy:.2f}")

# --- Save a results log ---
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
os.makedirs("results", exist_ok=True)
logfile = f"results/knn_results_{timestamp}.csv"

results_df = pd.DataFrame({
    "Actual": iris_test_tgt,
    "Predicted": preds
})
results_df.to_csv(logfile, index=False)
print(f"Results saved to: {logfile}")

# --- Optional visualization: confusion matrix ---
conf_matrix = metrics.confusion_matrix(iris_test_tgt, preds)
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues",
            xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.title(f"3-NN Confusion Matrix (Accuracy: {accuracy:.2f})")
plt.xlabel("Predicted")
plt.ylabel("Actual")

os.makedirs("images", exist_ok=True)
imgfile = f"images/knn_confusion_{timestamp}.png"
plt.savefig(imgfile, dpi=300, bbox_inches="tight")
plt.close()

print(f"Confusion matrix image saved as: {imgfile}")
