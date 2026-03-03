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
