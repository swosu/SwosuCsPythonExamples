import unittest
import random

def random_birthday_picker():
    return random.randint(1, 366)

class Test_Birthday_Problem(unittest.TestCase):
    test_run_limit = 10000
    def test_birthday_generator_get_one(self):
        result = random_birthday_picker()
        counter = 0
        while result != 1:
            counter += 1
            result = random_birthday_picker()    
            if result == 1:
                self.assertEqual(result, 1)
            elif counter > 10000:
                self.fail("No winner found after 10,000 tries")

    def test_birthday_generator_get_366(self):
        result = random_birthday_picker()
        counter = 0
        goal_date = 366
        while result != goal_date:
            counter += 1
            result = random_birthday_picker()    
            if result == goal_date:
                self.assertEqual(result, goal_date)
            elif counter > 10000:
                self.fail(f"No winner for {goal_date} found after 10,000 tries")
            

    # write a unit test to verify that after the test run limit, 
    #we will never have a negative birthday generated
    def test_birthday_generator_get_negative(self):
        result = random_birthday_picker()
        counter = 0
        while result > 0:
            counter += 1
            result = random_birthday_picker()    
            if result < 0:
                self.fail("Negative birthday generated")
            elif counter > 10000:
                self.assert
# If the script is run directly, execute the tests
if __name__ == '__main__':
    unittest.main()
