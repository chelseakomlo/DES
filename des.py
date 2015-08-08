from constants import *
from utils import *
from message_factory import MessageFactory

class DES():

  def __init__(self, key):
    key = permutate(key, PC1) 
    self.subkeys = self.gen_subkeys(key)

  def gen_subkeys(self, key, length=0, subkeys={}):
    next_key = self.build_subkey(key, length)
    subkeys[length] = permutate(next_key, PC2)

    if length == 15: return subkeys
    length += 1
    return self.gen_subkeys(next_key, length, subkeys)

  def build_subkey(self, prev_key, sequence):
    left, right = split(prev_key)
    schedule = ROTATION_SCHEDULE[sequence]
    return lshift(left, schedule) + lshift(right, schedule)

  def encrypt(self, message):
    m = permutate_one_index(message, IP)
    left, right = split(m)
    message = self.encode(left, right)
    return permutate_one_index(message, IP_INV)

  def encode(self, left, right, counter=0):
    next_left = right
    next_right = binary_add(left, self.feistel(right, counter))
    
    if counter == 0: return next_left + next_right
    return self.encode(next_left, next_right, counter+1)

  def feistel(self, right, n):
    message = ( MessageFactory(right)
                  .expand()
                  .xor(self.subkeys[n])
                  .substitute()
                  .p()
                  .get_message()
              )
    return message 

   
