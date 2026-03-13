"""
Barking Dog String Lab

Sparky the dog will guide us through a series of
string exploration challenges.

Students should write small pieces of code in VS Code
to solve each challenge.
"""

class Dog:

    def __init__(self, name):
        self.name = name
        self.commands = [
            "Enter a string from the user.",
            "Print the string in ALL UPPERCASE.",
            "Print the string in all lowercase.",
            "Count how many characters are in the string.",
            "Print the first character of the string.",
            "Print the last character of the string.",
            "Replace spaces with underscores.",
            "Split the string into words.",
            "Join the words back together with hyphens.",
            "Print the string backwards."
        ]

    def bark(self, message):
        print(f"\n🐶 {self.name} barks: {message}")

    def puppy_eyes(self):
        print(f"{self.name} tilts head and gives you very convincing puppy-dog eyes...")

    def wag_tail(self):
        print(f"{self.name}'s tail wags enthusiastically!")

    def run_lab(self):

        print("\n==============================")
        print("SPARKY'S STRING ADVENTURE LAB")
        print("==============================")

        self.bark("Hello human! Today we explore STRING OBJECTS!")

        self.puppy_eyes()

        print("\nSparky has some coding challenges for you...\n")

        for i, command in enumerate(self.commands, start=1):

            print("-----------------------------------")
            print(f"Challenge {i}")
            print("-----------------------------------")

            self.bark(command)

            input("\nPress ENTER after you try this in VS Code...")

            self.wag_tail()

        print("\nAll challenges complete!")

        self.bark("Great job exploring strings!")
        self.bark("Remember: a string is an OBJECT created from the str class!")

        print("\nSparky sits proudly and waits for a treat.")


# ---------------------------------------------------
# Main Program
# ---------------------------------------------------

sparky = Dog("Sparky")

sparky.run_lab()