
user_input = input("Enter a list of numbers separated by spaces: ")


number_list = list(map(int, user_input.split()))


list_length = len(number_list)


for current_position in range(list_length - 1):
  
    index_of_largest = current_position

    
    for next_position in range(current_position + 1, list_length):
        
        if number_list[next_position] > number_list[index_of_largest]:
            index_of_largest = next_position

    
    number_list[current_position], number_list[index_of_largest] = (
        number_list[index_of_largest],
        number_list[current_position],
    )

   
    print(f"After iteration {current_position + 1}: {number_list}")

