#input is 8.3, 10.4, 5.0, 4.8
#output is 2072, 7, 2071.680, 7.125
num1=float(input('please enter your first number'))
num2=float(input('please enter your second number'))
num3=float(input('please enter your third number'))
num4=float(input('please enter your fourth number'))


print(f'your values were {num1} {num2} {num3} {num4}')

'''Given 4 floating-point numbers.
Use a string formatting expression with conversion specifiers
to output their product and their average
as integers (rounded), then as floating-point numbers.
'''

int_product=int(num1)*int(num2)*int(num3)*int(num4)
print(f'your integer product was {int_product}.')
float_product=float(num1)*float(num2)*float(num3)*float(num4)
print(f'your float product was {float_product}.')
int_average=(int(num1)+int(num2)+int(num3)+int(num4))/4
print(f'your interger average was {int_average}.')
float_average=(float(num1)+float(num2)+float(num3)+float(num4))/4.0
print(f'your float product was {float_average}.')

print(f'{int_product:.0f}')
print(f'{int_average:.0f}')
print(f'{float_product:.3f}')
print(f'{float_average:.3f}')
