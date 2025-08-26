import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x = np.linspace(-5, 5, 400)

# Define the exponential function: f(x) = 2^x
y = np.exp(x)

# Create the plot
plt.plot(x, y)

# Add title and labels
plt.title('Exponential Function: f(x) = e^x')
plt.xlabel('x')
plt.ylabel('f(x)')

# Add grid for better readability
plt.grid(True)

# Show the plot
plt.show()
