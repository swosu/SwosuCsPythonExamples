class Car:
    def __init__(self):
        self.model_year = 0
        self.purchase_price = 0     
        self.current_value = 0

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        # Car depreciation formula
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)

    def print_info(self):
        print(f"The year of your car's model is {self.model_year}.")
        print(f"You bought your car for {self.purchase_price}.")
        print(f"If you sold your car now, you would get around ${self.current_value} for it.")

if __name__ == "__main__":    
    year = int(input("What year is your car model?\n")) 
    price = int(input("How much did your car cost when you bought it?\n"))
    current_year = int(input("What year is it now?\n"))
    
    my_car = Car()
    my_car.model_year = year
    my_car.purchase_price = price
    my_car.calc_current_value(current_year)
    my_car.print_info()