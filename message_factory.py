from constants import *
from utils import *

class MessageFactory():

  def __init__(self, message):
    self.message = message

  def xor(self, key):
    result = [ int(self.message[x]) ^ int(key[x]) for x in range(len(self.message)) ]
    self.message = "".join(str(x) for x in result)
    return self

  def substitute(self):
    chunks = [self.message[x:x+6] for x in range(0, len(self.message), 6)]

    m = ""
    for i in range(8):
      m += self.sbox(chunks[i], i)
    self.message = m
    return self

  def sbox(self, block, n):
    row = int((block[0] + block[5]), 2)
    column = int(block[1:5], 2)
    m = SBOXES[n][row][column]
    return_val = str(bin(int(m))[2:])
    return return_val.zfill(4)

  def expand(self):
    self.message = permutate(self.message, EXPANSION)
    return self

  def p(self):
    self.message = permutate_one_index(self.message, P)
    return self

  def get_message(self):
    return self.message
