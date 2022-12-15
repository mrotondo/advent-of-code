import re
import sys

line_re = re.compile('Sensor at x=(\-?\d+), y=(\-?\d+): closest beacon is at x=(\-?\d+), y=(\-?\d+)')
f = open('input.txt')
sensors = {}
beacons = {}
for line in f:
  sx, sy, bx, by = line_re.search(line).groups()
  sx = int(sx); sy = int(sy); bx = int(bx); by = int(by);
  sensors[(sx, sy)] = (bx, by)
  beacons.setdefault((bx, by), []).append((sx, sy))

def dist(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

# part 1
# check_y = 2000000
# impossible_xs = set()
# for sensor, beacon in sensors.items():
#   d = dist(sensor, beacon)
#   for x in range(sensor[0] - d - 10, sensor[0] + d + 10):
#     if dist(sensor, (x, check_y)) <= d:
#       impossible_xs.add(x)
# beacons_at_check_y = [beacon for beacon in beacons if beacon[1] == check_y]

# print(len(impossible_xs) - len(beacons_at_check_y))

# part 2 
class BlockMerger:
  def __init__(self):
    self.blocks = []
  
  def add_block(self, new_block):
    inserted = False
    i = 0
    while i < len(self.blocks):
      block = self.blocks[i]
      if new_block[1] < block[0]:
        self.blocks.insert(i, new_block)
        inserted = True
        break
      elif new_block[0] <= block[1] and new_block[1] >= block[0]:
        new_block = (min(new_block[0], block[0]), max(new_block[1], block[1]))
        del self.blocks[i]
        i -= 1
      i += 1
    if not inserted:
      self.blocks.append(new_block)

  def merge_adjacent(self):
    if len(self.blocks) < 2:
      return
    i = 0
    while i < len(self.blocks) - 1:
      block = self.blocks[i]
      next_block = self.blocks[i + 1]
      if block[1] + 1 == next_block[0]:
        new_block = (block[0], next_block[1])
        del self.blocks[i:i+2]
        self.blocks.insert(i, new_block)
        i -= 1
      i += 1

  def gaps(self):
    if len(self.blocks) < 2:
      return
    gaps = []
    for i in range(len(self.blocks) - 1):
      block = self.blocks[i]
      next_block = self.blocks[i + 1]
      gap = (block[1] + 1, next_block[0] - 1)
      gaps.append(gap)
    return gaps

  def __repr__(self):
    return str(self.blocks)

# search_space_size = 20
search_space_size = 4000000
row_blocks = {}
for sensor, beacon in sensors.items():
  d = dist(sensor, beacon)
  # print(f'sensor {sensor} has beacon {beacon} with dist {d}')
  for y in range(search_space_size + 1):
    y_dist = abs(y - sensor[1])
    if y_dist <= d:
      width_at_y = max(0, (d - y_dist) * 2 + 1)
      # print(f'at y {y}, y_dist is {y_dist} and width is {width_at_y}')
      min_x = sensor[0] - width_at_y // 2
      max_x = sensor[0] + width_at_y // 2
      # print(f'adding block {(min_x, max_x)}')
      row_blocks.setdefault(y, BlockMerger()).add_block((min_x, max_x))
  # print('-')

for y, row_block in row_blocks.items():
  row_block.merge_adjacent()
  gaps = row_block.gaps()
  if gaps:
    print(f'y: {y}, gaps: {gaps}')

# print([f'{y}: {row_blocks[y]}' for y in sorted(row_blocks)])