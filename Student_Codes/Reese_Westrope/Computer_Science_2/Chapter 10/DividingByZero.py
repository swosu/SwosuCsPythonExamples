


try:
    user_num = int(input("Enter the number you want to divide."))
    div_num = int(input("Enter the number you want to divide by."))
except ValueError:
    print("Value Error: All your numbers must be an integer (no decimal points, no letters)")
try: 
    quotient = user_num/div_num 
except ZeroDivisionError:
    print("Zero Division Error: The number you want to divide by can not equal zero.")

print(f"Your quotient is {quotient}.")
