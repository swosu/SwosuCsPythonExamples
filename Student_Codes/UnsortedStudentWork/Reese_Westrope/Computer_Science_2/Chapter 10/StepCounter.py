

def steps_to_miles(num_of_steps):
    miles_walked = num_of_steps/2000
    if num_of_steps <= 0:
        raise ValueError("You can't walk negative steps.")
    else:
        print(f"You walked {miles_walked} miles.")



if __name__ == "__main__":

    steps_walked = int(input("How many steps did you walk?\n:"))

    try:
        steps_to_miles(steps_walked)
    except ValueError as error_message:
        print(f"ValueError: {error_message}")


