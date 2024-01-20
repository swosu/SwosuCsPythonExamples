num1 = float(input("Enter a number here:"))
num2 = float(input("Enter another number:"))
num3 = float(input("Enter another number:"))
num4 = float(input("Enter one more number here:"))

print("The product of your numbers is about",f'{num1*num2*num3*num4:.0f}',"and the average of your numbers is about",f'{(num1*num2*num3*num4)/4:.0f}')
print("The product of your numbers is exactly",f'{num1*num2*num3*num4:.3f}',"and the average of your numbers is exactly",f'{(num1*num2*num3*num4)/4:.3f}')