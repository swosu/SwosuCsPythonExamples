import matplotlib.pyplot as plt
import pandas as pd

file = input()
df = pd.read_csv(file)

df.insert(4, 'Size', df['Gross Potential']/2)
print(df)

plt.scatter(df['Capacity'], df['Gross Potential'], marker='x', color='green', s=df['Size'])

# Add axes labels and title
plt.xlabel('Capacity', fontsize = 10)
plt.ylabel('Gross Potential', fontsize = 10)
plt.title('Gross Potential vs Capacity', fontsize = 16)
plt.grid(linestyle='--')

plt.savefig('images/output_fig.png')