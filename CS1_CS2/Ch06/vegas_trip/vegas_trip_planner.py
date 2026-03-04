def print_greeting() -> None:
    """Print a welcome message for the Vegas trip planner program."""
    print("Welcome to the Vegas Trip Planner! This program helps you plan your Vegas getaway.")


def ask_number_of_travelers() -> int:
    """Prompt for and return the number of people traveling."""
    return int(input("How many people are traveling? "))


def ask_trip_length_days() -> int:
    """Prompt for and return the number of days the trip will last."""
    return int(input("How many days will the trip last? "))


def ask_hotel_price() -> float:
    """Prompt for and return the hotel price per night."""
    return float(input("What is the hotel price per night? "))


def ask_number_of_rooms() -> int:
    """Prompt for and return the number of hotel rooms needed."""
    return int(input("How many hotel rooms are needed? "))


def ask_food_cost_per_day() -> float:
    """Prompt for and return expected food cost per person per day."""
    return float(input("How much does each traveler expect to spend on food per day? "))


def ask_entertainment_budget() -> float:
    """Prompt for and return the total gambling and entertainment budget."""
    return float(input("What is your total gambling and entertainment budget? "))


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


def calculate_gallons_needed(distance: float, mpg: float) -> float:
    """Calculate the total gallons of fuel needed for the trip."""
    return distance / mpg


def calculate_fuel_cost(gallons: float, fuel_price: float) -> float:
    """Calculate total fuel cost for the trip."""
    return gallons * fuel_price


def calculate_flight_cost(ticket_price: float, travelers: int) -> float:
    """Calculate total airfare cost for all travelers."""
    return ticket_price * travelers


def calculate_transportation_cost(method: str, fuel_cost: float, flight_cost: float) -> float:
    """Select and return transportation cost based on the chosen travel method."""
    if method == "drive":
        return fuel_cost
    if method == "fly":
        return flight_cost
    raise ValueError("method must be 'drive' or 'fly'")


def calculate_lodging_cost(price_per_night: float, rooms: int, nights: int) -> float:
    """Calculate total hotel lodging cost."""
    return price_per_night * rooms * nights


def calculate_food_cost(food_per_day: float, travelers: int, days: int) -> float:
    """Calculate total food spending for all travelers over the trip."""
    return food_per_day * travelers * days


def main() -> None:
    """Run the Vegas trip planner program."""
    pass


if __name__ == "__main__":
    main()
