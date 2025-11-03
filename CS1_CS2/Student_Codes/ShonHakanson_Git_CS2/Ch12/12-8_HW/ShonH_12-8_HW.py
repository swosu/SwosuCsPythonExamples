file_name = input("Enter the file name: ")
lower_bound = input("Enter the lower bound: ")
upper_bound = input("Enter the upper bound: ")
opened_file = open(file_name, 'r')
text_lines = opened_file.readlines()
line_list = []
line_list = [line.strip() for line in text_lines]

print ("Lines between", lower_bound, "and", upper_bound, "are:")
for word in line_list:
    if lower_bound <= word <= upper_bound:
        print (f"{word} - in range")
    else:
        print (f"{word} - out of range")

opened_file.close()