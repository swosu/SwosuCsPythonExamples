import random 

def gen_birthdays(people):
        birthdays = []
        for person in range(people):
            birthdays.append(random.randint(1,366))
        return birthdays

def sim(groups,sims = 2000):
    birthdays_list = []
    for i in range(groups):
         birthdays_list.append(gen_birthdays(people))

    matches = 0
    for i in range(sims):
        people_birthdays = gen_birthdays(people)
        if len(set(people_birthdays)) != len(people_birthdays):
            matches += 1

    return (f"for {people} people is {(matches/sims)*100:.2f}%")

if __name__ == '__main__':
    nums = [30,35,40,46,68]
    groups = 10
    print(f"The probablility of atleast two people having a matching birthday in a room:")
    for i in nums:
         people = i
         print(sim(groups))