class Engine:
    """
    A simple Engine class to demonstrate COMPOSITION.
    An Engine belongs to a Car but is its own object.
    """
    def __init__(self, horsepower: int, fuel_type: str):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def __str__(self):
        # This string representation makes debugging & printing nice
        return f"{self.horsepower} HP {self.fuel_type} engine"


class Car:
    """
    Base class representing a generic car.
    Demonstrates ENCAPSULATION & ABSTRACTION.
    """
    def __init__(self, model_year: int, purchase_price: int, engine: Engine):
        self.model_year = model_year
        self.purchase_price = purchase_price
        self.current_value = purchase_price  # will depreciate later
        self.engine = engine  # composition: a Car *has an* Engine

    def calc_current_value(self, current_year: int):
        """Calculate depreciation. Generic cars lose 15% per year."""
        depreciation_rate = 0.15
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)

    def print_info(self):
        """Print information about the car."""
        print("Car's information:")
        print(f"  Model year: {self.model_year}")
        print(f"  Purchase price: ${self.purchase_price}")
        print(f"  Current value: ${self.current_value}")
        print(f"  Engine: {self.engine}")  # Delegates to Engine's __str__


class TruckCar(Car):
    """
    A specialized type of Car (INHERITANCE).
    Ranchero & El Camino are trucks + cars (aka Utes).
    """
    def __init__(self, model_year: int, purchase_price: int, engine: Engine, bed_size: str):
        super().__init__(model_year, purchase_price, engine)
        self.bed_size = bed_size  # extra attribute just for trucks

    def calc_current_value(self, current_year: int):
        """
        Trucks tend to hold their value a little better.
        Override depreciation to 10% instead of 15% (POLYMORPHISM).
        """
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
        car_age = current_year - self.model_year
        if car_age < 10:
            depreciation_rate = 0.20  # ouch, steep early drop
        else:
            depreciation_rate = 0.05  # collectible status slows depreciation
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)


# ------------------- DEMO -------------------

if __name__ == "__main__":
    # Hardcoded year for testing
    current_year = 2025

    # Create engines
    ranchero_engine = Engine(250, "V8")
    el_camino_engine = Engine(200, "V8")
    corvette_engine = Engine(495, "V8")

    # Create vehicles
    ranchero = TruckCar(1972, 3200, ranchero_engine, bed_size="Long bed")
    el_camino = TruckCar(1985, 4500, el_camino_engine, bed_size="Short bed")
    corvette = SportsCar(2011, 55000, corvette_engine)

    # Calculate values
    ranchero.calc_current_value(current_year)
    el_camino.calc_current_value(current_year)
    corvette.calc_current_value(current_year)

    # Print results
    print("\n--- Ranchero ---")
    ranchero.print_info()
    print("\n--- El Camino ---")
    el_camino.print_info()
    print("\n--- Corvette ---")
    corvette.print_info()
