import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    'Book Title': [
        'The Silent Lake', 'Gardens of Tomorrow', 'Rising Embers', 'The Last Architect',
        'Code of Dreams', 'Forest of Mist', 'Space Between Stars', 'Betrayal\'s Price',
        'Broken Crown', 'The Vanishing Night', 'Quantum Vortex', 'The Final Empire'
    ],
    'Genre': [
        'Mystery', 'Sci-Fi', 'Fantasy', 'Mystery',
        'Sci-Fi', 'Fantasy', 'Sci-Fi', 'Thriller',
        'Fantasy', 'Mystery', 'Sci-Fi', 'Thriller'
    ],
    'Author': [
        'Alice Monroe', 'Ben Watts', 'Carla Hill', 'Alice Monroe',
        'Derek Yu', 'Carla Hill', 'Ben Watts', 'Eliza Quinn',
        'Carla Hill', 'Alice Monroe', 'Derek Yu', 'Eliza Quinn'
    ],
    'Price': [15, 20, 18, 15, 22, 18, 20, 25, 18, 15, 22, 25],
    'Copies Sold': [120, 85, 140, 100, 90, 130, 95, 75, 160, 110, 105, 85],
    'Month': [
        'January', 'January', 'February', 'February',
        'March', 'March', 'April', 'April',
        'May', 'May', 'June', 'June'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Add Revenue column
df['Revenue'] = df['Price'] * df['Copies Sold']

# 1. Total copies sold by genre
genre_sales = df.groupby('Genre')['Copies Sold'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=genre_sales.index, y=genre_sales.values, palette='viridis')
plt.title('Total Copies Sold by Genre')
plt.ylabel('Copies Sold')
plt.xlabel('Genre')
plt.show()

# 2. Top 5 best-selling authors
author_sales = df.groupby('Author')['Copies Sold'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=author_sales.index, y=author_sales.values, palette='magma')
plt.title('Top 5 Authors by Copies Sold')
plt.ylabel('Copies Sold')
plt.xlabel('Author')
plt.show()

# 3. Total sales revenue by month
month_revenue = df.groupby('Month')['Revenue'].sum()
# To keep months in order
month_order = ['January', 'February', 'March', 'April', 'May', 'June']
month_revenue = month_revenue.reindex(month_order)

plt.figure(figsize=(8,5))
sns.lineplot(x=month_revenue.index, y=month_revenue.values, marker='o')
plt.title('Total Sales Revenue by Month')
plt.ylabel('Revenue ($)')
plt.xlabel('Month')
plt.show()

# 4. Price vs Copies Sold
plt.figure(figsize=(8,5))
sns.scatterplot(x=df['Price'], y=df['Copies Sold'], hue=df['Genre'], s=100)
plt.title('Price vs Copies Sold')
plt.xlabel('Price ($)')
plt.ylabel('Copies Sold')
plt.legend(title='Genre')
plt.show()
