our_string = "hello"
print(our_string + ": print the string")
print(our_string.capitalize())
print(our_string.upper())
print(our_string)

# change our_string to all uppercase
our_string = our_string.upper()
print(our_string)

print("starting our new example.")

class IntegerStringChecker:
    def __init__(self, user_string):
        self.user_string = user_string

    def is_integer(self):
        return self.user_string.isdigit()

    def __str__(self):
        return "Yes" if self.is_integer() else "No"

# Example usage:
user_string = input("Enter a string: ")
checker = IntegerStringChecker(user_string)
print(checker)
