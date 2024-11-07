string_name = "-Hello, 1 world$!"

plain_string = ""
 
# Iterate over the string
for element in string_name:
    print(element, end = '')
    if element.isalpha():
        print(':  that was a character.')
        plain_string = plain_string + element
    else: 
        print(': that was not a character.')
        string_name = string_name.replace(element, '')
print("\n")

print(f'our cleaned up string is: {string_name}.')

print(f'doing an concat with empty string: {plain_string}.')