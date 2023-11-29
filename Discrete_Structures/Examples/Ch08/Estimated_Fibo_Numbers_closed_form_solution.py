print('hello.')

fibos = [0, 1]

# estimate fibo numbers using closed form solution

constant_one = (1 / 5 ** 0.5)

constant_two = (-1 / 5 ** 0.5)

base_part = (1 + 5 ** 0.5) / 2

for fibo_number in range(2, 100):
    fibos.append(int(constant_one * base_part ** fibo_number - constant_two * base_part ** fibo_number))


# print the first 100 fibo numbers, 10 numbers per line
print('fibo:', end = ' ')
for i in range(100):
    print(fibos[i], end = ' ')

    if i % 10 == 9:
        print()