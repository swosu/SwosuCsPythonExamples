class Triangle:
    
    def __init__(self):
        self.base = 0
        self.height = 0
        
    def set_base(self, user_input_base_length):
        self.base = user_input_base_length
        
    def set_height(self, user_input_side_height):
        self.height = user_input_side_height

    def get_area(self):
        return self.base * self.height / 2
    
    def print_info(self):
        print('Base:', self.base)
        print('Height:', self.height)
        print('Area:', self.get_area())


if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()
    
    triangle1_base = int(input('what is traingle 1 base length?'))
    triangle1_height = int(input('what is traingle 1 height?'))
    

    # TODO: Read and set base and height for triangle1 (use set_base() 
    # and set_height())
    triangle1.set_base(triangle1_base)
    triangle1.set_height(triangle1_height)
      
    # TODO: Read and set base and height for triangle2 (use set_base() and set_height())
    triangle2.set_base(int(input('what is traingle 2 base length?')))
    triangle2.set_height(int(input('what is traingle 2 side height?')))
      
    print('Triangle with smaller area:')  
    
    # TODO: Determine smaller triangle (use get_area())
    #       and output smaller triangle's info (use print_info())

    if triangle1.get_area() < triangle2.get_area():
        triangle1.print_info()

