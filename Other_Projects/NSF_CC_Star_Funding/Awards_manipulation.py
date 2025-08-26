import csv

# Open the CSV file for reading
with open('Awards.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    
    # Skip the header row if it exists
    next(reader)
    
    # Initialize a dictionary to store state-wise totals
    state_totals = {}
    
    # Iterate over each row in the CSV file
    for row in reader:
        state = row[0]  # Assuming the state is in the first column
        amount = float(row[1].replace('$', '').replace(',', ''))  # Assuming the amount is in the second column
        
        # Add the amount to the state's total
        state_totals[state] = state_totals.get(state, 0) + amount

# Print the state-wise totals
for state, total in state_totals.items():
    print(f"{state}: {total}")

