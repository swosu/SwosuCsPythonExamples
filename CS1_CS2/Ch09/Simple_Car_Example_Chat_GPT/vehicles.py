"""
vehicles.py
Core OOP demo with Engine, Car, TruckCar, SportsCar, and Fleet.
"""

from abc import ABC, abstractmethod


class Engine:
    """A simple Engine class to demonstrate COMPOSITION."""
    def __init__(self, horsepower: int, fuel_type: str):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def __str__(self):
        return f"{self.horsepower} HP {self.fuel_type} engine"

    def __repr__(self):
        return f"Engine({self.horsepower}, '{self.fuel_type}')"


class Vehicle(ABC):
    """Abstract base class for all vehicles."""
    @abstractmethod
    def calc_current_value(self, current_year: int):
        pass


class Car(Vehicle):
    """Base class representing a generic car."""
    depreciation_rate = 0.15  # shared across all cars unless overridden

    def __init__(self, model_year: int, purchase_price: int, engine: Engine):
        if purchase_price < 0:
            raise ValueError("Purchase price cannot be negative")
        self.model_year = model_year
        self.purchase_price = purchase_price
        self.current_value = purchase_price
        self.engine = engine

    # --- Properties ---
    @property
    def age(self):
        return 2025 - self.model_year

    # --- Magic Methods ---
    def __repr__(self):
        return f"Car({self.model_year}, ${self.purchase_price}, {repr(self.engine)})"

    def __eq__(self, other):
        return isinstance(other, Car) and self.model_year == other.model_year and self.purchase_price == other.purchase_price

    def __lt__(self, other):
        return self.purchase_price < other.purchase_price

    # --- Utility methods ---
    @staticmethod
    def miles_to_km(miles: float) -> float:
        return miles * 1.609

    @classmethod
    def from_string(cls, data: str, engine: Engine):
        year, price = data.split(",")
        return cls(int(year), int(price), engine)

    # --- Business logic ---
    def calc_current_value(self, current_year: int):
        if current_year < self.model_year:
            raise ValueError("Current year cannot be before model year")
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - Car.depreciation_rate) ** car_age)

    def print_info(self):
        print("Car's information:")
        print(f"  Model year: {self.model_year}")
        print(f"  Purchase price: ${self.purchase_price}")
        print(f"  Current value: ${self.current_value}")
        print(f"  Engine: {self.engine}")


class TruckCar(Car):
    """Specialized type of Car with a truck bed."""
    def __init__(self, model_year: int, purchase_price: int, engine: Engine, bed_size: str):
        super().__init__(model_year, purchase_price, engine)
        self.bed_size = bed_size

    def calc_current_value(self, current_year: int):
        depreciation_rate = 0.10  # trucks hold value better
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)

    def print_info(self):
        super().print_info()
        print(f"  Bed size: {self.bed_size}")


class SportsCar(Car):
    """Sports car that depreciates fast, then slows down."""
    def calc_current_value(self, current_year: int):
        car_age = current_year - self.model_year
        if car_age < 10:
            depreciation_rate = 0.20
        else:
            depreciation_rate = 0.05
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)


class Fleet:
    """Manages a collection of vehicles."""
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def calc_all_values(self, current_year: int):
        for v in self.vehicles:
            v.calc_current_value(current_year)

    def print_all_info(self):
        for v in self.vehicles:
            v.print_info()
            print("-" * 30)
