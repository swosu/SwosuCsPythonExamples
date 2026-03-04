"""Budget-related input functions for the Vegas trip planner."""


def ask_parking_cost_per_day() -> float:
    """Prompt for and return parking cost per day."""
    return float(input("How much does hotel or casino parking cost per day? "))


def ask_parking_ticket_budget() -> float:
    """Prompt for and return money reserved for parking tickets or fines."""
    return float(input("How much money do you want to reserve for parking tickets or fines? "))


def ask_vehicle_maintenance_budget() -> float:
    """Prompt for and return money reserved for vehicle maintenance or repairs."""
    return float(input("How much money do you want to reserve for vehicle maintenance or repairs during the trip? "))


def ask_local_transport_budget() -> float:
    """Prompt for and return local transportation budget in Las Vegas."""
    return float(input("How much do you expect to spend on taxis, Uber, or monorail rides in Las Vegas? "))


def ask_expected_gambling_loss() -> float:
    """Prompt for and return expected gambling losses."""
    return float(input("How much money do you expect to lose gambling? "))


def ask_entertainment_budget() -> float:
    """Prompt for and return the total gambling and entertainment budget."""
    return float(input("What is your total gambling and entertainment budget? "))


def ask_souvenir_budget() -> float:
    """Prompt for and return the total souvenir budget."""
    return float(input("How much do you expect to spend on souvenirs? "))


def ask_emergency_fund() -> float:
    """Prompt for and return the amount reserved for unexpected expenses."""
    return float(input("How much money do you want to reserve for unexpected expenses? "))