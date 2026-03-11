"""
word_frequency.py

This program demonstrates several Python objects working together:

1. Path objects (directory inspection)
2. File objects
3. CSV reader objects
4. Dictionary objects

The program will:
1. Look in the current directory
2. Show available CSV files
3. Let the user choose one
4. Count word frequencies
"""

import csv
from pathlib import Path


class WordFrequencyAnalyzer:
    """
    Object responsible for analyzing word frequencies in a CSV file.
    """

    def __init__(self, filename):
        self.filename = filename
        self.word_counts = {}
        self.word_order = []

    def read_words(self):
        """
        Open the file and process words using csv.reader.
        """

        with open(self.filename, newline="") as file_object:

            print("\nFile object created:")
            print(type(file_object))

            reader = csv.reader(file_object)

            print("CSV reader object created:")
            print(type(reader), "\n")

            for row in reader:
                for word in row:
                    self._process_word(word)

    def _process_word(self, word):
        """
        Update the frequency table.
        """

        if word not in self.word_counts:
            self.word_counts[word] = 1
            self.word_order.append(word)
        else:
            self.word_counts[word] += 1

    def print_results(self):
        """
        Print word frequencies.
        """

        print("\nWord Frequencies\n")

        for word in self.word_order:
            print(f"{word} - {self.word_counts[word]}")


class FileExplorer:
    """
    Responsible for discovering CSV files in the directory.
    """

    def __init__(self):
        self.current_directory = Path(".")
        self.csv_files = []

    def discover_csv_files(self):
        """
        Find all CSV files in the current directory.
        """

        for file in self.current_directory.glob("*.csv"):
            self.csv_files.append(file)

    def display_files(self):
        """
        Show available files to the user.
        """

        print("\nCSV files found in this directory:\n")

        for i, file in enumerate(self.csv_files):
            print(f"{i+1}. {file.name}")

    def choose_file(self):
        """
        Ask the user to choose a file.
        """

        while True:
            try:
                choice = int(input("\nChoose a file number: "))
                return self.csv_files[choice - 1]
            except (ValueError, IndexError):
                print("Invalid selection. Try again.")


def main():

    explorer = FileExplorer()

    explorer.discover_csv_files()
    explorer.display_files()

    chosen_file = explorer.choose_file()

    analyzer = WordFrequencyAnalyzer(chosen_file)

    analyzer.read_words()
    analyzer.print_results()


if __name__ == "__main__":
    main()