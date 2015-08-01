import random

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

CORE_KEY = bin(random.getrandbits(56)[2:])

PARITY = 0 if CORE_KEY.count('1') % 2 == 0 else 1

KEY = CORE_KEY + PARITY

def gen_subkeys():
  # this method will return a list of 16 subkeys from the initial key
  subkeys = []
  
  # need the key split into left and right sections. 
  left = CORE_KEY[0:(len(CORE_KEY)/2)]
  right = CORE_KEY[(len(CORE_KEY)/2) len(CORE_KEY)]

  # circular left shifts
  for i in range(16):
    subkeys[1] = shift(left, right) 


# In successive rounds, both halves are rotated left by one or two bits (specified for each round), and then 48 subkey bits are 
# selected by Permuted Choice 2 (PC-2) — 24 bits from the left half, and 24 from the right. The rotations mean that a different 
# set of bits is used in each subkey; each bit is used in approximately 14 out of the 16 subkeys.
