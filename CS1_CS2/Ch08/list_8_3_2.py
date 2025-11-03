
user_input = input('Enter numbers seperated by a space and then press enter when you are done:')

tokens = user_input.split()  # Split into separate strings
print(tokens)
print(type(tokens))
print(type(tokens[0]))

# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number
print()  # Print a single newline
for index in range(len(nums)):
    value = nums[index]
    
    print(f'{index}: {value}')

# Determine maximum even number
max_num = None
for num in nums:
    if (max_num == None) and (num % 2 == 0):
        # First even number found
        max_num = num
    elif (max_num != None) and (num > max_num ) and (num % 2 == 0):
        # Larger even number found
        max_num = num

print(f'Max even #: {max_num}')