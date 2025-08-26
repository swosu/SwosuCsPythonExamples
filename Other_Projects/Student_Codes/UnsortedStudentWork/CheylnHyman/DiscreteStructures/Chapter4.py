import csv

def if_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

max_value = 100000 # 100,00 too big
counter = 0
number_of_primes = 0

while counter < max_value:
    if if_prime(counter):
        number_of_primes = number_of_primes + 1
    counter = counter + 1

number_of_primes = number_of_primes - 1

print(number_of_primes)
print(counter)
# create a new text file
#file = open('Chapter4.txt', 'w')

# open csv file
with open('Chapter4.csv', 'w', newline='') as csvfile:
    # create csv writer
    writer = csv.writer(csvfile, delimiter=',')
    # write header
    writer.writerow(['Number of primes', 'Number of numbers'])
    # write data
    writer.writerow([number_of_primes, counter])
