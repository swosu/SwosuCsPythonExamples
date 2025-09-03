# test_parser.py

import unittest
from unittest.mock import patch
from parser import parse_input


class TestParseInput(unittest.TestCase):

    @patch("builtins.input", side_effect=["14.25", "25", "0", "5.75", "done", "y", "n"])
    def test_valid_numbers(self, mock_input):
        """Valid input should be collected into a list of floats."""
        result = parse_input()
        self.assertEqual(result, [14.25, 25.0, 0.0, 5.75])

    @patch("builtins.input", side_effect=["14.25", "oops", "25", "done", "y", "n"])
    def test_reject_non_numbers(self, mock_input):
        """Non-numbers should be rejected and retried."""
        result = parse_input()
        self.assertEqual(result, [14.25, 25.0])

    @patch("builtins.input", side_effect=["done", "y", "n"])
    def test_empty_list(self, mock_input):
        """User should be able to finish without entering numbers."""
        result = parse_input()
        self.assertEqual(result, [])

    @patch("builtins.input", side_effect=["14.25", "done", "n", "y", "n"])
    def test_add_more_numbers(self, mock_input):
        """User should be asked if they want to add more numbers after done."""
        result = parse_input()
        self.assertEqual(result, [14.25])

    @patch("builtins.input", side_effect=["14.25", "done", "y", "y", "n"])
    def test_confirm_proceed_past_phase(self, mock_input):
        """User must confirm before proceeding past parse phase."""
        result = parse_input()
        self.assertEqual(result, [14.25])

    def test_parser_has_docstring(self):
        """Ensure parse_input has a meaningful docstring."""
        from parser import parse_input
        self.assertIsNotNone(parse_input.__doc__)
        self.assertTrue(len(parse_input.__doc__.strip()) > 10)  # not empty, not trivial



if __name__ == "__main__":
    unittest.main()
