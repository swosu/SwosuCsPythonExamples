from trip_greeting import print_greeting
from transportation_inputs import (
    ask_driving_distance,
    ask_fuel_price,
    ask_plane_ticket_price,
    ask_travel_method,
    ask_vehicle_mpg,
)
from budget_inputs import (
    ask_emergency_fund,
    ask_entertainment_budget,
    ask_expected_gambling_loss,
    ask_local_transport_budget,
    ask_parking_ticket_budget,
    ask_souvenir_budget,
    ask_vehicle_maintenance_budget,
)
from trip_inputs import (
    ask_food_cost_per_day,
    ask_hotel_price,
    ask_number_of_rooms,
    ask_number_of_travelers,
    ask_trip_length_days,
)


# Input Functions
def ask_parking_cost_per_day() -> float:
    """Prompt for and return parking cost per day."""
    return float(input("How much does hotel or casino parking cost per day? "))


# Cost Calculations
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


# Output Functions
def print_trip_summary(
    total_cost: float,
    cost_per_person: float,
    parking_cost: float,
    souvenir_spending: float,
    emergency_reserve: float,
    gambling_losses: float,
    miscellaneous_expenses: float,
) -> None:
    """Print a summary of key trip costs and per-traveler totals."""
    print(f"Parking costs: ${parking_cost:.2f}")
    print(f"Souvenir spending: ${souvenir_spending:.2f}")
    print(f"Emergency reserves: ${emergency_reserve:.2f}")
    print(f"Gambling losses: ${gambling_losses:.2f}")
    print(f"Miscellaneous expenses: ${miscellaneous_expenses:.2f}")
    print(f"Total trip cost: ${total_cost:.2f}")
    print(f"Cost per traveler: ${cost_per_person:.2f}")


# Program Orchestration
def plan_vegas_trip() -> None:
    """Orchestrate prompts, calculations, and output for the Vegas trip planner."""
    travelers = ask_number_of_travelers()
    days = ask_trip_length_days()
    hotel_price = ask_hotel_price()
    rooms = ask_number_of_rooms()
    food_per_day = ask_food_cost_per_day()

    parking_per_day = ask_parking_cost_per_day()
    souvenir_budget = ask_souvenir_budget()
    emergency_fund = ask_emergency_fund()
    gambling_loss = ask_expected_gambling_loss()

    parking_ticket_budget = ask_parking_ticket_budget()
    vehicle_maintenance_budget = ask_vehicle_maintenance_budget()

    local_transport_budget = ask_local_transport_budget()
    entertainment_budget = ask_entertainment_budget()
    travel_method = ask_travel_method()

    fuel_cost = 0.0
    flight_cost = 0.0

    if travel_method == "drive":
        driving_distance = ask_driving_distance()
        vehicle_mpg = ask_vehicle_mpg()
        fuel_price = ask_fuel_price()
        gallons_needed = calculate_gallons_needed(driving_distance, vehicle_mpg)
        fuel_cost = calculate_fuel_cost(gallons_needed, fuel_price)
    else:
        plane_ticket_price = ask_plane_ticket_price()
        flight_cost = calculate_flight_cost(plane_ticket_price, travelers)

    transportation_cost = calculate_transportation_cost(travel_method, fuel_cost, flight_cost)
    lodging_cost = calculate_lodging_cost(hotel_price, rooms, days)
    food_cost = calculate_food_cost(food_per_day, travelers, days)
    parking_cost = calculate_parking_cost(parking_per_day, days)
    miscellaneous_travel_costs = calculate_miscellaneous_costs(
        parking_ticket_budget,
        vehicle_maintenance_budget,
    )
    total_cost = calculate_total_trip_cost(
        transportation_cost,
        lodging_cost,
        food_cost,
        parking_cost,
        local_transport_budget,
        entertainment_budget,
        souvenir_budget,
        emergency_fund,
        gambling_loss,
        miscellaneous_travel_costs,
    )
    cost_per_person = calculate_cost_per_person(total_cost, travelers)

    print_trip_summary(
        total_cost,
        cost_per_person,
        parking_cost,
        souvenir_budget,
        emergency_fund,
        gambling_loss,
        miscellaneous_travel_costs,
    )


def main() -> None:
    """Run the Vegas trip planner program."""
    print_greeting()
    plan_vegas_trip()


if __name__ == "__main__":
    main()