# calculator.py

import math_functions as mth_fun

import Dictionary as our_words

def main():

    print("Testing Dictionary")
    # get the definition of a word
    #print off the keys from the dictioanry
    print(our_words.our_dict.keys())


    print("Simple Calculator")
    print("Options: add, subtract, multiply, divide")
    
    operation = input("Choose an operation: ").strip().lower()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "add":
        result = mth_fun.add(num1, num2)
    elif operation == "subtract":
        result = mth_fun.subtract(num1, num2)
    elif operation == "multiply":
        result = mth_fun.multiply(num1, num2)
    elif operation == "divide":
        result = mth_fun.divide(num1, num2)
    else:
        result = "Invalid operation."

    print("Result:", result)

if __name__ == "__main__":
    print("hello from calculator.py")
    main()
