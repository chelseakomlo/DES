from utils import *

class DES():

# expand to build a message, rather than one block of 64 bits
  def encrypt(message):
    message = permutate(message, IP)

    for i in range(16):
      left, right = split(message)
      right_post = feistel(right)
      left_post = xor(left, right_post)
      if i != 16:
        left, right = swap(left, right)
      message = left + right
    
    return permutate(message, FP)

  def decrypt(message):
    pass

# accepts a block of 64 bits
  def permutate(block, interface):
    return list(map(lambda x: block[x], interface))

  def split(block):
    mid = len(block) / 2
    return (block[0:mid], block[mid:len(block))

  def swap(left, right):
    return (right, left)

  def xor(block, interface):
    pass

# The Feistel structure has the advantage that encryption and decryption operations are very similar, even identical in some cases, requiring only a reversal of the key schedule. 
  def feistel(block):
    pass
