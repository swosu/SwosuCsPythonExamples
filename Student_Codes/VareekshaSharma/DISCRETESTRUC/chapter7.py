"""Determine the number of people needed to ensure that the probability 
at least two of them have the same day of the year as their birthday is 
at least 70%, at least 80%, at least 90%, at least 95%, and at least 99%. 
Write a program that convinces you this is correct."""
import random

def gen_bmonth(people):
    bmonth = []
    for num in range(people):
        bmonth.append(random.randint(1, 12))
    return bmonth

def check_for_12():
    had_12_bmonth = False
    while not had_12_bmonth:
        ppls_bmonth = gen_bmonth(people)
        for month in ppls_bmonth:
            if month == 12:
                had_12_bmonth = True
                break


if __name__ == "__main__":
    people = 10
    # for 6, its 77%; for 7 its 88%; for 8 its 95%; for 10 its 99%
    rooms_to_check = 200000
    check_for_12()

    repeats = 0
    no_repeats = 0

    for room in range(rooms_to_check):
        ppls_bmonth = gen_bmonth(people)
        # ppls_bmonth.sort()
        # print(ppls_bmonth)
        ppls_bmonth_wo_repeats = set(ppls_bmonth)

        if len(ppls_bmonth) == \
            len(ppls_bmonth_wo_repeats):
            no_repeats += 1
        else:
            repeats += 1

    print("repeats: ", repeats)
    print("no repeats: ", no_repeats)
    print(f"repeats / rooms_to_check: {(100 * (repeats / rooms_to_check)):.2f}%")
