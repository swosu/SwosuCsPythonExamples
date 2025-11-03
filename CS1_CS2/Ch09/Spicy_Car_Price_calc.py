# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:17:48 2023

@author: evertj
"""
class Car:
    
    def __init__(self):
        self.data = []
        self.model_year = 0
        self.purchase_price = 0
        self.current_year = 0
        self.__mileage = 0
        self.__manufacturer = ''
        self.model = ''
        self.car_age = 0
    
    def print_model_year(self):
        print(f'INSIDE METHOD our model year is: {my_car_object.model_year}.')

    def set_mileage(self, mileage_from_user):
        self.__mileage = mileage_from_user

    def get_mileage(self):
        return self.__mileage
    
    def set_manufacturer(self, manufacturer_from_user):
        self.__manufacturer = manufacturer_from_user
        
    def calculate_current_car_value(self):
        depreciation_rate = 0.15
        # Car depreciation formula
        self.car_age = self.current_year - self.model_year
        print(self.car_age)
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** self.car_age)

    def print_car_info(self):
        print(f'model year: {self.model_year}.')
        print(f'purchase price: ${self.purchase_price}.')
        print(f'current value: ${self.current_value}.')

if __name__ == '__main__':
    print('welcome to the car value calculator.')
    
    my_car_object = Car()
    
    my_car_object.model_year = 2011
    print(f'our model year is: {my_car_object.model_year}.')
    my_car_object.print_model_year()
    
    my_car_object.purchase_price = 18_000
    my_car_object.current_year = 2018
    
    my_car_object.set_mileage(123456)
    
    # AttributeError: 'Car' object has no attribute '__mileage'
    #print(f'our mileage was: {my_car_object.__mileage}.')
    
    print(f'our car mileage was: {my_car_object.get_mileage()}.')
    
    my_car_object.set_manufacturer('Dodge')
    my_car_object.model = 'B100'
    
    my_car_object.calculate_current_car_value()
    
    my_car_object.print_car_info()
    
    
    