def permutate_one_index(block, iterator):
  return "".join(str(x) for x in [block[x-1] for x in iterator])

def permutate(block, iterator):
  return "".join(str(x) for x in [block[x] for x in iterator])

def split(block):
  mid = len(block) // 2 
  return (block[:mid], block[mid:])

def lshift(block, schedule):
  if schedule == 0: return block
  first = block[0]
  block = block[1:] + first
  return lshift(block, schedule-1)

def xor(block1, block2):
  result = [ int(block1[x]) ^ int(block2[x]) for x in range(len(block1)) ]
  return "".join(str(x) for x in result)

