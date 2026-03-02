# ------------------------------
# CALCULATION FUNCTIONS
# ------------------------------

def calculate_car_fuel_cost(distance, mpg, fuel_price):
    gallons_needed = distance / mpg
    return gallons_needed * fuel_price


def calculate_plane_cost(ticket_price, baggage_cost, people):
    return (ticket_price + baggage_cost) * people


def calculate_lodging_cost(price_per_night, rooms, days):
    return price_per_night * rooms * days


def calculate_food_cost(food_budget, people, days):
    return food_budget * people * days


def calculate_travel_cost(travel_method, travel_details, people):
    if travel_method == "car":
        distance, mpg, fuel_price = travel_details
        return calculate_car_fuel_cost(distance, mpg, fuel_price)
    else:
        ticket_price, baggage_cost = travel_details
        return calculate_plane_cost(ticket_price, baggage_cost, people)


def calculate_trip_costs(trip_data):
    travel_cost = calculate_travel_cost(
        trip_data["travel_method"],
        trip_data["travel_details"],
        trip_data["people"]
    )

    lodging_cost = calculate_lodging_cost(
        trip_data["lodging"][0],
        trip_data["lodging"][1],
        trip_data["days"]
    )

    food_cost = calculate_food_cost(
        trip_data["food_budget"],
        trip_data["people"],
        trip_data["days"]
    )

    bail_cost = trip_data["bail"]

    total_cost = travel_cost + lodging_cost + food_cost + bail_cost

    return {
        "travel_cost": travel_cost,
        "lodging_cost": lodging_cost,
        "food_cost": food_cost,
        "bail_cost": bail_cost,
        "total_cost": total_cost
    }