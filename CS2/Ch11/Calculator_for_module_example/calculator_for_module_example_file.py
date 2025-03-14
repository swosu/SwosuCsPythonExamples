# calculator.py

import math_functions as mth_fun




def main(our_words):

    print("Testing Dictionary")
    # get the definition of a word
    #print off the keys from the dictioanry
    

    # change the name of the person from John to Steve
    our_words.our_dictionary["name"] = "Steve"
    print(our_words.our_dictionary["name"])

    # now delete our local copy of our_words and reimport and run it again
    del our_words
    import Dictionary_file as our_other_words
    print(our_other_words.our_dictionary["name"])
    print(our_other_words.our_dictionary.keys())
    print(our_other_words.our_dictionary.values())


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

    import Dictionary_file as our_words
    print(our_words.our_dictionary.keys())
    print("hello from calculator.py")
    main(our_words)
