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