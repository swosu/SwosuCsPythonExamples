import hashlib
import struct
import random

'''
When should I get a collision?

P(c) = 1 - (N! / ((N - c)! * N^c))
c = Two messages with the same hash
N = number of possible hashes

#Number of possible hashes for SHA-1 = 2^160

50% Chance of collision:
0.5 = 1 - (2^160! / ((2^160 - c)! * 2^160^c))

Solve for c:
c is about equal to 2^80

You would need to make a total of:

1,208,925,819,614,629,174,706,176

hashes to have a 50% chance of collision

'''


# Define the prefixes and suffux for the message
prefix = b"birthday"
suffix = b"attack"
hashDatabase = {}
loadingProgress = 0

# Generate random messages until we find a collision
while True:
    variation = random.randint(0, 2**64)
    password = prefix + struct.pack("<Q", variation) + suffix
    
    sha_hash = hashlib.sha1(password).hexdigest()

    if sha_hash not in hashDatabase:
        hashDatabase[sha_hash] = password
    else:
        print(f"Collision found for passwords! \nPassword 1: {password} \nPassword 2: {hashDatabase[sha_hash]}")
        print(f"Hash value for password 1: {hashlib.sha1(password).hexdigest()}")
        print(f"Hash value for password 2: {hashlib.sha1(hashDatabase[sha_hash]).hexdigest()}")
        break
    
    # Create a forced collision
    if loadingProgress == 2_000_000:
        if sha_hash not in hashDatabase:
            hashDatabase[sha_hash] = password
        else:
            print(f"Collision found for passwords! \nPassword 1: {password} \nPassword 2: {hashDatabase[sha_hash]}")
            print(f"Hash value for password 1: {hashlib.sha1(password).hexdigest()}")
            print(f"Hash value for password 2: {hashlib.sha1(hashDatabase[sha_hash]).hexdigest()}")
            break

    # Update the loading bar
    loadingProgress += 1
    if loadingProgress % 100_000 == 0:
        print(f"Progress: {loadingProgress} hashes computed")
