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
    
    
    # TODO: Define print_info() method to output model_year, purchase_price, and current_value
    def print_info(self):
        print(f'Model year: {self.model_year}')
        print(f'Purchase price: ${self.purchase_price}')
        print(f'Current value: ${self.current_value}')


if __name__ == "__main__":    
    user_input_model_year = int(input('what year was the vehicle made? ')) 
    user_input_purchase_price = int(input('how much did you pay for the vehicle? '))
    user_input_current_year = int(input('what is the current year?'))
    
    my_car = Car() # Create an instance of the Car class (make an object based on Car class)
    my_car.model_year = user_input_model_year
    my_car.purchase_price = user_input_purchase_price
    my_car.calc_current_value(user_input_current_year)
    my_car.print_info()