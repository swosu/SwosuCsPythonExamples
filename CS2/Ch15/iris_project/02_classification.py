# ============================================
# Classification Data Visualization and Split
# ============================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from datetime import datetime
import os

# --- Load the Iris dataset ---
print("\nLoading the Iris dataset...")
iris = datasets.load_iris()

# Convert to DataFrame
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df["target"] = iris.target

# --- Peek at the data ---
print("\nFirst 3 rows:")
print(iris_df.head(3))
print("\nLast 3 rows:")
print(iris_df.tail(3))

# --- Create a timestamped filename ---
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = "images"
os.makedirs(output_dir, exist_ok=True)
filename = f"{output_dir}/iris_pairplot_{timestamp}.png"

# --- Visualize relationships ---
sns.pairplot(iris_df, hue="target", corner=True, plot_kws={"s": 40})
plt.suptitle("Iris Dataset — Feature Relationships", y=1.02)
plt.savefig(filename, dpi=300, bbox_inches="tight")
plt.close()
print(f"\n✅ Pairplot saved as: {filename}")

# --- Display target class names ---
print("\nTarget names:")
print(iris.target_names)
print(f"\nExample target 0 corresponds to: {iris.target_names[0]}")

# --- Split dataset into training and testing sets ---
iris_train_ftrs, iris_test_ftrs, iris_train_tgt, iris_test_tgt = train_test_split(
    iris.data, iris.target, test_size=0.25, random_state=42
)

print("\nTrain features shape:", iris_train_ftrs.shape)
print("Test features shape:", iris_test_ftrs.shape)
print("Train targets shape:", iris_train_tgt.shape)
print("Test targets shape:", iris_test_tgt.shape)

print("\n✅ Data successfully split for model training and testing.")
