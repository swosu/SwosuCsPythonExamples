import matplotlib.pyplot as plt

# Example data
months = ['January', 'February', 'March', 'April']
sales = [1500, 1800, 1700, 2100]

# Create a bar chart
plt.bar(months, sales, color='skyblue')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True, linestyle='--', alpha=0.5)

# Show the plot
plt.show()
