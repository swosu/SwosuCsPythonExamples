# Function to calculate the change for a given amount
def calculate_change(amount):
    # Define the available denominations (from largest to smallest)
    denominations = [100, 50, 20, 10, 5, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    
    # Dictionary to hold the result of change breakdown
    change = {}
    
    # Loop through each denomination
    for denom in denominations:
        count = int(amount // denom)  # Find how many times this denomination can fit in the remaining amount
        if count > 0:
            change[denom] = count  # Store the count for this denomination
        amount -= count * denom  # Subtract the equivalent amount from the total
        amount = round(amount, 2)  # Round to avoid floating-point precision issues
    
    return change

# Function to print the change in a readable format
def print_change(change):
    for denom, count in change.items():
        print(f"${denom} x {count}")

# Main function to run the program
def main():
    # Get user input for the amount
    amount = float(input("Enter the amount for change: "))
    
    # Calculate the change
    change = calculate_change(amount)
    
    # Display the result
    print("Change breakdown:")
    print_change(change)

# Execute the program
if __name__ == "__main__":
    main()
