"""
A half-life is the amount of time it takes for a substance
or entity to fall to half its original value.
Caffeine has a half-life of about 6 hours in humans.
Given caffeine amount (in mg) as input,
output the caffeine level after 6, 12, and 24 hours.
Use a string formatting expression with conversion
specifiers to output the caffeine amount as floating-point numbers.

Output each floating-point value with two digits after
the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

Ex: If the input is:

100
the output is:

After 6 hours: 50.00 mg
After 12 hours: 25.00 mg
After 24 hours: 6.25 mg

Note: A cup of coffee has about 100 mg. A soda has about 40 mg. An "energy" drink (a misnomer) has between 100 mg and 200 mg.



starter code from inside book:

caffeine_mg = float(input())

''' Type your code here. '''
"""

caffeine_mg = float(input("How much caffine do we start with?"))
print(f"""
You entered a value for initial caffine.
That value was {caffeine_mg}.
Thank you and carry on.
""")
print('After 6 hours: ', end = '')
print(f'{(caffeine_mg / 2.0):.2f}')
#After 12 hours: 25.00 mg
#After 24 hours: 6.25 mg
#print(f'{your_value:.2f}')
