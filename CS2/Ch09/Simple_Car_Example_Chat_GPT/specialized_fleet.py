import requests
from vehicles import Car, TruckCar, SportsCar, Engine, Fleet


class InternationalCar(Car):
    """
    Extends Car with country-of-origin data.
    """
    def __init__(self, model_year: int, purchase_price: int, engine: Engine, country: str):
        super().__init__(model_year, purchase_price, engine)
        self.country = country

    def print_info(self):
        super().print_info()
        print(f"  Country of origin: {self.country}")

    def get_country_info(self):
        """Fetch details about the country from REST Countries API."""
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

    def get_weather(self):
        """Fetch current weather for the car's country of origin."""
        url = f"https://wttr.in/{self.country}?format=3"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.text  # e.g. "Germany: 🌦️ +18°C"
        except Exception as e:
            return f"Weather unavailable: {e}"


class SmartFleet(Fleet):
    """
    Fleet that can pick the best vehicle for a trip based on weather.
    """
    def best_vehicle_for_trip(self):
        best_choice = None
        for v in self.vehicles:
            if hasattr(v, "get_weather"):
                weather = v.get_weather()
                print(f"Checking {v.model_year} {v.engine}: {weather}")

                # Rule system
                if "rain" in weather.lower() or "🌧" in weather:
                    if isinstance(v, TruckCar):
                        best_choice = v
                elif "snow" in weather.lower() or "❄" in weather:
                    if isinstance(v, TruckCar):
                        best_choice = v
                elif "sun" in weather.lower() or "☀" in weather:
                    if isinstance(v, SportsCar):
                        best_choice = v
                else:
                    # fallback: newest car
                    if not best_choice or v.model_year > best_choice.model_year:
                        best_choice = v
        return best_choice


# ------------------- DEMO -------------------

if __name__ == "__main__":
    current_year = 2025

    # Engines
    bmw_engine = Engine(300, "Turbo I6")
    toyota_engine = Engine(150, "I4 Hybrid")

    # Cars with countries
    bmw = InternationalCar(2015, 55000, bmw_engine, "Germany")
    prius = InternationalCar(2020, 25000, toyota_engine, "Japan")

    # Smart fleet
    fleet = SmartFleet()
    fleet.add_vehicle(bmw)
    fleet.add_vehicle(prius)

    # Update values and show info
    fleet.calc_all_values(current_year)
    fleet.print_all_info()

    # Pull in API info for countries
    print("\n--- Country Info ---")
    bmw.get_country_info()
    prius.get_country_info()

    # Decide best car for the trip
    print("\n--- Best Vehicle for Trip ---")
    chosen = fleet.best_vehicle_for_trip()
    if chosen:
        chosen.print_info()
    else:
        print("No suitable vehicle found.")
