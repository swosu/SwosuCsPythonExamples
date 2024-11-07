import matplotlib.pyplot as plt
import pandas as pd

file1 = input()
file2 = input()

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

print(df1)
print(df2)

plt.subplot(1,2,1)
plt.scatter(df1['Gross Potential'], df1['Capacity'])
plt.title('July 2002')
plt.ylabel('Capacity')
plt.xlabel('Gross Potential')

plt.subplot(1,2,2)
plt.scatter(df2['Gross Potential'], df2['Capacity'])
plt.title('December 2002')
plt.xlabel('Gross Potential')

plt.suptitle('Capacity vs. Gross Potential')

plt.savefig('subplots.png')