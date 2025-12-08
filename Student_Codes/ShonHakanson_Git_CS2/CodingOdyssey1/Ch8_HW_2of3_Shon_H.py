#Ch8_HW_2of3_Shon_Hakanson, Problem 8.17: Filter and Sort a List
#Write a program that gets a list of integers from input, and outputs negative integers 
# in descending order (highest to lowest).


def main():
    int_list = []
    if True:
        try:
            int_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
        except ValueError:
            print("Invalid input. Please enter integers only.")
    neg_ints = [num for num in int_list if num < 0]
    neg_ints.sort(reverse=True)
    print("Negative integers in descending order:", neg_ints)

if __name__ == "__main__":
    main()