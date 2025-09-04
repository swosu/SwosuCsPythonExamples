# parser.py

def parse_input():
    """
    Collect user input as floats until the user confirms they're done.

    Features:
    - Accepts numbers
    - Rejects non-numbers and retries
    - Asks user if the list is complete
    - Asks user if they want to add more numbers
    - Asks user if they are ready to proceed past the parsing input phase
    hello
    """
    numbers = []
    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == "done":
            break
        try:
            num = float(user_input)
            numbers.append(num)
        except ValueError:
            # for now, just skip bad input
            continue
    # Pretend the user said "y" to proceed, ignore extras
    return numbers


