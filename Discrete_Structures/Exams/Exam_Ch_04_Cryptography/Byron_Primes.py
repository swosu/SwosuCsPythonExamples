ctr = 0

n = 25

for num in range(n):
    if num <= 1:
        continue
    for i in range (2,num):
        if (num % i) == 0:
            break

    else:
        ctr += 1

print(f'count was: {ctr}.')