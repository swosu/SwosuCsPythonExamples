our_initial_string = 'hello'
print(our_initial_string)

# convert each letter in our string to an ASCII value in a list

# create an empty list to hold the ASCII values
list_of_decimal_values_for_each_letter = []

# loop through each letter in our string
for letter in our_initial_string:

    # convert the letter to an ASCII value and append it to the list
    letter_as_a_decimal = ord(letter)
    print('our letter was:', letter, 'and its ASCII value is:', letter_as_a_decimal)
    list_of_decimal_values_for_each_letter.append(letter_as_a_decimal)

# print the list of ASCII values

print('our string was: ', our_initial_string)

print('our list of ASCII values is:', list_of_decimal_values_for_each_letter)

# convert each value in the list to a binary value
list_of_binary_values_for_each_letter = []
for item in list_of_decimal_values_for_each_letter:

    print('our decimal value was:', item, 'and its binary value is:', bin(item))
    list_of_binary_values_for_each_letter.append(bin(item))

print('our list of binary values is:', list_of_binary_values_for_each_letter)

# now convert each lettter to hex
list_of_hex_values_for_each_letter = []
for item in list_of_decimal_values_for_each_letter:

    print('our decimal value was:', item, 'and its hex value is:', hex(item))
    list_of_hex_values_for_each_letter.append(hex(item))

print('our list of hex values is:', list_of_hex_values_for_each_letter)