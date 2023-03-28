import csv
import random

# Set the filename to <city_count>.csv and the number of rows and columns to <city_count>
city_count = 1000
filename = f'{city_count}.csv'
num_rows = city_count
num_cols = city_count

# Generate random data
data = [[random.randint(2, 200) for j in range(num_cols)] for i in range(num_rows)]

# Write data to CSV file
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)