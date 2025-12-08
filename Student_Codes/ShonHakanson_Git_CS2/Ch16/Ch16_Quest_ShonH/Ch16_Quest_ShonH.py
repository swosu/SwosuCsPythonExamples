"""def read_words_from_file(filename):
    Reads a file and returns a list of all words in all lines.
    words = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            # Split on whitespace, basic cleaning
            for word in line.strip().split():
                words.append(word.lower())   # Make searches case-insensitive
    return words


def binary_search_all(sorted_list, key):
    
    Modified binary search.
    Returns a list of ALL indexes where 'key' appears.
    

    low = 0
    high = len(sorted_list) - 1
    found_index = -1

    # Standard binary search to find *one* match
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == key:
            found_index = mid
            break
        elif sorted_list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    if found_index == -1:
        return []   # No matches

    # Expand left to find other duplicates
    matches = [found_index]
    i = found_index - 1
    while i >= 0 and sorted_list[i] == key:
        matches.append(i)
        i -= 1

    # Expand right to find other duplicates
    i = found_index + 1
    while i < len(sorted_list) and sorted_list[i] == key:
        matches.append(i)
        i += 1

    return sorted(matches)  # Return indexes in order


def main():
    filename = "file_search.txt"
    words = read_words_from_file(filename)

    print(f"Loaded {len(words)} total words.")

    # Sorting is required for binary search
    words.sort()

    key = input("Enter a word to search for: ").lower()

    matches = binary_search_all(words, key)

    if not matches:
        print(f"'{key}' not found.")
    else:
        print(f"'{key}' found {len(matches)} times!")
        print("Indexes:", matches)


if __name__ == "__main__":
    main()
"""



def read_words_with_lines(filename):
    #Reads words from a file and returns a dictionary:
    #word -> list of line numbers where that word appears.


    word_locations = {}
    
    with open(filename, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            words = line.strip().split()
            for word in words:
                w = word.lower()
                if w not in word_locations:
                    word_locations[w] = []
                word_locations[w].append(line_number)
    
    return word_locations


def main():
    filename = "file_search.txt"
    word_locations = read_words_with_lines(filename)

    print("File loaded successfully!")
    print(f"Total unique words: {len(word_locations)}")

    key = input("Enter a word to search for: ").lower()

    if key not in word_locations:
        print(f"'{key}' not found.")
    else:
        lines = word_locations[key]
        print(f"'{key}' found {len(lines)} times on the following lines:")
        print(lines)


if __name__ == "__main__":
    main()