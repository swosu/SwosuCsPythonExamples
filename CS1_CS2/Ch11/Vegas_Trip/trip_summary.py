"""Trip summary output functions for the Vegas trip planner."""


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