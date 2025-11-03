import unittest

class Car_class:
    def __init__(self):
        self.model_year = 0
        self.purchase_price = 0  # Added attribute purchase_price
        self.current_value = 0
        self.mileage = 0

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)

    def print_info(self):
        print("Car's information:")
        print(f"  Model year: {self.model_year}")
        print(f"  Purchase price: ${self.purchase_price}")
        print(f"  Current value: ${self.current_value}")



class TestCar(unittest.TestCase):

    def test_initial_values(self):
        car_object = Car_class()
        self.assertEqual(car_object.model_year, 0)
        self.assertEqual(car_object.purchase_price, 0)
        self.assertEqual(car_object.current_value, 0)
        self.assertEqual(car_object.mileage, 0)

    def test_calc_current_value(self):
        car_object = Car_class()
        car_object.model_year = 2011
        current_year = 2018
        car_object.purchase_price = 18000
        car_object.calc_current_value(2018)
        expected_value = round(18000 * (1 - 0.15) ** (2018 - 2011))
        self.assertEqual(car_object.current_value, expected_value)

    def test_print_info(self):
        car_object = Car_class()
        car_object.model_year = 2011
        car_object.purchase_price = 18000
        car_object.calc_current_value(2018)
        
        expected_output = (
            "Car's information:\n"
            "  Model year: 2011\n"
            "  Purchase price: $18000\n"
            "  Current value: $5770\n"
        )

        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output
        car_object.print_info()
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
