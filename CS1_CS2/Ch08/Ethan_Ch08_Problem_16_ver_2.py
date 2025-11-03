def get_float_numbers():
    numbers = []
    while True:
        user_input = input("Enter a floating point number (or 'done' to finish): ")
        if user_input == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid floating point number.")
    return numbers

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0.0
    total = sum(numbers)
    average = total / len(numbers)
    return average

def find_maximum(numbers):
    if len(numbers) == 0:
        return None
    return max(numbers)

def find_minimum(numbers):
    if len(numbers) == 0:
        return None
    return min(numbers)

def print_output(numbers, average, maximum, minimum):
    print("Numbers: ", ", ".join([f"{num:.2f}" for num in numbers]))
    print("Average: {:.2f}".format(average))
    print("Maximum: {:.2f}".format(maximum))
    print("Minimum: {:.2f}".format(minimum))

# Main program
number_list = get_float_numbers()
average_value = calculate_average(number_list)
maximum_value = find_maximum(number_list)
minimum_value = find_minimum(number_list)
print_output(number_list, average_value, maximum_value, minimum_value)