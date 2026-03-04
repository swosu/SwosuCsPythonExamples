"""Unit tests for transportation cost selection logic."""

import pytest

from trip_calculations import calculate_transportation_cost


def test_calculate_transportation_cost_uses_fuel_cost_when_driving() -> None:
    """Driving should select fuel cost as the transportation total."""
    assert calculate_transportation_cost("drive", fuel_cost=180.5, flight_cost=999.0) == 180.5


def test_calculate_transportation_cost_uses_flight_cost_when_flying() -> None:
    """Flying should select flight cost as the transportation total."""
    assert calculate_transportation_cost("fly", fuel_cost=180.5, flight_cost=999.0) == 999.0


def test_calculate_transportation_cost_rejects_invalid_method() -> None:
    """Invalid travel method should raise ValueError."""
    with pytest.raises(ValueError):
        calculate_transportation_cost("train", fuel_cost=180.5, flight_cost=999.0)