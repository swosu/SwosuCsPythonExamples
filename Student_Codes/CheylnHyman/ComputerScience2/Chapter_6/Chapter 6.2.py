
list_size = 3
numbers = list()

def max_magnitude(number_list):
    higest_number = 0
    for number in number_list:
        if abs(number) > abs(higest_number):
            higest_number = number
    return higest_number

while len(numbers) < list_size:
    numbers.append(int(input("Please enter a number")))

print(max_magnitude(numbers))


