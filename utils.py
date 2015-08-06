
def permutate(block, iterator):
  return "".join(str(x) for x in [block[x] for x in iterator])

def split(block):
  mid = len(block) // 2 
  return (block[:mid], block[mid:])

def lshift(block, schedule):
  next_block = ""
  for i in range(0, schedule): 
    first = block[0]
    next_block = block[1:] + first
  return next_block
