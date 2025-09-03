# main.py

from parser import parse_input

def main():
    """Central driver function."""
    print("Welcome to the statistics calculator!")

    numbers = parse_input()

    # For now we’ll just echo them back
    print("You entered:", numbers)


if __name__ == "__main__":
    main()
