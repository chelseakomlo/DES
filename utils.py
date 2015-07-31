
# initial permutation IP
# The Initial Permuation (IP) is a description of how a byte wide interface is connected 
# to a 64 bit block comprised of two 32 bit blocks (L and R). 
# Consider a byte wide interface with the bits numbered 1-8. 
# The event numbered bits go to the L Block and the odd numbered bits go to the R block. 
# Note that the bit order is big endian, where bit 1 is most significant and bit 8 is least 
# significant. The input block is typically loaded as 8 successive byte loads

IP = [ 57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7,
      56, 48, 40, 32, 24, 16, 8,  0,
      58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6
    ]

FP = [ 39,  7, 47, 15, 55, 23, 63, 31,
     38,  6, 46, 14, 54, 22, 62, 30,
     37,  5, 45, 13, 53, 21, 61, 29,
     36,  4, 44, 12, 52, 20, 60, 28,
     35,  3, 43, 11, 51, 19, 59, 27,
     34,  2, 42, 10, 50, 18, 58, 26,
     33,  1, 41,  9, 49, 17, 57, 25,
     32,  0, 40,  8, 48, 16, 56, 24
     ]

KEY = "12345" 
# 1. How to choose a key? 

# The key is and must be picked at random. You grab a bunch of bits from wherever, and hope that they are random enough to resist 
# attacks on the key generation algorithm.

# DES is a symmetric encryption algorithm, which means that to decrypt the data you must have the same key that was used to encrypt it. 


# 2. What is the proper key for this? 

# At the simplest level, the key is generated from a hashed version of a password. The key (ie the specific series of bits) must 
# be re-creatable otherwise you will not be able to decrypt the encrypted object.

# DES keys must either be 56 or 48 bits

# 3. How to generate sub keys for each permutation? 

# In cryptography, the so-called product ciphers are a certain kind of ciphers, where the (de-)ciphering of data is done in "rounds". 
# The general setup of each round is the same, except for some hard-coded parameters and a part of the cipher key, called a subkey. 
# A key schedule is an algorithm that, given the key, calculates the subkeys for these rounds.

# DES uses a key schedule where the 56 bit key is divided into two 28-bit halves; each half is thereafter treated separately. 
# In successive rounds, both halves are rotated left by one or two bits (specified for each round), and then 48 subkey bits are 
# selected by Permuted Choice 2 (PC-2) — 24 bits from the left half, and 24 from the right. The rotations mean that a different 
# set of bits is used in each subkey; each bit is used in approximately 14 out of the 16 subkeys.
