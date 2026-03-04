"""Unit tests for miscellaneous travel cost calculations."""

from trip_calculations import calculate_miscellaneous_costs


def test_calculate_miscellaneous_costs_adds_parking_tickets_and_maintenance() -> None:
    """Miscellaneous costs should be the sum of parking tickets and maintenance."""
    total = calculate_miscellaneous_costs(parking_tickets=75.0, vehicle_maintenance=120.0)
    assert total == 195.0


def test_calculate_miscellaneous_costs_allows_zero_values() -> None:
    """Zero inputs should produce a zero miscellaneous total."""
    assert calculate_miscellaneous_costs(parking_tickets=0.0, vehicle_maintenance=0.0) == 0.0


def test_calculate_miscellaneous_costs_handles_decimal_inputs() -> None:
    """Decimal budget values should be summed accurately."""
    total = calculate_miscellaneous_costs(parking_tickets=49.99, vehicle_maintenance=30.01)
    assert total == 80.0