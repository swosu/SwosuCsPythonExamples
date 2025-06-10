print("hello")

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Month': ['January', 'February', 'March', 'April', 'May'],
    'Sales': [2500, 3200, 2800, 4000, 3500]
}
df = pd.DataFrame(data)

# Part 1: Line Plot with Matplotlib
plt.figure(figsize=(8, 6))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales (in USD)')
plt.grid(True)
plt.show()

# Part 2: Bar Plot with Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.barplot(x='Month', y='Sales', data=df, palette='Blues')
plt.title('Monthly Sales - Bar Plot')
plt.show()

# Part 3: Interactive Line Plot with Plotly
fig = px.line(df, x='Month', y='Sales', 
              title='Monthly Sales Trend (Interactive)', 
              markers=True)
fig.show()
