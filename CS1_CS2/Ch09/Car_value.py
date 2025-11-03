class Car:
    def __init__(self):
        self.model_year = 0
        self.purchase_price = 0
        self.current_value = 0
        self.been_crashed = False
        self.number_of_miles = 0
        self.proof_of_ownership = True

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        # Car depreciation formula
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)
    
    def print_info(self):
        print("Car's information:")
        print("   Model year:", self.model_year)
        print("   Purchase price: ${:,}".format(self.purchase_price))
        print("   Current value: ${:,}".format(self.current_value))


if __name__ == "__main__":    
    year = int(input("Enter the car's model year: ")) 
    price = int(input("Enter the purchase price: "))
    current_year = int(input("Enter the current year: "))

    elizabeth = Car()
    elizabeth.model_year = year
    elizabeth.purchase_price = price
    elizabeth.calc_current_value(current_year)
    elizabeth.print_info()