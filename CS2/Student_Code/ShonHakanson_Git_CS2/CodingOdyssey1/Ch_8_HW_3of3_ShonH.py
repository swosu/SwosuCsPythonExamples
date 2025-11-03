# Ch_8_HW_3of3_ShonH, 8.18 Lab: Elements in a Range
#Write a program that first gets a list of integers from input. That list is followed by two more integers 
# representing lower and upper bounds of a range. Your program should output all integers from the list 
# that are within that range (inclusive of the bounds).
#For coding simplicity, follow each output integer by a comma, even the last one. Do not end with newline.

def find_int_in_range():
    usable_numbers = []
    usable_numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    lower_bound = int(input("Enter the lower bound of the range: "))    
    upper_bound = int(input("Enter the upper bound of the range: "))
    found_numbers = [num for num in usable_numbers if lower_bound <= num <= upper_bound]
    found_numbers.sort()
    print("Numbers within the range [{}, {}]: ".format(lower_bound, upper_bound), end="")
    output = ",".join(str(num) for num in found_numbers)
    if output:
        print(f"{output},", end="")

if __name__ == "__main__":
    find_int_in_range()