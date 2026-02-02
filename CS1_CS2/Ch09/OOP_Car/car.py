class Car:

    def __init__(self):
        self.model_year = 0
        # TODO: Declare purchase_price attribute

        self.current_value = 0

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        # Car depreciation formula
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price *
                                   (1 - depreciation_rate)**car_age)

    
    def print_info(self):
        print(f"Model Year: {self.model_year}")
        print(f"Purchase Price: ${self.purchase_price}")
        print(f"Current Value: ${self.current_value}")

if __name__ == "__main__":
    year = int(input("What year was the car made? "))
    price = int(input("What was the purchase price? "))
    current_year = int(input("What is the current year? "))

    my_car = Car()
    my_car.model_year = year
    my_car.purchase_price = price
    my_car.calc_current_value(current_year)
    my_car.print_info()
