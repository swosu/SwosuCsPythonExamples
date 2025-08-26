import random
def change_making(coins, amount):
    print(f'inside function {coins}')
    n = len(coins)
    ans =[]
    for i in range(n-1, -1,-1):
        print(f'check our first ccoin: {coins[i]}.')
        while amount >= coins[i]:
            amount -= coins[i]
            ans.append(coins[i])
    return ans

def print_answer(change, coins):
    print('inside the printing answer definition')
    n = len(coins)
    for i in range(n-1, -1,-1):
        print(f'check our first ccoin: {coins[i]}.')
        coin_count = change.count(coins[i])
        print(f'coin count for {coins[i]} was {coin_count}.')

        if 25 == coins[i]:
            if coin_count > 1:
                print(f'your change was {coin_count} quarters')
            elif 1 == coin_count:
                print(f'your change was 1 quarter.')


print('hello')         
coins = [1,5,10,25, 50, 100]
print(coins)
amount = random.randint(50, 5000)
print(amount)

change = change_making(coins, amount)
print(change)

print_answer(change, coins)