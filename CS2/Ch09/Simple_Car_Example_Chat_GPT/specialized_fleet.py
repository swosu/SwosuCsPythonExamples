# specialized_fleet.py
import requests
from vehicles import Car, TruckCar, SportsCar, Engine, Fleet

class InternationalCar(Car):
    """
    Extends Car with country-of-origin data.
    Demonstrates EXTENDING imported classes.
    """
    def __init__(self, model_year: int, purchase_price: int, engine: Engine, country: str):
        super().__init__(model_year, purchase_price, engine)
        self.country = country

    def print_info(self):
        super().print_info()
        print(f"  Country of origin: {self.country}")

    def get_country_info(self):
        """
        Example of using an API to fetch extra details about the country.
        We'll use the REST Countries API (https://restcountries.com).
        """
        url = f"https://restcountries.com/v3.1/name/{self.country}"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()[0]
            capital = data["capital"][0]
            region = data["region"]
            population = data["population"]
            print(f"  {self.country} details:")
            print(f"    Capital: {capital}")
            print(f"    Region: {region}")
            print(f"    Population: {population:,}")
        except Exception as e:
            print(f"  Could not fetch country info: {e}")


# ------------------- DEMO -------------------

if __name__ == "__main__":
    current_year = 2025

    # Engines
    bmw_engine = Engine(300, "Turbo I6")
    toyota_engine = Engine(150, "I4 Hybrid")

    # Cars with countries
    bmw = InternationalCar(2015, 55000, bmw_engine, "Germany")
    prius = InternationalCar(2020, 25000, toyota_engine, "Japan")

    # Fleet
    fleet = Fleet()
    fleet.add_vehicle(bmw)
    fleet.add_vehicle(prius)

    # Update values and show info
    fleet.calc_all_values(current_year)
    fleet.print_all_info()

    # Pull in API info for countries
    print("\n--- Country Info ---")
    bmw.get_country_info()
    prius.get_country_info()
