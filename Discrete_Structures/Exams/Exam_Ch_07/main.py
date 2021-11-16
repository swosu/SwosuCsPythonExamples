print('hello.')

import random

random.seed()
# have a person have a birthday from 1 to 366


"""
for i in range(100000):
    my_birthday = random.randint(1,367)
    if(my_birthday == 366):
        print(my_birthday)
"""

my_birthday = random.randint(1,367)
print(my_birthday)
