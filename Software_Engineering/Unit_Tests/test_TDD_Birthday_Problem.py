def test_birthday_generator(self):
    result = random_birthday_picker()
    while result != 1:
        result = random_birthday_picker()
    self.assertEqual(result, 1)def add_numbers(a, b):
    return a + bdef add_numbers(a, b):
    return a + b