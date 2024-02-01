def calculate_scrabble_score(word):
    # Define a dictionary with letter scores
    letter_scores = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
        'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
        'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
    }

    # Convert the word to uppercase to handle all letters in uppercase
    word = word.upper()

    # Initialize the total score
    total_score = 0

    # Calculate the score for each letter in the word and sum them up
    for letter in word:
        if letter in letter_scores:
            total_score += letter_scores[letter]
        else:
            # Handle special characters or unsupported letters
            print(f"Ignore unsupported character: {letter}")

    return total_score

# Get a word from the user
user_word = input("Enter a word for Scrabble: ")

# Calculate the score for the user's word
score = calculate_scrabble_score(user_word)
print(f"The Scrabble score for '{user_word}' is: {score}")
