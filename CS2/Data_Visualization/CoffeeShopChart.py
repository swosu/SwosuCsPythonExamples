import numpy as np
import matplotlib.pyplot as plt

# Coffee shop names
coffee_shops = ['Shop A', 'Shop B', 'Shop C', 'Shop D', 'Shop E']

# Sales data for 5 days (rows: coffee shops, columns: days)
sales_data = np.array([
    [120, 130, 125, 140, 135],  # Shop A
    [150, 140, 155,160, 145],  # Shop B
    [90, 100, 95, 110, 105],    # Shop C
    [200, 190, 205, 210, 195],  # Shop D
    [180, 175, 185, 190, 170]       # Shop E
])

# Days
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']

# Plotting the data
for i, shop in enumerate(coffee_shops):
    plt.plot(days, sales_data[i], label=shop)

# Chart customization
plt.title('Coffee Shop Sales Over 5 Days')
plt.xlabel('Days')
plt.ylabel('Sales')
plt.legend()
plt.grid(False)

# Show the chart
plt.tight_layout()
plt.show()