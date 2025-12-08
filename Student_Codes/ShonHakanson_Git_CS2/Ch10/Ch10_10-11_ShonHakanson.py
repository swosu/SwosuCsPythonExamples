#Ch 10 Homework, 10.11: StepCounter Exceptions, Shon Hakanson


def step_counter(num_of_steps):
    num_of_steps = float(num_of_steps)
    num_of_miles = num_of_steps / 2000
    if num_of_steps < 0:
        raise ValueError("Exception: Negative step count entered.")
    else:
        return num_of_miles
    
if __name__ == "__main__":
    try:
        steps_input = input("Enter the number of steps taken: ")
        print(f"You have walked {(step_counter(steps_input)):.2f} miles")
    except ValueError as val_error_message:
        print(val_error_message)
