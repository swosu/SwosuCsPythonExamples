import unittest
import random

def random_birthday_picker():
    return random.randint( 1 , 366 )

class Test_Random_Birthday_Picker(unittest.TestCase):
    test_run_limit = 100000
    def test_random_birthday_picker_in_range(self):
        for goal_date in range(1, 366+1):
            #print(f"Looking for {goal_date}")
            count = 0
            result = random_birthday_picker()
            while result != goal_date:
                count += 1
                result = random_birthday_picker()
                # if our count has exceeded the run limit for the class
                # break the loop
                if self.test_run_limit < count:
                    break

            if self.test_run_limit > count:
                # tell the user the goal date if this fails and that it exceeded the limit
                self.assertEqual(result, goal_date, f"Test run limit exceeded: {self.test_run_limit} when looking for {goal_date}")
            elif self.test_run_limit <= count:
                self.assertLess(count, self.test_run_limit, 
                                f"Test run limit exceeded: {self.test_run_limit} when looking for {goal_date}")

    def test_random_birthday_picker_out_of_range_positive(self):
        #print(f"Looking for {goal_date}")
            count = 0
            result = random_birthday_picker()
            upper_limit = 366
            while result <= upper_limit:
                count += 1
                result = random_birthday_picker()
                # if our count has exceeded the run limit for the class
                # break the loop
                if self.test_run_limit < count:
                    break

            if self.test_run_limit > count:
                # test pass if result is less than or equal to upper limit
                print('our result is...', result)
                self.assertTrue(result <= upper_limit, f"Result is {result} and is greater than {upper_limit}")
            else:
                self.assertLess( self.test_run_limit, count,
                                f"Test run limit exceeded: {self.test_run_limit} when testing upper limit")
                
    def test_random_birthday_picker_out_of_range_negative(self):
        count = 0
        result = random_birthday_picker()
        lower_limit = 0
        while result >= lower_limit:
            count += 1
            result = random_birthday_picker()
            # if our count has exceeded the run limit for the class
            # break the loop
            if self.test_run_limit < count:
                break

        if self.test_run_limit > count:
            # test pass if result is greater than or equal to lower limit
            print('our result is...', result)
            self.assertTrue(result > lower_limit, f"Result is {result} and is less than {lower_limit}")
if __name__ == '__main__':
    unittest.main()