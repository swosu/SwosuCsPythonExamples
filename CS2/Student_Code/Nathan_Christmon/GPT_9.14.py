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
      
    # TODO: Read and set base and height for triangle2 (use set_base() and set_height())
    
      
    print('Triangle with smaller area:')  
    
    # TODO: Determine smaller triangle (use get_area())
    #       and output smaller triangle's info (use print_info())

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

    # Read and set base and height for triangle1 (use set_base() and set_height())
    user_input = float(input('Enter base of triangle 1: '))
    triangle1.set_base(user_input)
    user_input = float(input('Enter height of triangle 1: '))
    triangle1.set_height(user_input)

    # Read and set base and height for triangle2 (use set_base() and set_height())
    user_input = float(input('Enter base of triangle 2: '))
    triangle2.set_base(user_input)
    user_input = float(input('Enter height of triangle 2: '))
    triangle2.set_height(user_input)
    
      
    print('Triangle with smaller area:')  
    
    # Determine smaller triangle (use get_area())
    #       and output smaller triangle's info (use print_info())
    if triangle1.get_area() < triangle2.get_area():
        triangle1.print_info()
    else:
        triangle2.print_info()
        