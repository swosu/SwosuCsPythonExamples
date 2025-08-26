import unittest

class Number_Adder():
    def __init__(self):
        self.data = []
        self.number_one = 0
        self.number_two = 0
        self.sum = 0

    def set_number_one(self, number):
        self.number_one = number

    def set_number_two(self, number):
        self.number_two = number

    def add_two_numbers(self):
        self.sum = self.number_one + self.number_two

    def get_sum(self):
        return self.sum


class TestNumberAdder(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_add_two_numbers(self):
        our_adder.set_number_one(10)
        our_adder.set_number_two(15)
        our_adder.add_two_numbers()
        self.assertEqual(our_adder.get_sum(), 25)


if __name__ == '__main__':
    our_adder = Number_Adder()
    our_adder.set_number_one(2)
    our_adder.set_number_two(3)
    unittest.main()
