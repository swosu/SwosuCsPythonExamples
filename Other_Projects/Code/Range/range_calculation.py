print("Hello, World.")
import math

"""
We are going to calculate range.
"""

initial_velocity = 20
angle_in_degrees = 44
gravity_m_per_sec = 9.807

print('our initial velocity', initial_velocity)
print('angle in degrees', angle_in_degrees)
print('gravity in meters per second', gravity_m_per_sec)

range = 0
range = initial_velocity * initial_velocity *\
 math.sin(math.radians(2 * angle_in_degrees)) / gravity_m_per_sec

print('range', range)
