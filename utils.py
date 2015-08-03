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

PC1 = [ 56, 48, 40, 32, 24, 16, 8,
      0, 57, 49, 41, 33, 25, 17,
      9, 1, 58, 50, 42, 34, 26,
      18, 10, 2, 59, 51, 43, 35,
      62, 54, 46, 38, 30, 22, 14,
      6, 61, 53, 45, 37, 29, 21,
      13, 5, 60, 52, 44, 36, 28,
      20, 12, 4, 27, 19, 11, 3
    ]

PC2 = [                                                                                       
    13, 16, 10, 23, 0, 4,                                                                      
    2, 27, 14, 5, 20, 9,                                                                       
    22, 18, 11, 3, 25, 7,                                                                      
    15, 6, 26, 19, 12, 1,                                                                      
    40, 51, 30, 36, 46, 54,                                                                      
    29, 39, 50, 44, 32, 47,                                                                      
    43, 48, 38, 55, 33, 52,                                                                      
    45, 41, 49, 35, 28, 31                                                                       
    ]

ROTATION_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def build_key():
  hex_k = "FFFFFFFFFFFFFC"
  k = bin(int(hex_k, 16))[2:]
  return _with_parity(k)

def _with_parity(key):
  final_key = ""
  while len(key) != 0:
    block = key[0:7]
    parity = 0 if (block.count('1') % 2 == 0) else 1
    final_key += block + str(parity)
    key = key[7:]
  return final_key

def gen_subkeys(key):
  subkeys = {}
  left = key[0:(len(key)/2)]
  right = key[(len(key)/2):len(KEY)]

  for i in range(0, 16):
    rotation = ROTATION_SCHEDULE[i]
    subkey = lshift(left, rotation) + lshift(right, rotation)
    subkeys[i] = permutate(subkey, PC2) 
  return subkeys

def lshift(block, rotation=1):
  for i in range(rotation):
    last = block[-1]
    block = last + block[:-1]
  return block
  
def permutate(block, interface):
  return list(map(lambda x: block[x], interface))
 
KEY = build_key()
key = "".join(permutate(KEY, PC1))
gen_subkeys(key)
