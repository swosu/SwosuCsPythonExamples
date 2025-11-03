import pandas as pd

# URL of the dataset on GitHub
#url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/births/births.csv"
url = "https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/births/US_births_2000-2014_SSA.csv"

# Step 1: Load the dataset directly from the URL into a pandas DataFrame
try:
    data = pd.read_csv(url)
    print("Data loaded successfully!")
except Exception as e:
    print(f"An error occurred: {e}")

# Step 2: Display the first few rows to verify the data
print(data.head())

# Step 3: Perform basic analysis (Optional)
# Example: Calculate the average number of births by day of the week
avg_births_by_day = data.groupby('day_of_week')['births'].mean()
print("\nAverage births by day of the week:")
print(avg_births_by_day)

# Save a local copy (Optional)
data.to_csv('births_data.csv', index=False)
print("\nA local copy has been saved as 'births_data.csv'.")
