# Step 1: Create a dictionary of dictionaries to build the thesaurus
thesaurus = {}

# Step 2: Use files to keep track of the synonyms for individual words
# In each word file, there should be a number of different words with a similar meaning.
def load_synonyms(word):
    try:
        with open(f"{word}.txt", 'r') as f:
            synonyms = f.read().splitlines()
        return synonyms
    except FileNotFoundError:
        return None

# Step 3: Load synonyms into the thesaurus
def load_thesaurus(word):
    synonyms = load_synonyms(word)
    if synonyms is not None:
        thesaurus[word] = synonyms

# Step 4: Export the final dictionaries into a json file
import json
def export_thesaurus():
    with open('thesaurus.json', 'w') as f:
        json.dump(thesaurus, f)

# Step 5: Interactive function to use the thesaurus
def use_thesaurus():
    while True:
        word = input("Enter a word: ")
        letter = input("Enter a letter: ")
        load_thesaurus(word)
        if word in thesaurus:
            synonyms = [syn for syn in thesaurus[word] if syn.startswith(letter)]
            if synonyms:
                print(f"Synonyms for {word} starting with {letter}: {', '.join(synonyms)}")
            else:
                print(f"No synonyms for {word} starting with {letter} found in the thesaurus.")
        else:
            print(f"{word} not found in the thesaurus. Would you like to add synonyms from the internet? (y/n)")
        if input("Would you like to quit? (y/n)") == 'y':
            break

# Step 6: Unit tests
import unittest
class TestThesaurus(unittest.TestCase):
    def test_load_synonyms(self):
        # Test that synonyms are being loaded correctly
        synonyms = load_synonyms('happy')
        self.assertIsInstance(synonyms, list)
        self.assertTrue('joyful' in synonyms)

    def test_export_thesaurus(self):
        # Test that thesaurus is exported to a json file correctly
        load_thesaurus('happy')
        export_thesaurus()
        with open('thesaurus.json', 'r') as f:
            exported = json.load(f)
        self.assertEqual(exported, thesaurus)

# Run the unit tests
if __name__ == '__main__':
    unittest.main()