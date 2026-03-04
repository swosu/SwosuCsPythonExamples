"""General trip input functions for the Vegas trip planner."""


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
