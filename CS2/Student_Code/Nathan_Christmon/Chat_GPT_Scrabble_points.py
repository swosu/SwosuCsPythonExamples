tile_dict = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
             'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
             'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

def calculate_base_value(word):
    total_value = 0
    for letter in word:
        if letter.upper() in tile_dict:
            total_value += tile_dict[letter.upper()]
    return total_value

# Prompt the user to enter a word
word = input("Enter a word: ")

# Calculate and print the base value of the word
base_value = calculate_base_value(word)
print(f"The base value of '{word}' is {base_value}")
