"""
This is code to examine time of flight.
We are going to used closed form equations to solve for
the range an object flies.
We are then going to try to make an optimization that
finds the best possible angle for launch to get the gratest distance.
We know the answer should be 45 degrees.
We want to see if we can make an optimization tool that finds that for us.

Here is a link to our starting equations:
https://courses.lumenlearning.com/boundless-physics/chapter/projectile-motion/#:~:text=The%20time%20of%20flight%20of%20an%20object%2C%20given%20the%20initial,2%20v%20i%20sin%20%E2%81%A1%20

and here is the equation for range:
Range = ( initial_velocity * initial_velocity * sin ( 2 * launch_angle ) ) / gravity

We will use an initial_velocity of 20 meters per second
We will use 9.807 meters per second squared for gravity
For a launch angle of 45 degrees, this should result in a distance of 40.79 meters.
For a launch angle of 44 or 46 degrees, this should result in a distance of 40.76 meters.
"""

import math

def print_greeting():
    print('hello, world.')

def calculate_range(launch_angle):
    initial_velocity = 20
    gravity = 9.807
    range = \
    initial_velocity * initial_velocity * \
    math.sin ( math.radians(2 * launch_angle)) \
    / gravity
    return range

if __name__ == '__main__':
    print_greeting()

    launch_angle = 45
    range = calculate_range(launch_angle)
    print("angle", launch_angle, "range", range, " meters")
