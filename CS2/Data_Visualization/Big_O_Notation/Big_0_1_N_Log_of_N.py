import matplotlib.pyplot as plt
import numpy as np

# Generate a larger array of input sizes (n)
n = np.logspace(1, 6, 500)  # From 10^1 to 10^6

# The time complexity O(1) is a constant
constant_time = np.ones_like(n)

# The time complexity O(n) is linear
linear_time = n

# The time complexity O(log n) is logarithmic
log_time = np.log(n)

# Plot with different line styles for black and white
plt.plot(n, constant_time, label="O(1)", linestyle='-', color='black', linewidth=3)
plt.plot(n, linear_time, label="O(n)", linestyle='--', color='black', linewidth=3)
plt.plot(n, log_time, label="O(log n)", linestyle='-.', color='black', linewidth=3)

# Set x and y axes to logarithmic scale
plt.xscale('log')
plt.yscale('log')

# Set font sizes for title, labels, and legend
plt.title('Big O Notation: O(1), O(n), O(log n)', fontsize=18)
plt.xlabel('Input Size (n)', fontsize=14)
plt.ylabel('Operations', fontsize=14)

# Adjust the font size of the legend
plt.legend(fontsize=12)

# Set the global font size for ticks
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Display the plot
plt.grid(True, which="both", ls="--")  # Use grid lines for better readability
plt.show()

print("Done.")
