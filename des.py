from utils import *

# The Feistel structure has the advantage that encryption and decryption operations are very similar, even identical in some cases, requiring only a reversal of the key schedule. 
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
                 .mix(subkey)
                 .substitute()
                 .permutate()

class Block():
  
  def __init__(self, message):
    self.message = message

  def expand(self):
    # The 32-bit half-block is expanded to 48 bits using the expansion permutation by duplicating half of the bits. 
    # The output consists of eight 6-bit (8 * 6 = 48 bits) pieces, each containing a copy of 4 corresponding input bits, plus a copy of the immediately adjacent bit from each of the input pieces to either side.
    pass

  def mix(self, subkey):
    # the result is combined with a subkey using an XOR operation. 16 48-bit subkeys — one for each round — are derived from the main key using the key schedule.
    pass

  def substitute(self):
    # something to do with s-box subsitution
    pass

  def permutate(self):
  # the 32 outputs from the S-boxes are rearranged according to a fixed permutation, the P-box. This is designed so that, after permutation, each S-box's output bits are spread across 4 different S boxes in the next round.
    pass
