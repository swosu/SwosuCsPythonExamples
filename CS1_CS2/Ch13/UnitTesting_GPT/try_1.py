# test_example.py
import unittest

def add(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5, "Adding 2 and 3 should equal 5. Got {0}".format(result))

    def test_add_two_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_one_positive_one_negative(self):
        result = add(-2, 3)
        self.assertEqual(result, 1)



if __name__ == "__main__":
    unittest.main()
