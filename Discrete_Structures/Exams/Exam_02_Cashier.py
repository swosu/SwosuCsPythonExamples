print('hello')

#https://www.geeksforgeeks.org/python-randint-function/
import random

# Generates a random number between
# a given positive range
total_dollars = random.randint(0, 101)
total_cents = random.randint(0, 101)
#print('our random dollars: ' + str(total_dollars))
#print('our random cents: ' + str(total_cents))
total = float(total_dollars) + float(total_cents)/100
print('our total is:' + "${:,.2f}".format(total))
# https://www.kite.com/python/answers/how-to-format-currency-in-python

payment = round(random.uniform(total, total+100),2)
print("our payment was" + "${:,.2f}".format(payment))

change = payment - total
print("our change should be" + "${:,.2f}".format(change))

remaining_change = change
#print("our remaining change is" + "${:,.2f}".format(remaining_change))

# first copy:
denomination = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.10, 0.05, 0.01]
how_much_of_each_denomination_to_give_back = []
for index in range(len(denomination)):
    print('Considering the denomination:' + \
    "${:,.2f}".format(denomination[index]))
    count = 0
    while denomination[index] <= remaining_change:
        remaining_change -= denomination[index]
        count += 1
        #print("after " + str(count) + " of money, " + str(denomination[index]) +\
        # "our remaining change is" + \
        # "${:,.2f}".format(remaining_change))
    print('we are going to give back ' + str(count) + " of " \
    "${:,.2f}".format(denomination[index]) )
    print("our remaining change is" + \
    "${:,.2f}".format(remaining_change))
    how_much_of_each_denomination_to_give_back.append(count)
