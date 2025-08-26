import seaborn as sns
import pandas as pd

# Load sample dataset
tips = sns.load_dataset('tips')

# Create plot
sns.set_theme(style="whitegrid")
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title('Daily Total Bill Distribution')
plt.show()