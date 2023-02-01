total_cost = float(input('How much does your cart cost?'))
amount_paid = float(input('How much are you giving the cashier?'))
cash_back = amount_paid - total_cost

dollars_back = 0
quarters_back = 0
dimes_back = 0
nickels_back = 0
pennies_back = 0

print('Your cash back will be $','{:.2f}'.format(cash_back))

if cash_back < 0:
    print('You still owe the cashier $','{:.2f}'.format(-cash_back))

elif 1 <= cash_back:
    while 1 <=cash_back:
        cash_back = cash_back-1.00
        dollars_back = dollars_back + 1

    while 0.25 <= cash_back:
        cash_back = cash_back - 0.25
        quarters_back = quarters_back + 1

    while 0.10<=cash_back:
        cash_back = cash_back - 0.10
        dimes_back = dimes_back +1

    while 0.05<=cash_back:
        cash_back = cash_back - 0.05
        nickels_back = nickels_back +1

    while 0.01<=cash_back:
        cash_back = cash_back - 0.01
        pennies_back = pennies_back + 1

dollar_word = ''
quarter_word = ''
dime_word = ''
nickel_word = ''
penny_word = ''

if dollars_back == 1:
    dollar_word = 'dollar'
else:
    dollar_word = 'dollars'

if quarters_back == 1:
    quarter_word = 'quarter'
else:
    quarter_word = 'quarters'

if dimes_back == 1:
    dime_word = 'dime'
else:
    dime_word = 'dimes'

if nickels_back == 1:
    nickel_word = 'nickel'
else:
    nickel_word = 'nickels'

if pennies_back == 1:
    penny_word = 'penny'
else:
    penny_word = 'pennies'

print('The cashier will give you',dollars_back,dollar_word,quarters_back,quarter_word,dimes_back,dime_word,nickels_back,nickel_word,', and',pennies_back,penny_word)