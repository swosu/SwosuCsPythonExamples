time_to_start = int(input('when do you want to start?'))
clock_direction = input('1 for after or 2 for before')
hours = int(input ('how many hours difference?'))

if '1' == clock_direction:
    print('going forward or after hours.')
    remainder_of_hours = hours % 12

    time = time_to_start
    for index in range (0, remainder_of_hours):
        time += 1
        if 13 == time:
            time = 1
    print(f'the clock reads {time}:00.')
else:
    print('going backwards or before hours.')
    remainder_of_hours = hours % 12

    time = time_to_start
    for index in range (0, remainder_of_hours):
        time -= 1
        if 1 == time:
            time = 13
    print(f'the clock reads {time}:00.')
