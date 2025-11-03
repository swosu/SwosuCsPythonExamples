user_num = int(input('Enter a big number you want to see divided by something three times:\n'))
#user_num = int(input())
x = int(input('Enter a small number you want to divide by:\n'))
#------------*x = int(input())

num_1 = int(user_num / x)
num_2 = int(num_1 / x)
num_3 = int(num_2 / x)

print(num_1, num_2, num_3)