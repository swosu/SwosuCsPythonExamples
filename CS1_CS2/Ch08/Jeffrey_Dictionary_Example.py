name_and_length_Dictonary = {}

while True:
    name = input("Please enter a name. Enter done if you want to quit.")

    if "done" == name:
        break

    number_of_letters_in_name = len(name)

    # add to our dictionary
    name_and_length_Dictonary[name] = number_of_letters_in_name

    # print off our current dictionary
    print(name_and_length_Dictonary)

print('thank you. Here is your final dictionary')

for key, value in name_and_length_Dictonary.items():
    print(key, value)


