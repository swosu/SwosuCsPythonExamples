# write a scoring program for the game of scrabble

# create a dictionary of letters and their values
# create a function that takes a word and returns the score
# create a function that takes a word and returns the highest scoring word

letter_scores = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
        'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
        'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
    }


def score_word(word):
    score = 0
    for letter in word.upper():
        if letter in letter_scores:
            score += letter_scores[letter]
        else:
            print(f"Letter {letter} not found in letter_scores dictionary.")
    return score

if __name__ == '__main__':
    word = input("Please enter a word: ")
    print(score_word(word))