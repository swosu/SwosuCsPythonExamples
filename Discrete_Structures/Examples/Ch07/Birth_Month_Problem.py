import pandas as pd
import os
import matplotlib.pyplot as plt

def birth_month_problem(n):
    months = 12
    probability = 1.0
    for i in range(n):
        probability *= (months - i) / months
    return probability

# Create an empty DataFrame
df = pd.DataFrame(columns=['People', 'No Shared Month (Decimal)', 'Shared Month (Decimal)'])

for i in range(1, 14):
    no_shared_month = birth_month_problem(i)
    shared_month = 1 - no_shared_month
    df = df.append({
        'People': i,
        'No Shared Month (Decimal)': no_shared_month,
        'Shared Month (Decimal)': shared_month,
    }, ignore_index=True)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['People'], df['Shared Month (Decimal)']*100, marker='o')
plt.title('Probability of People Sharing a Birth Month')
plt.xlabel('Number of People')
plt.ylabel('Probability (%)')
plt.grid(True)
plt.show()


# Output DataFrame to CSV file
df.to_csv('birth_month_probabilities.csv', index=False)

# Open CSV file
os.startfile('birth_month_probabilities.csv')