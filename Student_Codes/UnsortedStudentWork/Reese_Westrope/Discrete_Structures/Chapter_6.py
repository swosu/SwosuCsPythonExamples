import itertools

cookie_types = ['chocolate chip', 'snickerdoodle', 'peanut butter', 'sugar']

num_cookies = int(input('How many cookies would you like to take?\n:'))

combinations = list(itertools.combinations_with_replacement(cookie_types, num_cookies))

print(f"There are {len(combinations)} combinations of {num_cookies} cookies from {len(cookie_types)} types.")

for cookie in cookie_types:
    print(cookie)

bad_cookie = input("Choose a cookie that you don't want to include in any of the combinations\n:")

good_cookie = input("Choose a cookie that you want to include in every combination\n:")

bad_cookie_list = []
good_cookie_list = []

for combination in combinations:
    if bad_cookie in combination:
        bad_cookie_list.append(combination)

#print(bad_cookie_list)

for combination in combinations:
    if good_cookie not in combination:
        bad_cookie_list.append(combination)

#print(good_cookie_list)

for bad_cookie_group in bad_cookie_list:
    if bad_cookie_group in combinations:
        combinations.remove(bad_cookie_group)

for good_cookie_group in good_cookie_list:
    if good_cookie_group in combinations:
        combinations.remove(good_cookie_group)

print(f"There are {len(combinations)} combinations that meet your requirements.")
print(combinations)
