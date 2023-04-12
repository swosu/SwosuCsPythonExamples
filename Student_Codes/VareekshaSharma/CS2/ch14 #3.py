'''14.12 LAB: Output a linked list

Clone
Edit lab

Note
Write a recursive function called print_list() that outputs the 
integer value of each node in a linked list. Function print_list() 
has one parameter, the head node of a list. The main program reads 
the size of the linked list, followed by the values in the list. 
Assume the linked list has at least 1 node.

Ex: If the input of the program is:

5
1
2
3
4
5
the output of the print_list() function is:

1, 2, 3, 4, 5,
Hint: Output the value of the current node, then call the print_list() 
function repeatedly until the end of the list is reached. Refer to the 
Node class to explore any available instance methods that can be used 
for implementing the print_list() function.


Starter Code'''

class Node:
    def __init__(self, value):
        self.data_val = value
        self.next_node = None

    def insert_after(self, node):
        tmp_node = self.next_node
        self.next_node = node
        node.next_node = tmp_node

    def get_next(self):
        return self.next_node

    def print_data(self):
        print(self.data_val, end=", ")

# TODO: Write recursive print_list() function here.

        
if __name__ == "__main__":
    size = int(input())
    value = int(input())
    head_node = Node(value) # Make head node as the first node
    last_node = head_node
    
    # Insert the second and the rest of the nodes
    for n in range(1, size):
        value = int(input())
        new_node = Node(value)
        last_node.insert_after(new_node)
        last_node = new_node
    
    print_list(head_node)