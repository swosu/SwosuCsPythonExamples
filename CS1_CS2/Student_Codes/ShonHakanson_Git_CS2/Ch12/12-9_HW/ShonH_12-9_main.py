import csv   # 1️⃣ Import the CSV module for reading comma-separated files

# 2️⃣ Ask the user for the input filename
file_name = input("Enter the CSV file name: ")

# 3️⃣ Open the file safely using 'with' (it closes automatically)
try:
    with open(file_name, 'r') as csv_file:
        # 4️⃣ Create a CSV reader object
        csv_reader = csv.reader(csv_file)
        
        # 5️⃣ Prepare a structure to store word counts
        # (maybe a dictionary later)
        word_counts = []

        # 6️⃣ Loop through each row in the CSV file
        for row in csv_reader:
            # Each 'row' is a list of words separated by commas
            for word in row:
            # You’ll process each word here
                word_counts.append(word.strip().lower())  # Store words in lowercase for uniformity

    # 7️⃣ After reading, display the results
    # (e.g., print each word and its count)
    for word in sorted(set(word_counts)):
        print(f"{word}: {word_counts.count(word)}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")


