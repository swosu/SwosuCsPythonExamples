#take an amount of cash, return the change options.
amount_due =  float(7.25)
amount_given = float(10.00)
cash = amount_given - amount_due
print(f"Amount due: ${amount_due}\nAmount recieved: ${amount_given}\nChange due: ${cash}")

#listed denominations 
dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

#check divisibility for coins and ones
while cash > 0:
    if cash >= 1:
        dollars += 1
        cash -= 1
        #print('passed more than 1 check')
    elif cash < 1:
        if cash % 0.25 == 0:
            #print('.25 passed')
            quarters += 1
            cash -= 0.25
        elif cash % 0.10 == 0:
            #print('.10 passed')
            quarters += 1
            cash -= 0.25
        elif cash % 0.05 == 0:
            #print('0.05 passed')
            nickels += 1
            cash -= 0.05
        else:
            pennies += 1
            cash -= 0.01
    #print(cash) #checking pass throughs 

print(f'Dollar(s): {dollars}')
print(f'Quarter(s): {quarters}')
print(f'Dime(s): {dimes}')
print(f'Nickel(s): {nickels}')
print(f'Pennie(s): {pennies}')

#Sources: https://www.toppr.com/guides/python-guide/examples/python-examples/functions/number-divisible/python-program-find-numbers-divisible-another-number/
#https://www.youtube.com/watch?v=9-Cpi3hGjrY
