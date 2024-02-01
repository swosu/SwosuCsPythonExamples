import random

# Function to calculate change denominations
def calculate_change(total, payment):
    # Check if payment is sufficient
    if payment < total:
        print("Insufficient payment!")
        return

    # Define the available denominations
    denominations = {
        50: "Fifty-dollar bills",
        20: "Twenty-dollar bills",
        10: "Ten-dollar bills",
        5: "Five-dollar bills",
        2: "Two-dollar bills",
        1: "One-dollar bills",
        0.5: "Half-dollars",
        0.25: "Quarters",
        0.1: "Dimes",
        0.05: "Nickels",
        0.01: "Pennies",
    }

    # Calculate the change amount
    change = payment - total
    change_dict = {}

    # Calculate the number of each denomination
    for denom, denom_name in denominations.items():
        num_denom = int(change / denom)
        if num_denom > 0:
            change_dict[denom_name] = num_denom
            change -= num_denom * denom

    # Print the change denominations
    for denom_name, count in change_dict.items():
        if count == 1:
            print(f"{count} {denom_name[:-1]}")
        else:
            print(f"{count} {denom_name}")

# Generate random total and payment values
total_value = round(random.uniform(0.01, 100), 2)
payment_value = round(random.uniform(total_value + 0.01, total_value + 100), 2)

print(f"Total Amount: ${total_value}")
print(f"Payment Amount: ${payment_value}")

# Calculate and print change denominations
calculate_change(total_value, payment_value)
