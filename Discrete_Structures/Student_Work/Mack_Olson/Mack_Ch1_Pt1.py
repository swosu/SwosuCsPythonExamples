def get_two_real_numbers():
    while True:
        try:
            num1 = float(input("Enter the first real number: "))
            num2 = float(input("Enter the second real number: "))

            print(f"Valid real numbers entered: {num1}, {num2}")

            # Convert numbers to binary (integer part only)
            binary_num1 = bin(int(num1))[2:]  # Convert integer part to binary
            binary_num2 = bin(int(num2))[2:]

            print(f"First number: {num1} -> {binary_num1}")
            print(f"Second number: {num2} -> {binary_num2}")
            
            break  # Exit loop if valid numbers are entered

        except ValueError:
            print("Invalid input. Please enter valid real numbers.")

get_two_real_numbers()
