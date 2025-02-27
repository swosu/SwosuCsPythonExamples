class QuickSortTracker:
    """
    A class to manage the sorting of user IDs using the Quicksort algorithm
    while tracking the number of recursive calls made.
    """
    def __init__(self):
        """
        Initializes the QuickSortTracker with a call counter and an empty list for user IDs.
        """
        self.number_of_quicksort_calls = 0
        self.user_ids = []

    def quicksort(self, ids_list, low_index, high_index):
        """
        Sorts the provided list in ascending order using the Quicksort algorithm.

        :param ids_list: List of integers to be sorted
        :param low_index: Starting index of the portion to sort
        :param high_index: Ending index of the portion to sort
        """
        if low_index < high_index:
            # Increment the counter for each quicksort call
            self.number_of_quicksort_calls += 1

            # Partition the list and get the pivot index
            pivot_index = self.partition(ids_list, low_index, high_index)

            # Recursively apply quicksort to the sublists
            self.quicksort(ids_list, low_index, pivot_index - 1)
            self.quicksort(ids_list, pivot_index + 1, high_index)

    def partition(self, ids_list, low_index, high_index):
        """
        Partitions the list around a pivot element such that elements less than the pivot
        appear on the left and elements greater than the pivot appear on the right.

        :param ids_list: List of integers to partition
        :param low_index: Starting index of the portion to partition
        :param high_index: Ending index of the portion to partition
        :return: The index of the pivot element
        """
        pivot = ids_list[high_index]  # Choose the last element as the pivot
        smaller_element_index = low_index - 1  # Pointer for the smaller element

        for current_index in range(low_index, high_index):
            if ids_list[current_index] < pivot:
                # Move the pointer for the smaller element
                smaller_element_index += 1

                # Swap ids_list[smaller_element_index] and ids_list[current_index]
                temp = ids_list[smaller_element_index]
                ids_list[smaller_element_index] = ids_list[current_index]
                ids_list[current_index] = temp

        # Place the pivot in the correct position
        temp = ids_list[smaller_element_index + 1]
        ids_list[smaller_element_index + 1] = ids_list[high_index]
        ids_list[high_index] = temp

        return smaller_element_index + 1

    def read_user_ids(self):
        """
        Reads user IDs until -1 is entered, then initializes the list for sorting.
        """
        print("Enter user IDs (end with -1):")
        while True:
            try:
                user_id = input()
                if user_id == '-1':
                    break
                self.user_ids.append(user_id)
            except ValueError:
                print("Please enter a valid integer.")

    def sort_and_display_results(self):
        """
        Sorts the collected user IDs using Quicksort and displays the results.
        """
        if not self.user_ids:
            print("No user IDs to sort.")
            return

        print("\nSorting user IDs...\n")
        self.quicksort(self.user_ids, 0, len(self.user_ids) - 1)

        print("Number of Quicksort calls:", self.number_of_quicksort_calls)
        print("Sorted User IDs:", " ".join(map(str, self.user_ids)))


if __name__ == "__main__":
    quicksort_tracker = QuickSortTracker()
    quicksort_tracker.read_user_ids()
    quicksort_tracker.sort_and_display_results()

