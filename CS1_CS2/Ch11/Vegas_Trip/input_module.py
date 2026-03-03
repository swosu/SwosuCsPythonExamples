"""
All functions that talk to the user.


choose_travel_method

etc.

This file ONLY asks questions.
"""

def collect_entourage_cost():
    bail_cost = ask_float("Potential bail fund (enter 0 if not needed)? ")
    return bail_cost


def collect_food_details():
    food_budget_per_person_per_day = ask_float("Food budget per person per day? ")
    return food_budget_per_person_per_day

def collect_lodging_details():
    hotel_price_per_night = ask_float("Hotel price per room per night? ")
    rooms_needed = ask_integer("How many rooms do you need? ")

    return hotel_price_per_night, rooms_needed

def collect_basic_trip_info():
    number_of_people = ask_integer("How many people are traveling? ")
    number_of_days = ask_integer("How many days will you stay? ")
    return number_of_people, number_of_days

def ask_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def ask_float(prompt):
    return float(input(prompt))


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


def choose_travel_method():
    print("\nChoose travel method:")
    print("1 - Car")
    print("2 - Plane")

    choice = ask_integer("Enter 1 or 2: ")

    if choice == 1:
        return "car"
    else:
        return "plane"