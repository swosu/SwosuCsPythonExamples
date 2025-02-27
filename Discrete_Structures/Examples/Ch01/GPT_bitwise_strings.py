num1 = int(input("Enter first number as an integer: "))
num2 = int(input("Enter second number as an integer: "))

# Convert to binary and remove '0b'
bin1 = bin(num1)[2:]
bin2 = bin(num2)[2:]

# Step 2: Ensure both strings are of equal length
n = max(len(bin1), len(bin2))
bin1 = bin1.zfill(n)
bin2 = bin2.zfill(n)

# Step 3: Perform bitwise operations
and_result = ''.join('1' if bin1[i] == '1' and bin2[i] == '1' else '0' for i in range(n))
or_result = ''.join('1' if bin1[i] == '1' or bin2[i] == '1' else '0' for i in range(n))
xor_result = ''.join('1' if bin1[i] != bin2[i] else '0' for i in range(n))

# Display results
print("Number 1 (binary):", bin1)
print("Number 2 (binary):", bin2)
print("Bitwise AND:", and_result)
print("Bitwise OR: ", or_result)
print("Bitwise XOR:", xor_result)
