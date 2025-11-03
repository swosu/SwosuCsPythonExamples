low_number = 20
high_number = 5
step_size = 5

print(f'You want to print from {low_number} to {high_number} by {step_size}.')

if low_number > high_number:
    print('Second integer can\'t be less than the first.')
else:
    our_number = low_number 
    while our_number <= high_number :
        print(f'{our_number} ', end = '')
        our_number += step_size
        
print('\nso long and thanks for all the fish.')