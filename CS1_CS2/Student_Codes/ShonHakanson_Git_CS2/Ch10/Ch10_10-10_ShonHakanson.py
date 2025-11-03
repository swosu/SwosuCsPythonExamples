#Ch10 Homework, Lab 10.10: Simple Integer Division, Multiple Exception Handlers

#Write a program that reads integers user_num and div_num as input, and output the quotient (user_num divided by div_num). Use a try block to perform all the statements. Use an except block to catch any ZeroDivisionError as a 
# variable and output "Zero Division Exception: " followed by the exception message from the variable. Use 
# another except block to catch any ValueError caused by invalid input as a variable and output 
# "Input Exception: " followed by the exception message from the variable.

#Note: ZeroDivisionError is raised when a division by zero happens. ValueError is raised when a user enters a 
# value of different data type than what is defined in the program. Do not include code to raise any exception 
# in the program.


try:
    user_number = input("Enter an integer to be divided: ")
    div_number = input("Enter another integer to divide the first: ")
    quotient = int(user_number) / int(div_number)
    print(f"{quotient:.0f}")
except ZeroDivisionError as zero_div_err:
    print(f"Zero Division Exception: {zero_div_err}")
except ValueError as val_err:
    print(f"Input Exception: {val_err}")