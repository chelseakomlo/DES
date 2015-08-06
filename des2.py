from utils import *

class DES():

  def encrypt(self, m):
    message = permutate(m, IP)
    right, left = self.split(message)

    left_post = "".join(str(x) for x in left)
    right_post = "".join(str(x) for x in right)
    for i in range(0, 16):
      left_zero = left_post
      left_post = right_post 
      right_post = bin(int(left_zero) + int(self.f(Block(right_post), subkeys[i+1])))[2:]
    return bin(int(left_post) + int(right_post))

  def decrypt(self, message):
    #requires reversal of the key schedule. 
    #TODO
    message = permutate(message, FP)
    pass

  def split(self, block):
    mid = len(block) / 2
    return (block[0:mid], block[mid:len(block)])

  def xor(self, block, interface):
    pass

  def f(self, block, subkey):
    block = ( block.expand()
                 .xor(subkey)
                 .substitute()
                 .permutate()
            )
    return block.message

class Block():
  
  def __init__(self, message):
    self.message = message

  def expand(self):
    self.message = permutate(self.message, EXPANSION)
    return self

  def xor(self, subkey):
    message = list(map(lambda x, y: int(x) ^ int(y), self.message, subkey)) 
    self.message = "".join(str(x) for x in message)
    return self

  def substitute(self):
    chunks = []
    for x in range(0, len(self.message), 6):
      chunk = self.message[x:x+6]
      chunks.append(chunk)

    m = ""
    for i in range(0, 8):
      chunk = chunks[i]
      row = int((chunk[0] + chunk[5]), 2)
      column = int(chunk[1:5], 2)
      element = SBOXES[i][row][column]
      m += str(element)
    self.message = bin(int(m))[2:]
    return self

  def permutate(self):
    print len(self.message)
    self.message = "".join(str(x) for x in permutate(self.message, P))
    return self

subkeys = build_key_and_subkeys()
message = " 0000000100100011010001010110011110001001101010111100110111101111"
print DES().encrypt(message)
