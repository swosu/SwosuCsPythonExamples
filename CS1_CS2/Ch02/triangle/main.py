print('hello world.')
import perimeter

side_a_length = int(input('Please enter side a length.'))
side_b_length = int(input('Please enter side b length.'))
side_c_length = int(input('Please enter side c length.'))

temp_perimeter = side_a_length + side_b_length + side_c_length
print(f'temp_perimeter was {temp_perimeter}.')

s =perimeter.calc_perimeter(side_a_length, side_b_length, side_c_length)
print(f'from the module call, {s}')
