from constants import *
from utils import *

class DES():

  def __init__(self, key):
    self.key = permutate(key, PC1) 

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

