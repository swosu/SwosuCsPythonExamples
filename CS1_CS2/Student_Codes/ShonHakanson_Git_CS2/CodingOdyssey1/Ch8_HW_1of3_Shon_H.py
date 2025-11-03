# Ch8_HW_1of3_Shon_Hakanson, Problem 8.16: Varied Amount of Input Data
#Statistics are often calculated with varying amounts of input data. 
# Write a program that takes any number of non-negative floating-point numbers
# as input, and outputs the max and average, respectively.
#Output the max and average with two digits after the decimal point.


def main():
    numbers = []
    num_list_elements = int(input("Enter the number of elements you want to input: "))
    count = 0
    while count < num_list_elements:
        try:
            num = float(input("Enter a non-negative floating-point number: "))
            if num < 0:
                print("Negative number entered. Please enter a non-negative number.")
                continue
            numbers.append(num)
            count += 1
        except ValueError:
            print("Invalid input. Please enter a valid floating-point number.")

    if numbers:
        maximum = max(numbers)
        average = sum(numbers) / len(numbers)
        print(f"Max: {maximum:.2f}")
        print(f"Average: {average:.2f}")
    else:
        print("No non-negative numbers were entered.")

if __name__ == "__main__":
    main()