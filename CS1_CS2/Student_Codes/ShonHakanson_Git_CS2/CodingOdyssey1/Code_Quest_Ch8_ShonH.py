import random

def pick_restaurant():
    # Start with a default list of restaurants
    restaurants = ["Olive Garden", "Buffalo Wild Wings", "Texas Roadhouse", "Hideaway Pizza", "Senor Salsa", "Chick-Fil-A"]

    while True:
        print("\nCurrent restaurants:", restaurants)
        choice = input("Type 'add' to add a restaurant, 'pick' to choose randomly, or 'quit' to exit: ").lower()

        if choice == "add":
            new_restaurant = input("Enter the restaurant name: ")
            restaurants.append(new_restaurant)
            print(f"{new_restaurant} added!")

        elif choice == "pick":
            
                picked = random.choice(restaurants)
                print(f"\n🎉 You should go to: {picked}!")
                break

        elif choice == "quit":
            print("Good luck with your meal!")
            break

        else:
            print("Invalid choice. Try 'add', 'pick', or 'quit'.")

if __name__ == "__main__":
    pick_restaurant()