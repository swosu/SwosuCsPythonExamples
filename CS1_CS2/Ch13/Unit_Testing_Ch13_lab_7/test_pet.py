# test_pet.py
import unittest
from pet import Pet, Cat
from io import StringIO
import sys

class TestPet(unittest.TestCase):

    def test_pet_initialization(self):
        pet = Pet('Dobby', 2)
        self.assertEqual(pet.name, 'Dobby')
        self.assertEqual(pet.age, 2)

    def test_pet_print_info(self):
        pet = Pet('Dobby', 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        pet.print_info()
        sys.stdout = sys.__stdout__
        expected_output = "Pet Information:\n   Name: Dobby\n   Age: 2\n"
        self.assertEqual(captured_output.getvalue(), expected_output)


class TestCat(unittest.TestCase):

    def test_cat_initialization(self):
        cat = Cat('Kreacher', 3, 'Scottish Fold')
        self.assertEqual(cat.name, 'Kreacher')
        self.assertEqual(cat.age, 3)
        self.assertEqual(cat.breed, 'Scottish Fold')
        self.assertEqual(cat.is_fixed, True)
        self.assertTrue(cat.has_claws, True)

    def test_cat_print_info(self):
        cat = Cat('Kreacher', 3, 'Scottish Fold')
        captured_output = StringIO()
        sys.stdout = captured_output
        cat.print_info()
        sys.stdout = sys.__stdout__
        expected_output = "Pet Information:\n   Name: Kreacher\n   Age: 3\n   Breed: Scottish Fold\n   Fixed: True\n   Declawed: False\n"
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
