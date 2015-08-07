from constants import *
from utils import *

class DES():

  def __init__(self, key):
    self.key = permutate(key, PC1) 
    self.subkeys = self.gen_subkeys()

  def gen_subkeys(self):
    subkeys = self.build(self.key)
    for i in subkeys:
      subkeys[i] = permutate(subkeys[i], PC2)
    return subkeys

  def build(self, key, length=0, subkeys={}):
    next_key = self.build_subkey(key, length)
    subkeys[length] = next_key 

    if length == 15: return subkeys

    length += 1
    return self.build(next_key, length, subkeys)

  def build_subkey(self, prev_key, sequence):
    left, right = split(prev_key)
    schedule = ROTATION_SCHEDULE[sequence]
    return lshift(left, schedule) + lshift(right, schedule)

  def encrypt(self, message):
    m = permutate_ip(message, IP)
    left, right = split(m)
    for i in range(0, 15):
      left = prev_right
      right = prev_left + feistel(prev_right, key)
    message = right + left
    return permutate_ip(message, IP_INV)

  def feistel(self, left, right, n):
    r = permutate(right, EXPANSION)
    r = xor(r, self.subkeys[n])
    r = self.substitute(r)
    p = permutate_one_index(r, P) 
    return p

  def substitute(self, message):
    chunks = []
    for x in range(0, len(message), 6):
      chunk = message[x:x+6]
      chunks.append(chunk)

    m = ""
    for i in range(8):
      chunk = chunks[i]
      m += self.sbox(chunk, i)
    return m

  def sbox(self, block, n):
    row = int((block[0] + block[5]), 2)
    column = int(block[1:5], 2)
    m = SBOXES[n][row][column]
    return_val = str(bin(int(m))[2:])
    return return_val.zfill(4)


   
