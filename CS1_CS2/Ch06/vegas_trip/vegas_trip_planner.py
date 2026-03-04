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


def ask_parking_cost_per_day() -> float:
    """Prompt for and return parking cost per day."""
    return float(input("How much does hotel or casino parking cost per day? "))


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


def calculate_parking_cost(parking_per_day: float, days: int) -> float:
    """Calculate total parking cost over the trip."""
    return parking_per_day * days


def calculate_total_trip_cost(
    transport: float,
    lodging: float,
    food: float,
    parking: float,
    local_transport: float,
    entertainment: float,
    souvenirs: float,
    emergency_fund: float,
) -> float:
    """Calculate and return the total trip cost."""
    return transport + lodging + food + parking + local_transport + entertainment + souvenirs + emergency_fund


def calculate_cost_per_person(total_cost: float, travelers: int) -> float:
    """Calculate and return the cost per traveler."""
    return total_cost / travelers


def print_trip_summary(total_cost: float, cost_per_person: float) -> None:
    """Print a summary of total trip cost and cost per traveler."""
    print(f"Total trip cost: ${total_cost:.2f}")
    print(f"Cost per traveler: ${cost_per_person:.2f}")


def plan_vegas_trip() -> None:
    """Orchestrate prompts, calculations, and output for the Vegas trip planner."""
    travelers = ask_number_of_travelers()
    days = ask_trip_length_days()
    hotel_price = ask_hotel_price()
    rooms = ask_number_of_rooms()
    food_per_day = ask_food_cost_per_day()
    parking_per_day = ask_parking_cost_per_day()
    local_transport_budget = ask_local_transport_budget()
    entertainment_budget = ask_entertainment_budget()
    souvenir_budget = ask_souvenir_budget()
    emergency_fund = ask_emergency_fund()
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
    total_cost = calculate_total_trip_cost(
        transportation_cost,
        lodging_cost,
        food_cost,
        parking_cost,
        local_transport_budget,
        entertainment_budget,
        souvenir_budget,
        emergency_fund,
    )
    cost_per_person = calculate_cost_per_person(total_cost, travelers)

    print_trip_summary(total_cost, cost_per_person)


def main() -> None:
    """Run the Vegas trip planner program."""
    print_greeting()
    plan_vegas_trip()


if __name__ == "__main__":
    main()
