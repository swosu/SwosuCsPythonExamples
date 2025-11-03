class Car:
    def __init__(self):
        # Fundamental OOP concept: attributes (aka instance variables)
        # These store the "state" of our Car object
        self.model_year = 0
        self.purchase_price = 0   # 👈 NEW attribute we need for this problem
        self.current_value = 0    # Calculated later, so initialize to 0

    def calc_current_value(self, current_year):
        """
        Calculates the car's current value using depreciation.
        Formula: current_value = purchase_price * (1 - depreciation_rate) ** car_age
        """
        depreciation_rate = 0.15   # 15% depreciation per year
        car_age = current_year - self.model_year
        print(f"our original year is {self.model_year}, and our current year is {current_year}, so our car age is {car_age}")
        print(f" our total years of depreciation is {car_age}")
        # OOP lesson: methods operate on object data (self)
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age , 2)

    def print_info(self):
        """
        Prints information about the car.
        This is a *behavior* of the Car class (methods = behaviors).
        """
        print("Car's information:")
        print(f"  Model year: {self.model_year}")
        print(f"  Purchase price: ${self.purchase_price}")
        print(f"  Current value: ${self.current_value}")


if __name__ == "__main__":
    # Input: year, purchase price, current year
    year = 2011
    price = 18000
    current_year = 2018

    # OOP concept: create an instance (object) of Car
    my_car = Car()

    # Assign object attributes
    my_car.model_year = year
    my_car.purchase_price = price

    # Call methods on the object
    my_car.calc_current_value(current_year)
    my_car.print_info()
