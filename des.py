from utils import *

class DES():

  def encrypt(message):
    message = permutate(message, IP)

    right, left = split(message)

    for i in range(0, 16):
      left_post = right
      right_post = left + f(Block(right), subkeys[i]
      message = left + right
    return message

  def decrypt(message):
    # similar to encryption, requires only a reversal of the key schedule. 
    message = permutate(message, FP)
    pass

  def permutate(block, interface):
    return list(map(lambda x: block[x], interface))

  def split(block):
    mid = len(block) / 2
    return (block[0:mid], block[mid:len(block))

  def xor(block, interface):
    pass

  # The F-function operates on half a block (32 bits) at a time and consists of four stages
  # 1. Expand each block from 32 bits to 48 bits
  # 2. XOR the output with key
  # 3. Use something to do with S box substitution
  # 4. Permutate according to P-Box
  def f(self, block, subkey):
    block = block.expand()
                 .xor(subkey)
                 .substitute()
                 .permutate()

class Block():
  
  def __init__(self, message):
    self.message = message

  def expand(self):
    return permutate(self.message, EXPANSION)

  def xor(self, subkey):
    return list(map(lambda x, y x ^ y, self.message, subkey)) 

  def substitute(self):
    chunks = [ self.message[x:x+6] for x in xrange(0, len(self.message), 6) ]

    # 2. blocks are subjected to a unique substitution function yielding a 4-bit block as output. 
      # a.  This is done by taking the first and last bits of the block to
      #     represent a 2-digit binary number (i) in the range of 0 to 3. 
      # b. The middle 4 of the block represent a 4-digit binary number in the range of 0 to 15. 
      # c.  The unique substitution number to use is the one in the ith row and jth column
      #     which is in the range of 0 to 15 and is represented by a 4-bit block.
   message = ""
   for i in range(0, 7):
    row = chunk[0] + chunk[5] 
    column = chunk[1:4]
    element = SBOXES[I][row][column]
    message += element
   return message

  def permutate(self):
  # the 32 outputs from the S-boxes are rearranged according to a fixed permutation, the P-box. This is designed so that, after permutation, each S-box's output bits are spread across 4 different S boxes in the next round.
    pass
