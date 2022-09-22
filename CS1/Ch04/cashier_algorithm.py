"""
Write a program with total change amount as an integer
input, and output the change using the fewest coins,
one coin type per line.
The coin types are Dollars, Quarters, Dimes, Nickels,
and Pennies.

If the input is:

45
the output is:

1 Quarter
2 Dimes 

Bouns: Use singular and plural coin names as appropriate,
like 1 Penny vs. 2 Pennies.
"""
# assume a limit of $5.
change_due = int(input())
#print(f'change due back is {change_due}.')

working_change_left = change_due

dollar_count = 0
quarter_count = 0
dime_count = 0
nickel_count = 0
penny_count = 0


if 0 == change_due:
    print('No change')

else:
    
    # change is more than a dollar
    if 100 <= working_change_left:
        dollar_count += 1
        working_change_left -= 100
        #print(f'you still need to give back {working_change_left}.')
   
    if 100 <= working_change_left:
        dollar_count += 1
        working_change_left -= 100
        #print(f'you still need to give back {working_change_left}.')
        
    if 100 <= working_change_left:
        dollar_count += 1
        working_change_left -= 100
        #print(f'you still need to give back {working_change_left}.')
   
    if 100 <= working_change_left:
        dollar_count += 1
        working_change_left -= 100
        #print(f'you still need to give back {working_change_left}.')
        
    if 100 <= working_change_left:
        dollar_count += 1
        working_change_left -= 100
        #print(f'you still need to give back {working_change_left}.')
    
    # change is less than a dollar and more than a quarter
    if 25 <= working_change_left:
        quarter_count += 1
        working_change_left -= 25
        #print(f'you still need to give back {working_change_left}.')
        
    if 25 <= working_change_left:
        quarter_count += 1
        working_change_left -= 25
        #print(f'you still need to give back {working_change_left}.')
        
    if 25 <= working_change_left:
        quarter_count += 1
        working_change_left -= 25
        #print(f'you still need to give back {working_change_left}.')
        
    # change is less than a quarter and more than a dime
    
    if 10 <= working_change_left:
        dime_count += 1
        working_change_left -= 10
        #print(f'you still need to give back {working_change_left}.')
        
    if 10 <= working_change_left:
        dime_count += 1
        working_change_left -= 10
        #print(f'you still need to give back {working_change_left}.')
        
    # change is less than a dime and more than a nickel
    
    if 5 <= working_change_left:
        nickel_count += 1
        working_change_left -= 5
        #print(f'you still need to give back {working_change_left}.')
        
    # change is less than a nickel and more than a penny
    
    if 1 <= working_change_left:
        penny_count += 1
        working_change_left -= 1
        #print(f'you still need to give back {working_change_left}.')
        
    if 1 <= working_change_left:
        penny_count += 1
        working_change_left -= 1
        #print(f'you still need to give back {working_change_left}.')
        
    if 1 <= working_change_left:
        penny_count += 1
        working_change_left -= 1
        #print(f'you still need to give back {working_change_left}.')
        
    if 1 <= working_change_left:
        penny_count += 1
        working_change_left -= 1
        #print(f'you still need to give back {working_change_left}.')
    
    
# print off results

#print(f'you still need to give back {working_change_left}.')

if 1 == dollar_count:
    print('1 Dollar')
elif 1 < dollar_count:
    print(f'{dollar_count} Dollars')
    
if 1 == quarter_count:
    print('1 Quarter')
elif 1 < quarter_count:
    print(f'{quarter_count} Quarters')
    
if 1 == dime_count:
    print('1 Dime')
elif 1 < dime_count:
    print(f'{dime_count} Dimes')
    
if 1 == nickel_count:
    print('1 Nickel')
elif 1 < nickel_count:
    print(f'{nickel_count} Nickels')
    
if 1 == penny_count:
    print('1 Penny')
elif 1 < penny_count:
    print(f'{penny_count} Pennies')
    