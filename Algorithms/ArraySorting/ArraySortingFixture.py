import random
import time

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

print('Hello, World!')

array_size = 10
initial_array = []
bubble_sort_array = []
python_sort_array = []
lower_limit = 0
upper_limit = array_size*100

for index in range (0,array_size):
    initial_array.append(random.randint(lower_limit, upper_limit))
    bubble_sort_array.append(initial_array[index])
    python_sort_array.append(initial_array[index])

if(array_size < 20):
    print(initial_array)
    print('bubble sort array')
    print(bubble_sort_array)
    print('python sort array')
    print(python_sort_array)
else:
    print('array was bigger than 20 numbers')

bubble_sort_start_time = time.perf_counter()
bubbleSort(bubble_sort_array)
bubble_sort_stop_time = time.perf_counter()
bubble_sort_elapsed_time = bubble_sort_stop_time - bubble_sort_start_time
print('bubble sort elapse time', bubble_sort_elapsed_time)

if(array_size < 20):
    print('bubble sort array')
    print(bubble_sort_array)
else:
    print('array was bigger than 20 numbers')
