from itertools import combinations_with_replacement

if __name__ == '__main__':
    print("Hello, welcome to our donut picker")
    #https://www.geeksforgeeks.org/permutation-and-combination-in-python/
    # Get all combinations of [1, 2, 3] and length 2
    comb = combinations_with_replacement(['glazed', 'chocolate', 'maple'], 6)

    # Print the obtained combinations
    count = 0
    for i in list(comb):
        print (i)
        count += 1

    print(f'number of choices is: {count}.')

    """
    donuts = ['glazed', 'chocolate', 'maple']
    all_choices = []
    for selection in product(['glazed', 'chocolate', 'maple'], repeat = 2):
        print(selection)
        new_list = sorted(selection)
        print(f'our new list is: {new_list}.')
        all_choices.append(new_list)
    print(f'All choices:\n {all_choices}.')

    final_selection_set = set()
    for selection in all_choices:
        final_selection_set.update(selection)
        print(f'updated final selection: {final_selection_set}.')


    print(f'After pearing down, all choices:\n {final_selection_set}.')
    print(f'lenght of all choices after pearing is: {len(final_selection_set)}.')

    #print(f'previous selection:\n {previous_selection}.')
    #print(f'lenght of previous selection is: {len(previous_selection)}.')
    """

#stuff = [1, 2, 3]
#for L in range(0, len(stuff)+1):
#    for subset in itertools.combinations(stuff, L):
#        print(subset)
