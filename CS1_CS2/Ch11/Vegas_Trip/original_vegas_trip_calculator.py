# ==========================================
# LAS VEGAS TRIP COST PLANNER
# ==========================================


# ------------------------------
# USER INPUT FUNCTIONS
# ------------------------------

def ask_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def ask_float(prompt):
    return float(input(prompt))


def ask_yes_no(prompt):
    response = input(prompt).strip().lower()
    return response == "y"


def collect_basic_trip_info():
    number_of_people = ask_integer("How many people are traveling? ")
    number_of_days = ask_integer("How many days will you stay? ")
    return number_of_people, number_of_days


def choose_travel_method():
    print("\nChoose travel method:")
    print("1 - Car")
    print("2 - Plane")

    choice = ask_integer("Enter 1 or 2: ")

    if choice == 1:
        return "car"
    else:
        return "plane"


def collect_car_details():
    distance = ask_float("How many miles to Vegas? ")
    mpg = ask_float("How many miles per gallon does your car get? ")
    fuel_price = ask_float("Price per gallon of gas? ")

    return distance, mpg, fuel_price


def collect_plane_details():
    ticket_price = ask_float("Price per plane ticket? ")
    baggage_cost = ask_float("Baggage cost per person? ")

    return ticket_price, baggage_cost


def collect_lodging_details():
    hotel_price_per_night = ask_float("Hotel price per room per night? ")
    rooms_needed = ask_integer("How many rooms do you need? ")

    return hotel_price_per_night, rooms_needed


def collect_food_details():
    food_budget_per_person_per_day = ask_float("Food budget per person per day? ")
    return food_budget_per_person_per_day


def collect_entourage_cost():
    bail_cost = ask_float("Potential bail fund (enter 0 if not needed)? ")
    return bail_cost


def collect_trip_details():
    people, days = collect_basic_trip_info()
    travel_method = choose_travel_method()
    lodging = collect_lodging_details()
    food_budget = collect_food_details()
    bail = collect_entourage_cost()

    if travel_method == "car":
        travel_details = collect_car_details()
    else:
        travel_details = collect_plane_details()

    return {
        "people": people,
        "days": days,
        "travel_method": travel_method,
        "travel_details": travel_details,
        "lodging": lodging,
        "food_budget": food_budget,
        "bail": bail
    }


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


# ------------------------------
# SUMMARY FUNCTIONS
# ------------------------------

def summarize_trip(trip_data, cost_data):
    return {
        "people": trip_data["people"],
        "days": trip_data["days"],
        "travel_method": trip_data["travel_method"],
        "cost_breakdown": cost_data
    }


# ------------------------------
# PRINTING FUNCTIONS
# ------------------------------

def print_line():
    print("=" * 40)


def print_cost(label, amount):
    print(f"{label:<20} ${amount:,.2f}")


def print_results(summary):
    print_line()
    print("LAS VEGAS TRIP SUMMARY")
    print_line()

    print(f"Travelers: {summary['people']}")
    print(f"Days: {summary['days']}")
    print(f"Travel Method: {summary['travel_method'].capitalize()}")
    print_line()

    costs = summary["cost_breakdown"]

    print_cost("Travel Cost:", costs["travel_cost"])
    print_cost("Lodging Cost:", costs["lodging_cost"])
    print_cost("Food Cost:", costs["food_cost"])
    print_cost("Bail Fund:", costs["bail_cost"])

    print_line()
    print_cost("TOTAL TRIP COST:", costs["total_cost"])
    print_line()


# ------------------------------
# MAIN ORCHESTRATION
# ------------------------------

def main():
    trip_data = collect_trip_details()
    cost_data = calculate_trip_costs(trip_data)
    summary = summarize_trip(trip_data, cost_data)
    print_results(summary)


if __name__ == "__main__":
    main()