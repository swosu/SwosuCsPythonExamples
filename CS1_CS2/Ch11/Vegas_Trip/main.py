"""Main orchestration module for the Vegas trip planner."""

from budget_inputs import (
    ask_emergency_fund,
    ask_entertainment_budget,
    ask_expected_gambling_loss,
    ask_local_transport_budget,
    ask_parking_cost_per_day,
    ask_parking_ticket_budget,
    ask_souvenir_budget,
    ask_vehicle_maintenance_budget,
)
from transportation_inputs import (
    ask_driving_distance,
    ask_fuel_price,
    ask_plane_ticket_price,
    ask_travel_method,
    ask_vehicle_mpg,
)
from trip_calculations import (
    calculate_cost_per_person,
    calculate_flight_cost,
    calculate_food_cost,
    calculate_fuel_cost,
    calculate_gallons_needed,
    calculate_lodging_cost,
    calculate_miscellaneous_costs,
    calculate_parking_cost,
    calculate_total_trip_cost,
    calculate_transportation_cost,
)
from trip_greeting import print_greeting
from trip_inputs import (
    ask_food_cost_per_day,
    ask_hotel_price,
    ask_number_of_rooms,
    ask_number_of_travelers,
    ask_trip_length_days,
)
from trip_summary import print_trip_summary


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
