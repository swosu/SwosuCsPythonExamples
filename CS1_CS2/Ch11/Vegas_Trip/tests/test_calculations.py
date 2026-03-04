"""Unit tests for trip cost calculations."""

from trip_calculations import (
    calculate_cost_per_person,
    calculate_food_cost,
    calculate_fuel_cost,
    calculate_lodging_cost,
    calculate_parking_cost,
    calculate_total_trip_cost,
)


def test_calculate_fuel_cost() -> None:
    """Fuel cost should be gallons multiplied by fuel price."""
    assert calculate_fuel_cost(40.0, 3.75) == 150.0


def test_calculate_lodging_cost() -> None:
    """Lodging cost should be nightly rate times rooms times nights."""
    assert calculate_lodging_cost(129.99, 2, 3) == 779.94


def test_calculate_food_cost() -> None:
    """Food cost should be per-day amount times travelers times days."""
    assert calculate_food_cost(55.0, 4, 5) == 1100.0


def test_calculate_parking_cost() -> None:
    """Parking cost should be per-day parking times days."""
    assert calculate_parking_cost(22.5, 4) == 90.0


def test_calculate_total_trip_cost() -> None:
    """Total trip cost should add all trip budget categories."""
    total = calculate_total_trip_cost(
        transport=300.0,
        lodging=800.0,
        food=500.0,
        parking=80.0,
        local_transport=120.0,
        entertainment=250.0,
        souvenirs=90.0,
        emergency_fund=200.0,
        gambling_losses=150.0,
        miscellaneous_travel_costs=60.0,
    )
    assert total == 2550.0


def test_calculate_cost_per_person() -> None:
    """Cost per person should be total trip cost divided by traveler count."""
    assert calculate_cost_per_person(2550.0, 5) == 510.0