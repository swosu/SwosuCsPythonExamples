import matplotlib.pyplot as plt
import numpy as np

# Generate an array of input sizes (n)
n = np.linspace(1, 100, 100)

# The time complexity O(1) is a constant
constant_time = np.ones_like(n)

# The time complexity O(n) is linear
linear_time = n

# Adjust line thickness and font sizes
plt.plot(n, constant_time, label="O(1)", color='blue', linewidth=3)
plt.plot(n, linear_time, label="O(n)", color='green', linewidth=3)

# Set font sizes for title, labels, and legend
plt.title('Big O Notation: O(1) and O(n)', fontsize=18)
plt.xlabel('Input Size (n)', fontsize=14)
plt.ylabel('Operations', fontsize=14)

# Adjust the font size of the legend
plt.legend(fontsize=12)

# Set the global font size for ticks
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Display the plot
plt.grid(True)
plt.show()
