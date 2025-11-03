# write to a CSV file
#left column should be 1 to 10.
#2nd column should be square of the first column
#3rd column should be cube of the first column

import csv

with open('test.csv', 'w') as csvfile:
    fieldnames = ['number', 'square', 'cube']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)


    writer.writeheader()
    for i in range(11,21):
        writer.writerow({'number': i, 'square': i**2, 'cube': i**3})


print("Done with initial write.")

# print the status of the file, if it is open or closed
print('if closed, should be true, else open if false. ', csvfile.closed)