import random

from Parrot_Class_File import Parrot

from Beta_Fish_Class_File import Fish

if __name__ == '__main__':
    print('hello')

    # instantiate the Parrot class
    blu = Parrot("Blu", 10)
    woo = Parrot("Woo", 15)

    rp = Parrot("Red", 20)
    sp = Parrot("Fido", 20)

    sp.set_average_speed(random.randint(1,sp.age))
    print(f"Sarah's bird can fly {sp.get_average_speed()} miles per hour right now.")

    rp.set_average_speed(random.randint(1,rp.age))
    print(f"Rooney's bird can fly {rp.get_average_speed()} miles per hour right now.")

    race_distance = 100
    keep_going = True

    while(keep_going):
        # find speed for this leg
        rp.set_average_speed(random.randint(1,rp.age))
        sp.set_average_speed(random.randint(1,sp.age))

        print(f'{rp.name} and fly {rp.get_average_speed()}')
        print(f'{sp.name} and fly {sp.get_average_speed()}')

        # add that time of flight times speed to the distance_covered
        rp.add_to_distance(rp.get_average_speed())
        sp.add_to_distance(sp.get_average_speed())

        print(f'\n{rp.name} has covered {rp.get_distance()}')
        print(f'{sp.name} has covered {sp.get_distance()}')

        if rp.get_distance() > race_distance or sp.get_distance() > race_distance:
            keep_going = False

    if rp.get_distance() > sp.get_distance():
        print(f"{rp.name} is the winner!")
    else:
        print(f"{sp.name} is the winner!")



    # access the class attributes
    #print("Blu is a {}".format(blu.__class__.species))
    #print("Woo is also a {}".format(woo.__class__.species))
    #print(f"{rp.name} is a {woo.__class__.species}.")

    # access the instance attributes
    #print("{} is {} years old".format( blu.name, blu.age))
    #print("{} is {} years old".format( woo.name, woo.age))
    #print("{} is {} years old".format( rp.name, rp.age))
