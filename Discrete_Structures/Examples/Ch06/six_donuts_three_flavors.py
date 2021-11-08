
# Function which returns subset or r length from n
from itertools import combinations
from itertools import combinations_with_replacement

def rSubset(arr, r):

    # return list of all subsets of length r
    # to deal with duplicate subsets use
    # set(list(combinations(arr, r)))
    return list(combinations(arr, r))

# Driver Function
if __name__ == "__main__":
    print('hello. This is example 1')
    arr = [1, 2, 3, 4]
    r = 2
    print (rSubset(arr, r))

    print('now for example 2')
    choices_for_each_donut = [1, 2, 3]
    donut_count = 6
    our_list = list(combinations_with_replacement('12345',2))
    print(our_list)
    donut_string = 'ABC'
    donut_list = list(combinations_with_replacement(donut_string, donut_count))
    for i in range(len(donut_list)):
        for x in donut_list:
            print(x[i], end =' ')
        print()
    print()
