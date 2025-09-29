section = 6
rows = 3
seats_per_row = 4
count = 0

for section in range(section):
    for row in range(rows):
        for seat in range(seats_per_row):
        
            count += 1

            # print off what the current row, seat, and count is
            print(f"Section: {section + 1}, Row: {row + 1}, Seat: {seat + 1}, Count: {count}")

print("Total people counted:", count)