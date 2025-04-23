import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load results
sort_results = pd.read_csv('sort_results.csv')
search_results = pd.read_csv('search_results.csv')

# Set style
sns.set_style('whitegrid')

# Plot 1: Sorting Time by Algorithm and Dataset Size
plt.figure(figsize=(12, 8))
sns.lineplot(data=sort_results, x='size', y='time', hue='algorithm', style='type')
plt.title('Sorting Algorithm Performance by Dataset Size and Type')
plt.xlabel('Dataset Size')
plt.ylabel('Time (seconds)')
plt.yscale('log')
plt.savefig('sorting_time_comparison.png')
plt.close()

# Plot 2: Sorting Comparisons by Algorithm
plt.figure(figsize=(12, 8))
sns.barplot(data=sort_results, x='algorithm', y='comparisons', hue='type')
plt.title('Number of Comparisons by Sorting Algorithm')
plt.xlabel('Algorithm')
plt.ylabel('Comparisons (log scale)')
plt.yscale('log')
plt.savefig('sorting_comparisons.png')
plt.close()

# Plot 3: Searching Time by Algorithm and Dataset Size
plt.figure(figsize=(12, 8))
sns.lineplot(data=search_results, x='size', y='time', hue='algorithm', style='type')
plt.title('Search Algorithm Performance by Dataset Size and Type')
plt.xlabel('Dataset Size')
plt.ylabel('Time (seconds)')
plt.yscale('log')
plt.savefig('search_time_comparison.png')
plt.close()

# Plot 4: Sorting Algorithm Memory Usage
plt.figure(figsize=(12, 8))
sns.boxplot(data=sort_results, x='algorithm', y='memory')
plt.title('Memory Usage by Sorting Algorithm')
plt.xlabel('Algorithm')
plt.ylabel('Memory Usage (bytes)')
plt.savefig('sorting_memory.png')
plt.close()

print("Visualizations created and saved!")