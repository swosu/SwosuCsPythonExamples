tile_dict = { 'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4,
                'G': 2, 'H': 4, 'I': 1, 'J': 8,
                'K': 5, 'L': 1, 'M': 3, 'N': 1,
                'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
                'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 }


user_word = input("What word do you want to score?")

print('you entered', user_word)

total_score = 0

for letter in user_word:
    print(letter)
    letter_value = tile_dict[letter.upper()]
    print('letter value was: ', letter_value)
    total_score = total_score + letter_value

print('total score of ', user_word, ' was ', total_score)
