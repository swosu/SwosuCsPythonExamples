total_money = 10.52


def function(amount):
    dollar, quaters, dimes, nickels, pennies = 0, 0, 0, 0, 0
    while amount > 0:
        if amount >= 1:
            dollar += 1
            amount -= 1
        if amount >= 0.25:
            quaters += 1
            amount -= 0.25
        elif amount >= 0.10:
            dimes += 1
            amount -= 0.10
        elif amount >= 0.05:
            nickels += 1
            amount -= 0.05
        else:
            pennies += 1
            amount -= 0.01
    print('Quaters: ', quaters)
    print('Dimes: ', dimes)
    print('Nickels: ', nickels)
    print('Pennies: ', pennies)

function(total_money)


