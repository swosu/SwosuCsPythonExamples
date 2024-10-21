import sys
import os

if len(sys.argv) != 2:
    
    print(f'Usage: {sys.argv[0]} input_file')
    sys.exit(1)  # 1 indicates error


print(f'Opening file {sys.argv[1]}.')

if not os.path.exists(sys.argv[1]):  # Make sure file exists
    print('File does not exist.')
    sys.exit(1)  # 1 indicates error

f = open(sys.argv[1], 'r')

# Input files should contain two integers on separate lines

print('Reading two integers.')
num1 = int(f.readline())
num2 = int(f.readline())


print(f'Closing file {sys.argv[1]}')
f.close()  # Done with the file, so close it


print(f'\nnum1: {num1}')

print(f'num2: {num2}')

print(f'num1 + num2: {num1 + num2}')