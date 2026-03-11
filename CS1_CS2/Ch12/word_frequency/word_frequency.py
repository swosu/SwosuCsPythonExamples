"""
word_frequency.py

This program demonstrates a pipeline of objects:

FileExplorer  → finds CSV files
CSVReader     → opens and reads CSV rows
WordExtractor → extracts individual words
FrequencyAnalyzer → counts word frequencies

Each object does ONE job.
"""

import csv
from pathlib import Path


class CSVFileReader:
    """
    Responsible only for opening a CSV file
    and returning the rows inside it.
    """

    def __init__(self, filename):
        self.filename = filename

    def read_csv_file(self):
        """
        Opens the CSV file and returns rows.

        We try UTF-8 first, then fall back to UTF-16
        because some Windows tools save CSV files that way.
        """

        rows = []

        try:
            file_object = open(self.filename, newline="", encoding="utf-8")
        except UnicodeDecodeError:
            file_object = open(self.filename, newline="", encoding="utf-16")

        with file_object:

            print("\nFile object created:")
            print(type(file_object))

            reader = csv.reader(file_object)

            print("CSV reader object created:")
            print(type(reader))

            for row in reader:
                rows.append(row)

        return rows


class WordExtractor:
    """
    Responsible for extracting words from rows.
    """

    def extract_words(self, rows):

        words = []

        for row in rows:
            for word in row:
                words.append(word)

        return words


class WordFrequencyAnalyzer:
    """
    Responsible for counting word frequencies.
    """

    def __init__(self):
        self.word_counts = {}
        self.word_order = []

    def process_words(self, words):

        for word in words:

            if word not in self.word_counts:

                self.word_counts[word] = 1
                self.word_order.append(word)

            else:
                self.word_counts[word] += 1

    def print_results(self):

        print("\nWord Frequencies\n")

        for word in self.word_order:
            print(f"{word} - {self.word_counts[word]}")


class FileExplorer:
    """
    Finds CSV files in the current directory.
    """

    def discover_csv_files(self):

        directory = Path(".")
        return list(directory.glob("*.csv"))

    def choose_file(self, files):

        print("\nCSV files available:\n")

        for i, file in enumerate(files):
            print(f"{i+1}. {file.name}")

        while True:

            try:
                choice = int(input("\nSelect file number: "))
                return files[choice - 1]

            except (ValueError, IndexError):
                print("Invalid choice. Try again.")


def main():

    # discover files
    explorer = FileExplorer()
    files = explorer.discover_csv_files()

    chosen_file = explorer.choose_file(files)

    # read CSV
    reader = CSVFileReader(chosen_file)
    rows = reader.read_csv_file()

    # extract words
    extractor = WordExtractor()
    words = extractor.extract_words(rows)

    # analyze frequencies
    analyzer = WordFrequencyAnalyzer()
    analyzer.process_words(words)

    # print results
    analyzer.print_results()


if __name__ == "__main__":
    main()