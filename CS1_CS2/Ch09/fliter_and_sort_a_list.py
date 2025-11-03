# User inputs string w/ numbers
user_input = input()

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
input_data = []
for token in tokens:
    if int(token) < 0:
        input_data.append(int(token))

# Sort strings to integers
input_data.sort(reverse=True)

for values in input_data:
    print(values, end=' ')