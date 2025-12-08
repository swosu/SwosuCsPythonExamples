# Data Visualization Exercise - Shon Hakanson

# Import essential libraries for plotting and data handling
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import numpy as np

# --------------------------------------------
# Create random dataset for BONUS scatter plot
# --------------------------------------------
prices = np.random.uniform(5, 50, 50)     # Random float prices between 5 and 50
units  = np.random.randint(1, 200, 50)    # Random integer units sold
df2 = pd.DataFrame({'Price': prices, 'Units': units})  # DataFrame for scatter plot

# --------------------------------------------
# Create main DataFrame for Monthly Sales (Part 1 & Part 2 & Part 3)
# --------------------------------------------
data = { 
        'Month': ['January', 'February', 'March', 'April', 'May'], 
        'Sales': [2500, 3200, 2800, 4000, 3500] 
        } 
df = pd.DataFrame(data)

# ==================================================
# PART 1: Line Plot with Matplotlib (Static Plot)
# ==================================================
plt.figure(figsize=(10, 6))

# Plotting monthly sales as a line chart
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Data')  # Chart title

# NOTE: You may want to add explicit axis labels for full clarity in grading:
# plt.xlabel('Month')
# plt.ylabel('Sales (USD)')

plt.grid(True)                      # Add faint grid for readability
plt.xticks(rotation=0)              # Keep month labels horizontal
plt.tight_layout()                  # Prevent layout cutoff
plt.show()

# ==================================================
# PART 2: Bar Chart with Seaborn (Static Plot)
# ==================================================
sns.set(style="whitegrid")          # Use clean white grid style
plt.figure(figsize=(10, 6))

# Create bar chart of monthly sales
sns.barplot(x='Month', y='Sales', data=df, palette='Blues_d')
plt.title('Monthly Sales Data-Bar Chart')
plt.xlabel('Month')                 # X-axis label
plt.ylabel('Sales')                 # Y-axis label
plt.tight_layout()
plt.show()

# ==================================================
# PART 3: Interactive Line Plot with Plotly
# ==================================================
fig = px.line(
    df,
    x='Month',
    y='Sales',
    title='Monthly Sales Trend (Interactive)',
    markers=True                     # Add markers to each data point
)

# Change line color (optional customization)
fig.update_traces(line=dict(color='red'))
fig.show()

# ==================================================
# BONUS: Scatter Plot with Seaborn
# ==================================================

plt.figure(figsize=(7,5))

# Relationship between Price and Units Sold
sns.scatterplot(x='Price', y='Units', data=df2)
plt.title('Price vs Units Sold')
plt.tight_layout()
plt.show()

# ==================================================
# BONUS: Pie Chart with Plotly
# ==================================================
fig = px.pie(df, names='Month', values='Sales', title='Sales Share by Month')
fig.show()
