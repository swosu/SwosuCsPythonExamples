def print_greeting() -> None:
    """Print a welcome message for the Vegas trip planner program."""
    print("Welcome to the Vegas Trip Planner! This program helps you plan your Vegas getaway.")


def ask_number_of_travelers() -> int:
    """Prompt for and return the number of people traveling."""
    return int(input("How many people are traveling? "))


def ask_trip_length_days() -> int:
    """Prompt for and return the number of days the trip will last."""
    return int(input("How many days will the trip last? "))


def ask_travel_method() -> str:
    """Prompt for and return whether the travelers will drive or fly."""
    while True:
        method = input("Do you want to drive or fly? ").strip().lower()
        if method in ("drive", "fly"):
            return method
        print("Please enter 'drive' or 'fly'.")


def ask_driving_distance() -> float:
    """Prompt for and return the driving distance in miles."""
    return float(input("How many miles is the trip if traveling by car? "))


def ask_vehicle_mpg() -> float:
    """Prompt for and return the vehicle fuel efficiency in miles per gallon."""
    return float(input("What is your vehicle's fuel efficiency (mpg)? "))


def ask_fuel_price() -> float:
    """Prompt for and return the price of fuel per gallon."""
    return float(input("What is the price of fuel per gallon? "))


def calculate_gallons_needed(distance: float, mpg: float) -> float:
    """Calculate the total gallons of fuel needed for the trip."""
    return distance / mpg


def main() -> None:
    """Run the Vegas trip planner program."""
    pass


if __name__ == "__main__":
    main()
