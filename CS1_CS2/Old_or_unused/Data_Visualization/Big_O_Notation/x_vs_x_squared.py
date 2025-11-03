import matplotlib.pyplot as plt
import numpy as np

# Generate an array of x values
x = np.linspace(-10, 10, 1000)

# Compute y as x^2
y = x ** 2

# Create the plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('x')
plt.ylabel('x^2')
plt.title('Plot of x versus x^2')

# Display the plot
plt.grid(True)
plt.show()
