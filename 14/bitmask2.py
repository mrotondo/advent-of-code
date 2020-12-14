import re

f = open('input.txt')
ls = list(map(lambda s: s.strip(), f.readlines()))

def process_mask(mask_string):
  return mask_string[::-1]

def process_int(value):
  reversed_binary = '{0:b}'.format(value)[::-1]
  reversed_binary += '0' * (36 - len(reversed_binary))
  return reversed_binary

def mask_int(value, mask):
  masked_value = value
  for i in range(len(mask)):
    mask_char = mask[i]
    if mask_char == '1' or mask_char == 'X':
      masked_value = masked_value[:i] + mask_char + masked_value[i+1:]
  return masked_value

def resolve_masked_value(masked_value):
  if masked_value.count('X') == 0:
    return [masked_value]
  x_index = masked_value.index('X')
  zero_replacement_values = resolve_masked_value(masked_value[:x_index] + '0' + masked_value[x_index + 1:])
  one_replacement_values = resolve_masked_value(masked_value[:x_index] + '1' + masked_value[x_index + 1:])
  return zero_replacement_values + one_replacement_values

mask = None
mem = {}
for l in ls:
  if l.startswith('mask = '):
    mask = process_mask(l[7:])
  elif l.startswith('mem['):
    mem_loc = process_int(int(re.search(r'\[(\d*)\]', l).groups()[0]))
    value = int(re.search(r'= (\d*)$', l).groups()[0])

    masked_mem_loc = mask_int(mem_loc, mask)
    for generated_mem_loc in resolve_masked_value(masked_mem_loc):
      mem[generated_mem_loc] = value
print(sum(mem.values()))