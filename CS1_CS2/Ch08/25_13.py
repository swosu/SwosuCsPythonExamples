# The words parameter is a list of strings.
def build_dictionary(words):
    # The frequencies dictionary will be built with your code below.
    # Each key is a word string and the corresponding value is an integer
    # indicating that word's frequency.

    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies

# The following code asks for input, splits the input into a word list,
# calls build_dictionary(), and displays the contents sorted by key.
if __name__ == '__main__':
    words = input('please paste in your input').split()
    your_dictionary = build_dictionary(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(key + ': ' + str(your_dictionary[key]))
