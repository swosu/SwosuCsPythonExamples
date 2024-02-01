
def bitwiseAND(a,b):
    c = int(a,2) & int(b,2) # convert to int with base 2 and then do bitwise AND
    return bin(c)[2:] # returns binary representation of c with 0b removed, bin() returns a prefix 0b
def bitwiseOR(a,b):
    c = int(a,2) | int(b,2)
    return bin(c)[2:]
def bitwiseXOR(a,b):
    c = int(a,2) ^ int(b,2)
    return bin(c)[2:]
a = input("Enter the first bit string: ")
b = input("Enter the second bit string: ")
print("The bitwise AND of the two strings is: ",bitwiseAND(a,b))
print("The bitwise OR of the two strings is: ",bitwiseOR(a,b))
print("The bitwise XOR of the two strings is: ",bitwiseXOR(a,b))

# a test to make sure the bitwise operations work
print("The bitwise AND of 1010 and 1100 is: ",bitwiseAND("1010","1100"))
print("The bitwise OR of 1010 and 1100 is: ",bitwiseOR("1010","1100"))
print("The bitwise XOR of 1010 and 1100 is: ",bitwiseXOR("1010","1100"))





