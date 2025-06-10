import unittest

import os

def print_file_name():
    # Get the file name from the __file__ attribute
    file_name = os.path.basename(__file__)
    print(f"The name of this file is: {file_name}")
    print(f"The value of __name__ is: {__name__}")

# Function to be tested
def add(a, b):
    return a + b

class driving_costs:

    def __init__(self, miles_per_gallon:25, dollars_per_gallon:4, miles_driven:100):
        self.miles_per_gallon = miles_per_gallon
        self.dollars_per_gallon = dollars_per_gallon
        self.miles_driven = miles_driven

    def set_miles_per_gallon(self, miles_per_gallon):
        self.miles_per_gallon = miles_per_gallon

    @staticmethod
    def get_miles_per_gallon():
        return self.miles_per_gallon

# Unit test class
class TestAddFunction(unittest.TestCase):
    #print_file_name()

    def test_add_integers(self):
        self.assertEqual(add(1, 2), 3, "1 plus 2 as integers did not work.")
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
    
    def test_add_floats(self):
        self.assertAlmostEqual(add(1.1, 2.2), 3.3)
        self.assertAlmostEqual(add(-1.1, 1.1), 0.0)
    
    def test_add_strings(self):
        self.assertEqual(add('foo', 'bar'), 'foobar')

    def test_add_lists(self):
        self.assertEqual(add([1, 2], [3, 4]), [1, 2, 3, 4])

    def test_driving_costs_get_miles_per_gallon(self):
        self.assertEqual(driving_costs.get_miles_per_gallon(), 25)

    # I want to set driving costs to 30 miles per gallon
    def test_driving_costs_set_miles_per_gallon(self):
        driving_costs.set_miles_per_gallon(30)
        self.assertEqual(driving_costs.get_miles_per_gallon(), 30)

if __name__ == '__main__':
    unittest.main()
