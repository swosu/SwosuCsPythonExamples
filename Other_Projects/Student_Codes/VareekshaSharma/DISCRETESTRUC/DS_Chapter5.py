'''Write a program: Write a program that solves a problem iteratively, 
and then solve that same problem with recursion. Measure the number 
of steps taken to solve the problem each way. Please discuss the 
differences.'''

# recursive
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

n = int(input("Enter the number of disks: "))
TowerOfHanoi(n, 'A', 'C', 'B')

"""# iterative
def iterativeToH(n, from_rod, to_rod, aux_rod):
    total_moves = pow(2, n) - 1
    if total_moves % 3 == 1:
        print(f"move top disk from {from_rod} to {to_rod}")
    
    if total_moves % 3 == 2:
        print(f""))
"""
