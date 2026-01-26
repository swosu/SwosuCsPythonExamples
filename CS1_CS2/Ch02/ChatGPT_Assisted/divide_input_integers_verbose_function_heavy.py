"""
Divide Input Integers (Verbose + Function Explorer Edition)

What this program does:
- Reads a numerator (top number) and a divisor (bottom number).
- Divides three times.
- After each division, it floors the result and reports the "lost" fractional amount.
- Prints every step verbosely so you can see exactly what happened and when printing happened.

Interactive Help Mode:
- At the main menu, press:
    h  -> open function explorer (shows a numbered function list)
    r  -> run the divider
    q  -> quit

Inside Help Mode:
- Pick a number to view a function’s docstring.
- Then choose:
    b  -> back to function list
    c  -> return to calculator menu
    q  -> quit program

Python introspection tip:
- In a Python REPL, you can run:
    import divide_input_integers_verbose_function_heavy as m
    help(m.get_top_number)
"""

import math
import inspect


def verbose_print(message: str) -> None:
    """
    Print a message with extra visibility around printing.

    This function announces:
    - before printing
    - what message is being printed
    - after printing

    Usage:
        verbose_print("Hello!")
    """
    print("\n[PRINT ABOUT TO HAPPEN]")
    print(message)
    print("[PRINT COMPLETED]")


def get_top_number() -> int:
    """
    Prompt for the numerator (top number) and return it as an integer.

    Terminology:
    - Numerator: the top number in a division problem.

    Returns:
        int: the user-entered numerator.
    """
    while True:
        raw_input_text = input("Enter the TOP number (numerator): ")
        try:
            numerator = int(raw_input_text)
            verbose_print(f"Captured numerator = {numerator}")
            return numerator
        except ValueError:
            verbose_print(f"'{raw_input_text}' is not a valid integer. Try again.")


def get_bottom_number() -> int:
    """
    Prompt for the divisor (bottom number) and return it as an integer.

    Terminology:
    - Divisor: the number you divide by (bottom number).

    Rules:
    - Divisor cannot be 0.

    Returns:
        int: the user-entered divisor.
    """
    while True:
        raw_input_text = input("Enter the BOTTOM number (divisor): ")
        try:
            divisor = int(raw_input_text)

            if divisor == 0:
                verbose_print("Divisor cannot be 0. Please enter a non-zero integer.")
                continue

            verbose_print(f"Captured divisor = {divisor}")
            return divisor
        except ValueError:
            verbose_print(f"'{raw_input_text}' is not a valid integer. Try again.")


def calculate_exact_division(numerator: int, divisor: int) -> float:
    """
    Perform exact division and return the full float result.

    This is NOT floor division. This keeps the fractional part.

    Args:
        numerator (int): top number
        divisor (int): bottom number

    Returns:
        float: numerator / divisor
    """
    verbose_print(f"About to compute exact division: {numerator} / {divisor}")
    exact_result = numerator / divisor
    verbose_print(f"Exact division result = {exact_result}")
    return exact_result


def floor_and_report_loss(exact_value: float) -> tuple[int, float]:
    """
    Floor a float to an integer and report what was removed.

    Important behavior note:
    - math.floor() always goes toward negative infinity.
      Example: math.floor(-3.2) == -4

    Loss is defined as:
        exact_value - floored_value

    Args:
        exact_value (float): value to floor

    Returns:
        tuple[int, float]: (floored_value, lost_fraction)
    """
    verbose_print(f"About to floor the value: {exact_value}")

    floored_value = math.floor(exact_value)
    lost_fraction = exact_value - floored_value

    verbose_print(f"Floored value = {floored_value}")
    verbose_print(f"Amount lost due to flooring = {lost_fraction}")

    return floored_value, lost_fraction


def first_division_step(current_value: int, divisor: int) -> float:
    """
    Perform the first exact division step.

    Returns:
        float: exact result of current_value / divisor
    """
    verbose_print("=== FIRST DIVISION STEP (Exact) ===")
    return calculate_exact_division(current_value, divisor)


def first_rounding_step(exact_value: float) -> int:
    """
    Perform the first rounding step: floor the value and report loss.

    Returns:
        int: floored integer result
    """
    verbose_print("=== FIRST ROUNDING STEP (Floor + Loss) ===")
    floored_value, _ = floor_and_report_loss(exact_value)
    return floored_value


def second_division_step(current_value: int, divisor: int) -> float:
    """
    Perform the second exact division step.

    Returns:
        float: exact result of current_value / divisor
    """
    verbose_print("=== SECOND DIVISION STEP (Exact) ===")
    return calculate_exact_division(current_value, divisor)


def second_rounding_step(exact_value: float) -> int:
    """
    Perform the second rounding step: floor the value and report loss.

    Returns:
        int: floored integer result
    """
    verbose_print("=== SECOND ROUNDING STEP (Floor + Loss) ===")
    floored_value, _ = floor_and_report_loss(exact_value)
    return floored_value


def third_division_step(current_value: int, divisor: int) -> float:
    """
    Perform the third exact division step.

    Returns:
        float: exact result of current_value / divisor
    """
    verbose_print("=== THIRD DIVISION STEP (Exact) ===")
    return calculate_exact_division(current_value, divisor)


def third_rounding_step(exact_value: float) -> int:
    """
    Perform the third rounding step: floor the value and report loss.

    Returns:
        int: floored integer result
    """
    verbose_print("=== THIRD ROUNDING STEP (Floor + Loss) ===")
    floored_value, _ = floor_and_report_loss(exact_value)
    return floored_value


def ask_run_again() -> bool:
    """
    Ask if the user wants to run the divider again.

    Returns:
        bool: True if yes, False if no
    """
    while True:
        raw_choice = input("\nRun again? (y/n): ").strip().lower()
        if raw_choice in ("y", "yes"):
            verbose_print("User chose to run again.")
            return True
        if raw_choice in ("n", "no"):
            verbose_print("User chose to stop.")
            return False
        verbose_print("Please type 'y' or 'n'.")


def get_local_functions() -> list[tuple[str, object]]:
    """
    Return a sorted list of (function_name, function_object) for functions defined in this module.

    Filters out imported functions and internal dunder names.

    Returns:
        list[tuple[str, object]]: sorted by function name
    """
    current_module = inspect.getmodule(get_local_functions)
    items = []

    for name, value in current_module.__dict__.items():
        if inspect.isfunction(value) and value.__module__ == current_module.__name__:
            if not name.startswith("__"):
                items.append((name, value))

    return sorted(items, key=lambda pair: pair[0])


def show_help_mode() -> None:
    """
    Interactive function explorer.

    Flow:
    - Show numbered list of functions.
    - User selects a number to view docstring.
    - User can return to list, return to calculator menu, or quit.
    """
    functions = get_local_functions()

    while True:
        verbose_print("=== HELP MODE: Function Explorer ===")
        print("Available functions:\n")
        for index, (name, _) in enumerate(functions, start=1):
            print(f"  {index:2d}) {name}")

        print("\nChoose:")
        print("  - Type a number to view that function's docstring")
        print("  - Type 'c' to return to calculator menu")
        print("  - Type 'q' to quit program")

        choice = input("\nHelp> ").strip().lower()

        if choice == "c":
            verbose_print("Leaving Help Mode. Returning to calculator menu.")
            return
        if choice == "q":
            verbose_print("Quitting program from Help Mode.")
            raise SystemExit

        if not choice.isdigit():
            verbose_print("Not a number. Try again.")
            continue

        selected_index = int(choice)
        if not (1 <= selected_index <= len(functions)):
            verbose_print("Number out of range. Try again.")
            continue

        function_name, function_object = functions[selected_index - 1]
        doc = inspect.getdoc(function_object) or "(No docstring available.)"

        verbose_print(f"=== DOCSTRING: {function_name} ===")
        print(doc)

        while True:
            print("\nChoose next:")
            print("  b = back to function list")
            print("  c = return to calculator menu")
            print("  q = quit program")

            sub_choice = input("Doc> ").strip().lower()
            if sub_choice == "b":
                break
            if sub_choice == "c":
                return
            if sub_choice == "q":
                raise SystemExit
            verbose_print("Please type b, c, or q.")


def run_one_verbose_cycle() -> None:
    """
    Run one full cycle of 3 divisions + floor reporting and then summarize.

    This is the "calculator" part of the program.
    """
    verbose_print("Starting a new verbose division cycle...")

    numerator = get_top_number()
    divisor = get_bottom_number()

    verbose_print(f"Verification: numerator = {numerator}")
    verbose_print(f"Verification: divisor   = {divisor}")

    first_exact = first_division_step(numerator, divisor)
    first_floored = first_rounding_step(first_exact)

    second_exact = second_division_step(first_floored, divisor)
    second_floored = second_rounding_step(second_exact)

    third_exact = third_division_step(second_floored, divisor)
    third_floored = third_rounding_step(third_exact)

    verbose_print("=== SUMMARY ===")
    verbose_print(f"Final floored results (space-separated): {first_floored} {second_floored} {third_floored}")


def main() -> None:
    """
    Main menu loop.

    Keys:
    - r: run the divider
    - h: help mode (function explorer)
    - q: quit
    """
    verbose_print("Welcome to the ultra-verbose divider + function explorer.")

    while True:
        print("\nMain Menu:")
        print("  r = run divider")
        print("  h = help (function explorer)")
        print("  q = quit")

        choice = input("\nSelect> ").strip().lower()

        if choice == "q":
            verbose_print("All done. Goodbye!")
            return
        if choice == "h":
            show_help_mode()
            continue
        if choice == "r":
            run_one_verbose_cycle()
            if not ask_run_again():
                verbose_print("Returning to main menu.")
            continue

        verbose_print("Unknown choice. Please type r, h, or q.")


if __name__ == "__main__":
    main()
