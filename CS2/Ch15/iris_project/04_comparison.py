# ============================================
# 04_comparison.py
# Comparing k-NN and Naive Bayes Classifiers
# ============================================

import time
import pandas as pd
from sklearn import datasets, metrics, model_selection, neighbors, naive_bayes
from datetime import datetime
import os

try:
    # memory_profiler is optional, install if missing
    from memory_profiler import memory_usage
    mem_profiling = True
except ImportError:
    print("⚠️  memory_profiler not found. Run: pip install memory_profiler")
    mem_profiling = False

# --- Load the Iris dataset ---
iris = datasets.load_iris()

# --- Train/Test Split ---
iris_train_ftrs, iris_test_ftrs, iris_train_tgt, iris_test_tgt = model_selection.train_test_split(
    iris.data, iris.target, test_size=0.25, random_state=42
)

# --- Model definitions ---
models = {
    "k-NN": neighbors.KNeighborsClassifier(n_neighbors=3),
    "Naive Bayes": naive_bayes.GaussianNB()
}

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
os.makedirs("results", exist_ok=True)
results_file = f"results/classifier_comparison_{timestamp}.csv"

results = []

print("\n🚀 Starting classifier comparison...\n")

for name, model in models.items():
    # Measure training time and memory
    start_time = time.perf_counter()
    if mem_profiling:
        mem_used = memory_usage((model.fit, (iris_train_ftrs, iris_train_tgt)), max_iterations=1)
        mem_peak = max(mem_used) - min(mem_used)
    else:
        model.fit(iris_train_ftrs, iris_train_tgt)
        mem_peak = float("nan")

    fit_time = (time.perf_counter() - start_time) * 1000  # ms

    # Measure prediction time
    start_time = time.perf_counter()
    predictions = model.predict(iris_test_ftrs)
    pred_time = (time.perf_counter() - start_time) * 1000  # ms

    # Accuracy
    score = metrics.accuracy_score(iris_test_tgt, predictions)

    results.append({
        "Model": name,
        "Accuracy": round(score, 3),
        "Fit Time (ms)": round(fit_time, 3),
        "Predict Time (ms)": round(pred_time, 3),
        "Memory Used (MiB)": round(mem_peak, 4)
    })

    print(f"{name:>12s} | Accuracy: {score:.3f} | Fit: {fit_time:.2f} ms | "
          f"Predict: {pred_time:.2f} ms | Mem Δ: {mem_peak:.4f} MiB")

# --- Save results to CSV ---
results_df = pd.DataFrame(results)
results_df.to_csv(results_file, index=False)
print(f"\n✅ Results saved to: {results_file}")

# --- Visualization ---
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("images", exist_ok=True)
plt.figure(figsize=(8, 5))
sns.barplot(data=results_df, x="Model", y="Accuracy", palette="viridis")
plt.title("Classifier Accuracy Comparison")
plt.ylim(0, 1.05)
plt.grid(axis="y", linestyle="--", alpha=0.6)

imgfile = f"images/classifier_accuracy_{timestamp}.png"
plt.savefig(imgfile, dpi=300, bbox_inches="tight")
plt.close()

print(f"📊 Accuracy chart saved as: {imgfile}")

plt.figure(figsize=(8, 5))
sns.barplot(data=results_df.melt(id_vars=["Model"], 
                                 value_vars=["Fit Time (ms)", "Predict Time (ms)"],
                                 var_name="Stage", value_name="Time (ms)"),
            x="Model", y="Time (ms)", hue="Stage", palette="magma")
plt.title("Training vs. Prediction Time")
plt.grid(axis="y", linestyle="--", alpha=0.6)

imgfile2 = f"images/classifier_time_{timestamp}.png"
plt.savefig(imgfile2, dpi=300, bbox_inches="tight")
plt.close()

print(f"📈 Time comparison chart saved as: {imgfile2}\n")

print("🎉 Comparison complete! Check your 'results' and 'images' folders.\n")
