seats = [1, 0, 1, 1, 0, 1]  # 1 = occupied, 0 = empty
count = 0

for seat in seats:
    if 1 == seat:
        count += 1

print("People actually in stadium:", count)
