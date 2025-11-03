from abc import ABC, abstractmethod

class Engine:
    """
    A simple Engine class to demonstrate COMPOSITION.
    An Engine belongs to a Car but is its own object.
    """
    def __init__(self, horsepower: int, fuel_type: str):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def __str__(self):
        return f"{self.horsepower} HP {self.fuel_type} engine"

    def __repr__(self):
        return f"Engine({self.horsepower}, '{self.fuel_type}')"


class Vehicle(ABC):
    """
    Abstract base class for all vehicles.
    Forces subclasses to implement calc_current_value().
    """
    @abstractmethod
    def calc_current_value(self, current_year: int):
        pass


class Car(Vehicle):
    """
    Base class representing a generic car.
    Demonstrates ENCAPSULATION, ABSTRACTION, and COMPOSITION.
    """
    depreciation_rate = 0.15  # class-level attribute (shared default)

    def __init__(self, model_year: int, purchase_price: int, engine: Engine):
        if purchase_price < 0:
            raise ValueError("Purchase price cannot be negative")

        self.model_year = model_year
        self.purchase_price = purchase_price
        self.current_value = purchase_price  # will depreciate later
        self.engine = engine  # composition: a Car *has an* Engine

    # --- Properties ---
    @property
    def age(self):
        """Calculate car's age from current year 2025."""
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
        """Alternate constructor: '2011,55000' -> Car instance"""
        year, price = data.split(",")
        return cls(int(year), int(price), engine)

    # --- Business logic ---
    def calc_current_value(self, current_year: int):
        """Calculate depreciation. Generic cars lose 15% per year."""
        if current_year < self.model_year:
            raise ValueError("Current year cannot be before model year")
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - Car.depreciation_rate) ** car_age)

    def print_info(self):
        """Print information about the car."""
        print("Car's information:")
        print(f"  Model year: {self.model_year}")
        print(f"  Purchase price: ${self.purchase_price}")
        print(f"  Current value: ${self.current_value}")
        print(f"  Engine: {self.engine}")


class TruckCar(Car):
    """
    A specialized type of Car (INHERITANCE).
    Ranchero & El Camino are trucks + cars (aka Utes).
    """
    def __init__(self, model_year: int, purchase_price: int, engine: Engine, bed_size: str):
        super().__init__(model_year, purchase_price, engine)
        self.bed_size = bed_size  # extra attribute just for trucks

    def calc_current_value(self, current_year: int):
        """Override depreciation for trucks (hold value better)."""
        if current_year < self.model_year:
            raise ValueError("Current year cannot be before model year")
        depreciation_rate = 0.10
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)

    def print_info(self):
        super().print_info()
        print(f"  Bed size: {self.bed_size}")


class SportsCar(Car):
    """
    Corvette time! Sports cars might depreciate fast at first, then
    level off because they become collectible (POLYMORPHISM).
    """
    def calc_current_value(self, current_year: int):
        if current_year < self.model_year:
            raise ValueError("Current year cannot be before model year")
        car_age = current_year - self.model_year
        if car_age < 10:
            depreciation_rate = 0.20  # ouch, steep early drop
        else:
            depreciation_rate = 0.05  # collectible status slows depreciation
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)


class Fleet:
    """
    Manages a collection of vehicles (demonstrates polymorphism).
    """
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


# ------------------- DEMO -------------------

if __name__ == "__main__":
    current_year = 2025

    # Create engines
    ranchero_engine = Engine(250, "V8")
    el_camino_engine = Engine(200, "V8")
    corvette_engine = Engine(495, "V8")

    # Create vehicles
    ranchero = TruckCar(1972, 3200, ranchero_engine, bed_size="Long bed")
    el_camino = TruckCar(1985, 4500, el_camino_engine, bed_size="Short bed")
    corvette = SportsCar(2011, 55000, corvette_engine)

    # Create a fleet and add vehicles
    fleet = Fleet()
    fleet.add_vehicle(ranchero)
    fleet.add_vehicle(el_camino)
    fleet.add_vehicle(corvette)

    # Calculate and print values
    fleet.calc_all_values(current_year)
    fleet.print_all_info()

    # Demo utility
    print("50 miles is", Car.miles_to_km(50), "km")

    # Demo alternate constructor
    mustang_engine = Engine(300, "V8")
    mustang = Car.from_string("2015,25000", mustang_engine)
    mustang.calc_current_value(current_year)
    print("\n--- Mustang ---")
    mustang.print_info()
