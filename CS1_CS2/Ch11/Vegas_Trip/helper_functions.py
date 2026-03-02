def ask_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    number = ask_integer("Please enter an integer you potato: ")
    print(f"You entered: {number}. I am so proud.")