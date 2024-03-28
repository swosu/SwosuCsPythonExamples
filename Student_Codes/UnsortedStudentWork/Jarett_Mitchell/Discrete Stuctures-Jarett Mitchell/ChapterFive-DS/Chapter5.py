#count iterative and recursive processess and how long they both take.
import time

#create a factiorial function
def recursive_factorial(n, cycles = 0):
    start = time.time()
    if n == 0:
        end = time.time()
        print(f"Number of cycles for recursive: {cycles}")
        print(f"Recursive factorial took: {end - start} seconds")
        return 1
    else:
        return n * recursive_factorial(n-1, cycles + 1)

#create a iterative factorial function
def iterative_factorial(n):
    start = time.time()
    result = 1
    cycles = 0
    for i in range(1, n+1):
        result = result * i
        cycles += 1
    end = time.time()
    print(f"Number of cycles for iterative: {cycles}")
    print(f"Iterative factorial took: {end - start} seconds")
    return result

#call the functions
print(recursive_factorial(950))
print(iterative_factorial(950))

#This is a demonstration of 995 breaking the recursive function
ansOne = (input("Do you want iterative to run with 995? (y/n): "))
if ansOne == "y":
    print(iterative_factorial(995))
ansTwo = (input("Do you want recursive to run with 995? (y/n): "))
if ansTwo == "y":
    print(recursive_factorial(995))
