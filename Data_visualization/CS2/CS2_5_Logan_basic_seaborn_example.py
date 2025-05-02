import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset("tips")

# Create a scatter plot: total bill vs. tip
plt.figure(figsize=(8, 6))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", style="smoker")

# Add title and labels
plt.title("Total Bill vs Tip by Sex and Smoking Status")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.grid(True)

# Show plot
plt.show()
