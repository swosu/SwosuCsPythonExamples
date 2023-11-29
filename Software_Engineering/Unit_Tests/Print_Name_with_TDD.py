import unittest

class TestPrintName(unittest.TestCase):

    def test_print_name(self):
        self.assertEqual(print_name("jOhN", "sMiTh"), "John Smith")