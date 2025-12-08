#Ch 9 HW Shon Hakanson, 9.11: Car value
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
        print(f"Model Year: {self.model_year}")
        print(f"Purchase Price: ${self.purchase_price:,.0f}")
        print(f"Current Value: ${self.current_value:,.0f}")


if __name__ == "__main__":    
    
    car_obj = Car()
    car_obj.model_year = int(input("Input the model year of the car: "))
    car_obj.purchase_price = int(input("Input the purchase price of the car: "))
    current_year = int(input("Input the current year: "))
    car_obj.calc_current_value(current_year)
    car_obj.print_info()