# test_fibonacci.py

import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_base_cases(self):
        # Base cases
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_recursive_cases(self):
        # Check some common Fibonacci numbers
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(10), 55)

    def test_large_input(self):
        # Test a larger input to ensure function works for big numbers
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)

    def test_invalid_input(self):
        # Test negative input
        with self.assertRaises(ValueError):
            fibonacci(-1)
        # Optional: Handle non-integer input
        with self.assertRaises(TypeError):
            fibonacci("a string")
        with self.assertRaises(TypeError):
            fibonacci(5.5)

if __name__ == "__main__":
    unittest.main()
