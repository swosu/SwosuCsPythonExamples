import unittest
from unittest.mock import patch

# Import from your extended version file
# Make sure the file is named exactly this: fat_burner_example_extended_version.py
from fat_burner_example_extended_version import get_age, fat_burning_heart_rate, AgeError


class TestHeartRateCalculator(unittest.TestCase):

    def test_valid_age(self):
        """Test normal valid age input (should succeed)."""
        with patch("builtins.input", return_value="35"):
            print("\n[TEST] Testing valid age input: 35")
            age = get_age()
            self.assertEqual(age, 35, "Age should be exactly 35")
            heart_rate = fat_burning_heart_rate(age)
            print(f"    → Calculated heart rate: {heart_rate}")
            self.assertAlmostEqual(heart_rate, 129.5, msg="Heart rate calculation incorrect")

    def test_invalid_age_low(self):
        """Test age below valid range (should raise AgeError)."""
        with patch("builtins.input", return_value="17"):
            print("\n[TEST] Testing invalid low age input: 17")
            with self.assertRaises(AgeError) as cm:
                get_age()
            print(f"    → Raised error: {cm.exception}")
            self.assertEqual(str(cm.exception), "Invalid age.", "Error message should be 'Invalid age.'")

    def test_invalid_age_high(self):
        """Test age above valid range (should raise AgeError)."""
        with patch("builtins.input", return_value="100"):
            print("\n[TEST] Testing invalid high age input: 100")
            with self.assertRaises(AgeError) as cm:
                get_age()
            print(f"    → Raised error: {cm.exception}")
            self.assertEqual(str(cm.exception), "Invalid age.", "Error message should be 'Invalid age.'")

    def test_non_numeric_input(self):
        """Test non-numeric input (should raise AgeError with custom message)."""
        with patch("builtins.input", return_value="dog"):
            print("\n[TEST] Testing non-numeric input: 'dog'")
            with self.assertRaises(AgeError) as cm:
                get_age()
            print(f"    → Raised error: {cm.exception}")
            self.assertEqual(str(cm.exception), "Age must be a number.", "Error message should be 'Age must be a number.'")


if __name__ == "__main__":
    # Run tests with maximum verbosity
    unittest.main(verbosity=2)
