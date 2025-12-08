#Character Builder class that when called on gives specific input options to customize a character's appearance.
# The character's attributes include hair color, hair length, eye color, height, and build.
class Character:
    def __init__(self, name):
        self.name = name
        self.hair_color = "Brown"
        self.hair_length = "Short"
        self.eye_color = "Blue"
        self.height = "Average"
        self.build = "Average"

    def describe(self):
        print("\n--- Character Profile ---")
        print(f"Name: {self.name}")
        print(f"Hair: {self.hair_length} {self.hair_color}")
        print(f"Eyes: {self.eye_color}")
        print(f"Height: {self.height}")
        print(f"Build: {self.build}")
        print("-------------------------\n")

    def customize(self, attribute, value):
        if hasattr(self, attribute):
            setattr(self, attribute, value)
            print(f"{attribute.replace('_',' ').title()} updated to {value}.\n")
        else:
            print("Invalid attribute.\n")


def character_builder():
    name = input("Enter your character's name: ")
    char = Character(name)

    while True:
        char.describe()
        print("Customization Menu:")
        print("1. Change Hair Color")
        print("2. Change Hair Length")
        print("3. Change Eye Color")
        print("4. Change Height")
        print("5. Change Build")
        print("6. Exit Builder")

        choice = input("Choose an option: ")

        if choice == "1":
            new_color = input("Enter hair color (e.g., Blonde, Black, Red): ")
            char.customize("hair_color", new_color)

        elif choice == "2":
            new_length = input("Enter hair length (Short, Shaggy, Long): ")
            char.customize("hair_length", new_length)

        elif choice == "3":
            new_eye = input("Enter eye color: ")
            char.customize("eye_color", new_eye)

        elif choice == "4":
            new_height = input("Enter height (Short, Tall): ")
            char.customize("build", new_height)

        elif choice == "5":
            new_build = input("Enter build (Slim, Average, Muscular, Fat): ")
            char.customize("build", new_build)

        elif choice == "6":
            print("\nFinal Character:")
            char.describe()
            print("Character creation complete!")
            break
        else:
            print("Invalid choice, try again.\n")


# Run the builder
if __name__ == "__main__":
    character_builder()
