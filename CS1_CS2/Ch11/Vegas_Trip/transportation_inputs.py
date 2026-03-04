"""Transportation-specific input functions for the Vegas trip planner."""


def ask_travel_method() -> str:
    """Prompt for and return whether the travelers will drive or fly."""
    while True:
        method = input("Do you want to drive or fly? ").strip().lower()
        if method in ("drive", "fly"):
            return method
        print("Please enter 'drive' or 'fly'.")


def ask_plane_ticket_price() -> float:
    """Prompt for and return the cost of one plane ticket."""
    return float(input("What is the cost of one plane ticket? "))


def ask_driving_distance() -> float:
    """Prompt for and return the driving distance in miles."""
    return float(input("How many miles is the trip if traveling by car? "))


def ask_vehicle_mpg() -> float:
    """Prompt for and return the vehicle fuel efficiency in miles per gallon."""
    return float(input("What is your vehicle's fuel efficiency (mpg)? "))


def ask_fuel_price() -> float:
    """Prompt for and return the price of fuel per gallon."""
    return float(input("What is the price of fuel per gallon? "))