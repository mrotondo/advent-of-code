import re
import itertools

def get_mapped_value(from_type, to_type, from_value, maps, forward=True):
  ranges = maps[(from_type, to_type)]
  for (dst_start, src_start, range_length) in ranges:
    if forward:
      if from_value in range(src_start, src_start + range_length):
        return dst_start + from_value - src_start
    else:
      if from_value in range(dst_start, dst_start + range_length):
        return src_start + from_value - dst_start
  return from_value

f = open('input.txt')

seed_line = f.readline()
seeds = list(map(int, re.findall(r'\d+', seed_line)))

from_to = {}
to_from = {}
maps = {}
lines = f.readlines()
current_map = None
for line in lines:
  map_type_match = re.search(r'([a-z]+)-to-([a-z]+)', line)
  map_values_match = re.search(r'(\d+) (\d+) (\d+)', line)
  if map_type_match:
    (map_from, map_to) = map_type_match.groups()
    current_map = []
    maps[(map_from, map_to)] = current_map
    from_to[map_from] = map_to
    to_from[map_to] = map_from
  elif map_values_match:
    (dst_start, src_start, range_length) = list(map(int, map_values_match.groups()))
    current_map.append((dst_start, src_start, range_length))

locations = []
for seed in seeds:
  from_type = 'seed'
  from_value = seed
  while from_type != 'location':
    to_type = from_to[from_type]
    from_value = get_mapped_value(from_type, to_type, from_value, maps)
    from_type = to_type
  locations.append(from_value)

print(min(locations))

seed_ranges = [range(a, a + b) for (a, b) in zip(seeds[::2], seeds[1::2])]
for location in itertools.count(start=0, step=1):
  print('trying location {}'.format(location))
  from_type = 'location'
  from_value = location
  while from_type != 'seed':
    to_type = to_from[from_type]
    from_value = get_mapped_value(to_type, from_type, from_value, maps, forward=False)
    from_type = to_type
  for seed_range in seed_ranges:
    if from_value in seed_range:
      print(location)
      exit()