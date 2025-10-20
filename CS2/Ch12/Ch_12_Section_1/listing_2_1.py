# Example 1: Reading the entire contents of a file

print("Example 1: Reading the entire contents of a file")
# Open the file in read mode
myjournal = open("journal.txt")

print("File opened successfully.")
print("Reading the entire contents of the file...")
# Read the entire file into a single string
contents = myjournal.read()

print("File read successfully.")

print("Displaying the contents of the file:")

# Display what was read
print(contents)

# Close the file after use
myjournal.close()

print("thanka you")

