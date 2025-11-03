class SelectionSorter:
    """
    A class that provides a method to sort a list of integers in descending order 
    using the Selection Sort algorithm.
    """

    def __init__(self, input_list):
        """
        Initialize the sorter with the list of integers to be sorted.
        
        :param input_list: List of integers to sort
        """
        self.numbers_to_sort = input_list

    def sort_numbers_in_descending_order(self):
        """
        Sort the numbers in descending order using the selection sort algorithm.

        :return: List of integers sorted in descending order
        """
        for current_index in range(len(self.numbers_to_sort)):
            # Assume the first unsorted element is the largest
            largest_index = current_index
            
            # Compare it with the rest of the list
            for next_index in range(current_index + 1, len(self.numbers_to_sort)):
                if self.numbers_to_sort[next_index] > self.numbers_to_sort[largest_index]:
                    largest_index = next_index
            
            # Swap the largest element with the first unsorted element
            if largest_index != current_index:
                self.numbers_to_sort[current_index], self.numbers_to_sort[largest_index] = (
                    self.numbers_to_sort[largest_index],
                    self.numbers_to_sort[current_index],
                )
            print(self.numbers_to_sort)
        
        return self.numbers_to_sort


# Example usage:
if __name__ == "__main__":
    # Input list of integers
    numbers = [20, 10, 30, 40]
    
    # Create an instance of the sorter
    sorter = SelectionSorter(numbers)
    
    # Perform the sorting
    sorted_numbers = sorter.sort_numbers_in_descending_order()
    
    # Print the sorted list
    print("Sorted numbers in descending order:", sorted_numbers)
