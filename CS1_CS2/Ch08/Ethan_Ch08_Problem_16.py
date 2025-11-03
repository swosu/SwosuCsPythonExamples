def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter a floating point number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid floating point number.")
    return numbers

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_maximum(numbers):
    return max(numbers)

def find_minimum(numbers):
    return min(numbers)

def print_output(numbers, average, maximum, minimum):
    print("List of numbers:", ", ".join([f"{num:.2f}" for num in numbers]))
    print("Average:", f"{average:.2f}")
    print("Maximum:", f"{maximum:.2f}")
    print("Minimum:", f"{minimum:.2f}")

if __name__ == "__main__":
    numbers = get_numbers()
    average = calculate_average(numbers)
    maximum = find_maximum(numbers)
    minimum = find_minimum(numbers)
    print_output(numbers, average, maximum, minimum)
