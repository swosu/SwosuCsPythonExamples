"""Trip cost calculation functions for the Vegas trip planner."""


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


def calculate_parking_cost(parking_per_day: float, days: int) -> float:
    """Calculate total parking cost over the trip."""
    return parking_per_day * days


def calculate_miscellaneous_costs(
    parking_tickets: float,
    vehicle_maintenance: float,
) -> float:
    """Calculate combined miscellaneous travel costs."""
    return parking_tickets + vehicle_maintenance


def calculate_total_trip_cost(
    transport: float,
    lodging: float,
    food: float,
    parking: float,
    local_transport: float,
    entertainment: float,
    souvenirs: float,
    emergency_fund: float,
    gambling_losses: float,
    miscellaneous_travel_costs: float,
) -> float:
    """Calculate and return the total trip cost."""
    return (
        transport
        + lodging
        + food
        + parking
        + local_transport
        + entertainment
        + souvenirs
        + emergency_fund
        + gambling_losses
        + miscellaneous_travel_costs
    )


def calculate_cost_per_person(total_cost: float, travelers: int) -> float:
    """Calculate and return the cost per traveler."""
    return total_cost / travelers