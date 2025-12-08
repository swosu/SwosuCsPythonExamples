# Global variable to count function calls
num_calls = 0

def partition(user_ids, i, k):
    mid = (i + k) // 2
    pivot = user_ids[mid]
    l = i
    h = k

    while True:
        # Move l right until value >= pivot
        while user_ids[l] < pivot:
            l += 1
        # Move h left until value <= pivot
        while user_ids[h] > pivot:
            h -= 1

        # If pointers cross, partition is done
        if l >= h:
            return h

        # Swap out-of-place values
        user_ids[l], user_ids[h] = user_ids[h], user_ids[l]
        l += 1
        h -= 1


def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1  # Count how many times quicksort() is called

    if i >= k:
        return  # Base case: list of 1 or 0 elements

    # Partition and get split point
    j = partition(user_ids, i, k)

    # Recursively sort both halves
    quicksort(user_ids, i, j)
    quicksort(user_ids, j + 1, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids, 0, len(user_ids) - 1)

    print(num_calls)
    for user_id in user_ids:
        print(user_id)
