# factorial_calculator.py

def ask_for_user_input():
    """Ask the user which number they want the factorial of."""
    while True:
        try:
            your_number = int(input("What number would you like to find the factorial of? "))
            if your_number < 0:
                print("Factorial is not defined for negative numbers. Try again!")
                continue
            return your_number
        except ValueError:
            print("Please enter a valid integer!")

def factorial(n):
    """Compute n! recursively."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    """Main function to run the factorial program."""
    print("Welcome to the Factorial Finder!")
    number = ask_for_user_input()
    result = factorial(number)
    print(f"\nThe factorial of {number} is: {result}")

if __name__ == "__main__":
    main()

