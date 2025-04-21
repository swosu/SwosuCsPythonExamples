import matplotlib.pyplot as plt
import numpy as np

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create plot
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)', color='blue')
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()