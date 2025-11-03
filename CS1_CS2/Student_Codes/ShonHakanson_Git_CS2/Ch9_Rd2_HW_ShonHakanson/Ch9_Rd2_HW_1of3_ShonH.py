# Ch9_Rd2_HW_1of3, 9.14 Lab, Triangle Area Comparison

class Triangle:   
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height
   
    def get_area(self):
        area = 0.5 * self.base * self.height
        return area
   
    def print_info(self):
        print(f'Base: {self.base:.2f}')
        print(f'Height: {self.height:.2f}')
        print(f'Area: {self.get_area():.2f}')

if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()

    # TODO: Read and set base and height for triangle1 (use set_base() and set_height())
    triangle1.set_base(float(input("Enter base for triangle 1: ")))
    triangle1.set_height(float(input("Enter height for triangle 1: ")))
      
    # TODO: Read and set base and height for triangle2 (use set_base() and set_height())
    triangle2.set_base(float(input("Enter base for triangle 2: ")))
    triangle2.set_height(float(input("Enter height for triangle 2: ")))
      
    
    # TODO: Determine smaller triangle (use get_area())
    #       and output smaller triangle's info (use print_info())
    if triangle1.get_area() < triangle2.get_area():
        print('Triangle with smaller area is Triangle 1') 
        print('Triangle 1 info:')
        triangle1.print_info()
    elif triangle1.get_area() == triangle2.get_area():
        print('Both triangles have the same area')
        print('Triangle 1 info:')
        triangle1.print_info()
        print('Triangle 2 info:')
        triangle2.print_info()
    elif triangle1.get_area() > triangle2.get_area():
        print('Triangle with smaller area is Triangle 2') 
        print('Triangle 2 info:')
        triangle2.print_info()