"""
01_gallons_input_try_except.py

Goal:
- Ask the user for the number of gallons.
- Use try/except to handle bad input (like "ten" or "3.5").
- Keep asking until we get a valid non-negative integer.
"""




def get_gallons_from_user() -> int:
    """
    Repeatedly prompt the user until they enter a valid non-negative integer.
    Returns:
        int: The number of gallons as an integer.
    """
    while True:
        user_text = input("Enter the number of gallons (whole number, 0 or more): ")

        try:
            # First check if input is numeric
            if not user_text.isnumeric():
                raise ValueError("Input must be numeric characters only.")
            
            gallons = int(user_text)  # This is the risky line: it may raise ValueError.
        except ValueError as e:
            if "numeric" in str(e):
                print("❌ Input must contain only numeric digits. Try something like 0, 3, or 12.")
            else:
                print("❌ That was not a whole number. Try something like 0, 3, or 12.")
            continue  # Go back to the top of the loop and ask again.

        # If we got here, int(...) worked, so gallons is an integer.
        if gallons < 0:
            print("❌ Gallons cannot be negative. Try again.")
            continue

        return gallons


def main() -> None:
    gallons = get_gallons_from_user()
    print(f"✅ Thanks! You entered {gallons} gallon(s).")


if __name__ == "__main__":
    main()
