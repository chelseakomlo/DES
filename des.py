from utils import *

# The Feistel structure has the advantage that encryption and decryption operations are very similar, even identical in some cases, requiring only a reversal of the key schedule. 
class DES():

  def encrypt(message):
    # There is an initial permutation IP of the 64 bits of the message data M. 
    message = permutate(message, IP)

    # Next divide the permuted block IP into a left half L0 of 32 bits, and a right half R0 of 32 bits.
    right, left = split(message)

    # We now proceed through 16 iterations, for 1<=n<=16, using a function f which operates on two blocks--a data block of 32 bits and a key Kn of 48 bits--to produce a block of 32 bits.
    for i in range(0, 16):
      left_post = right
      right_post - left + f(right, subkeys[i]
      message = left + right
    
    return message

  def decrypt(message):
    pass

# accepts a block of 64 bits
  def permutate(block, interface):
    return list(map(lambda x: block[x], interface))

  def split(block):
    mid = len(block) / 2
    return (block[0:mid], block[mid:len(block))

  def xor(block, interface):
    pass

# To calculate f, we first expand each block Rn-1 from 32 bits to 48 bits. This is done by using a selection table that repeats some of the bits in Rn-1. 
# Next in the f calculation, we XOR the output E(Rn-1) with the key Kn
# To this point we have expanded Rn-1 from 32 bits to 48 bits, using the selection table, and XORed the result with the key Kn . We now have 48 bits, or eight groups of six bits. We now do something strange with each group of six bits: we use them as addresses in tables called "S boxes"
  def f(block):
    pass
