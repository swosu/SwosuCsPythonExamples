class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.area = 0

    def __str__(self):
        return 'Triangle base = ' + str(self.base) + ' height = ' + str(self.height) + ' area = ' + str(self.area)

    def area(self):
        self.area = 0.5 * self.base * self.height

# make a loop to read in a list of triangles from a user. 
# The user will enter the base and height of each triangle.
# The loop will end when the user enters a base of 0.



# make a loop to read in a list of triangles from a user.
print('Enter the base and height of each triangle.')
print(' The loop will end when the user enters a base or height of 0.')
list_of_triangle_objects = []
while True:
    print('new triangle entry: ')
    base_input = float(input("Enter the base of the triangle: "))
    if base_input == 0:
        break
    height_input = float(input("Enter the height of the triangle: "))
    if height_input == 0:
        break
    list_of_triangle_objects.append(Triangle(base_input, height_input))
    print('triangle added to list')

# print the list of triangles
print('The list of triangles is:')
for triangle in list_of_triangle_objects:
    print(triangle)
print()

# calculate the area for each triangle
print('The area of each triangle is:')
for triangle in list_of_triangle_objects:
    triangle.area()
    print(triangle)

# sort the triangle list by area
print('The list of triangles sorted by area is:')
list_of_triangle_objects.sort(key=lambda x: x.area)
for triangle in list_of_triangle_objects:
    print(triangle)
print()



