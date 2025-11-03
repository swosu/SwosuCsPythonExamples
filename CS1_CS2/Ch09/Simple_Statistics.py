# User inputs string w/ numbers
user_input = input('Enter your numbers seperated by a period. press enter when you are done')

tokens = user_input.split()  # Split into separate strings

# Convert strings to floats
input_data = []
index = 0
for token in tokens:
    print(f'our index is: {index}: Our token is: {token}')
    input_data.append(float(token))

# Get max and average
max_value = max(input_data)
average_value = sum(input_data) / len(input_data)

print(f'{max_value:.2f} {average_value:.2f}')