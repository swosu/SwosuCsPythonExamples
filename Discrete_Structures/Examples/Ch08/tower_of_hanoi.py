# Recursive Python function to solve tower of hanoi 
class Step_counter:
    def __init__(self):
        self.steps = 0
    def add(self):
        self.steps += 1
    def get(self):
        return self.steps
  
  
def TowerOfHanoi(n, from_rod, to_rod, aux_rod, step_counter): 
    if n == 0: 
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod, step_counter) 
    
    step_counter.add()
    print('number of steps: ', step_counter.get(), end = '')
    print(" Move disk", n, "from rod", from_rod, "to rod", to_rod) 
    
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod, step_counter) 
  
  
# Driver code how many discs do you want to have 
N = int(input('how many discs would you like?'))
step_counter = Step_counter()
# A, C, B are the name of rods 
TowerOfHanoi(N, 'A', 'B', 'C', step_counter) 
  
# Contributed By Harshit Agrawal 