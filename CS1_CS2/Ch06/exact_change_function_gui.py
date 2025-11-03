def exact_change(total_cents):
    quarters = total_cents // 25
    total_cents %= 25
    dimes = total_cents // 10
    total_cents %= 10
    nickels = total_cents // 5
    total_cents %= 5
    pennies = total_cents

    return quarters, dimes, nickels, pennies

def main():
    total_cents = int(input("Enter the total change in cents: "))
    if total_cents <= 0:
        print("no change")
    else:
        quarters, dimes, nickels, pennies = exact_change(total_cents)
        if quarters > 0:
            print(f"{quarters} quarter(s)")
        if dimes > 0:
            print(f"{dimes} dime(s)")
        if nickels > 0:
            print(f"{nickels} nickel(s)")
        if pennies > 0:
            print(f"{pennies} penny(ies)")

if __name__ == "__main__":
    main()