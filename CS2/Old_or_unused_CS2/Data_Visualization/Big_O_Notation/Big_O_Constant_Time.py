import matplotlib.pyplot as plt
import numpy as np

# Generate an array of input sizes (n)
n = np.linspace(1, 100, 100)

# The time complexity O(1) is a constant
constant_time = np.ones_like(n)

# Create the plot
plt.plot(n, constant_time, label="O(1)", color='blue')

# Add labels and title
plt.xlabel('Input Size (n)')
plt.ylabel('Operations')
plt.title('Big O Notation: Constant Time Complexity O(1)')

# Add a legend
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
