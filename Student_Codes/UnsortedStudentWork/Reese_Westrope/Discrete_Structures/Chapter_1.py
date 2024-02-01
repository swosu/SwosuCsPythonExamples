

aa = int(input("Enter the integer you want 'a' to represent:"))
bb = int(input("Enter the integer you want 'b' to represent:"))
 
# Print bitwise AND operation
print("a & b =", aa & bb)
 
# Print bitwise OR operation
print("a | b =", aa | bb)
 
# print bitwise XOR operation
print("a ^ b =", aa ^ bb)

def decimal_to_binary_list(n):
        result = [int(x) for x in list('{0:04b}'.format(n))]
        return result


if __name__ == "__main__":

    #converting integers to binary
    
    a = int(input("Enter an integer\n:"))
    b = int(input("Enter another integer\n:"))

    print(f"{a} in binary form is {'{0:04b}'.format(a)}.")
    print(f"{b} in binary form is {'{0:04b}'.format(b)}.")

    ListA = decimal_to_binary_list(a)
    ListB = decimal_to_binary_list(b)

    ListC = []

#creating an AND operator from scratch
    if ListA[0] == 1 and ListB[0] == 1:
        ListC.insert(0,'1')
    else:
        ListC.insert(0,'0')

    if ListA[1] == 1 and ListB[1] == 1:
        ListC.insert(1,'1')
    else:
        ListC.insert(1,'0')

    if ListA[2] == 1 and ListB[2] == 1:
        ListC.insert(2,'1')
    else:
        ListC.insert(2,'0')

    if ListA[3] == 1 and ListB[3] == 1:
        ListC.insert(3,'1')
    else:
        ListC.insert(3,'0')

    print(f'{a} AND {b} is {"".join(str(i) for i in ListC)}')
    

    