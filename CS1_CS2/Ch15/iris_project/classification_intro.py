# ============================================
# Predicting Categories: Getting Started
# ============================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from datetime import datetime
import os

# --- Load the Iris dataset ---
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

# --- Save instead of show ---
plt.savefig(filename, dpi=300, bbox_inches="tight")
plt.close()

print(f"\n✅ Pairplot saved as: {filename}")
