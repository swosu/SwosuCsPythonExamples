coin_names = {
    100: "$100 bill",
    50: "$50 bill",
    20: "$20 bill",
    10: "$10 bill",
    5: "$5 bill",
    1: "$1 bill",
    0.25: "Quarter",
    0.10: "Dime",
    0.05: "Nickel",
    0.01: "Penny"
}

def find_min_change(amount, denominations=None):
    if denominations is None:
        denominations = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]  # USD denominations
    
    change = []
    change_count = {}
    
    for coin in denominations:
        count = 0
        while amount >= coin:
            amount = round(amount - coin, 2)  # Prevent floating-point precision errors
            change.append(coin)
            count += 1
        if count > 0:
            change_count[coin] = count
    
    return change, change_count

# Example usage
if __name__ == "__main__":
    amount = float(input("Enter the amount of change: "))
    change, change_count = find_min_change(amount)
    print(f"Minimal change for {amount}: {change}")
    print("Breakdown:")
    for coin, count in change_count.items():
        print(f"{count} x {coin_names[coin]}")

