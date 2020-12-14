import re

f = open('input.txt')
ls = list(map(lambda s: s.strip(), f.readlines()))

def process_mask(mask_string):
  mask = {}
  for i in range(len(mask_string)):
    bit_index = len(mask_string) - i - 1
    char = mask_string[bit_index]
    if char == '0' or char == '1':
      mask[i] = int(char)
  return mask

def mask_value(value, mask):
  new_value = value
  for (bit_index, mask_value) in mask.items():
    if mask_value == 1:
      new_value |= 1 << bit_index
    elif mask_value == 0:
      new_value &= ~(1 << bit_index)
  return new_value

mask = None
mem = {}
for l in ls:
  if l.startswith('mask = '):
    mask = process_mask(l[7:])
  elif l.startswith('mem['):
    mem_loc = int(re.search(r'\[(\d*)\]', l).groups()[0])
    value = int(re.search(r'= (\d*)$', l).groups()[0])
    masked_value = mask_value(value, mask)
    mem[mem_loc] = masked_value
print(sum(mem.values()))