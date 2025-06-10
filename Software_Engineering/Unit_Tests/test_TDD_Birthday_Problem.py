def test_birthday_generator(self):
    # Test case 1: Check if the generated birthday is within a valid range
    birthday = birthday_generator()
    self.assertTrue(1 <= birthday <= 365, "Generated birthday is not within a valid range")

    # Test case 2: Check if the generated birthday is an integer
    birthday = birthday_generator()
    self.assertIsInstance(birthday, int, "Generated birthday is not an integer")

    # Test case 3: Check if the generated birthday is unique
    birthdays = set()
    for _ in range(100):
        birthday = birthday_generator()
        self.assertNotIn(birthday, birthdays, "Generated birthday is not unique")
        birthdays.add(birthday)