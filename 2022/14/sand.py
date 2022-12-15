import sys

f = open('input.txt')

walls = []
bounds = [[sys.maxsize, 0], [sys.maxsize, 0]]
for line in f:
  point_strings = line.split(' -> ')
  points = list(map(lambda s: tuple(map(int, s.split(','))), point_strings))
  pairs = zip(points, points[1:])
  walls.extend(pairs)

source = (500, 0)

world = {}
for wall in walls:
  a, b = wall
  diff = (b[0] - a[0], b[1] - a[1])
  dist = max(map(abs, diff))
  x_inc = diff[0] // abs(diff[0]) if diff[0] != 0 else 0
  y_inc = diff[1] // abs(diff[1]) if diff[1] != 0 else 0
  x, y = a
  for i in range(dist + 1):
    world[(x, y)] = '#'
    x += x_inc
    y += y_inc

# @profile
def drop_sand(world, source, h):
  if source in world and world[source] == 'o':
    return (source, False)

  pos = source
  prev_pos = None
  while prev_pos != pos:
    if pos[1] == h + 2:
      return (pos, False)
    # part 2
    if pos[1]+1 == h + 2:
        break

    prev_pos = pos
    down_pos = (pos[0], pos[1] + 1)
    if down_pos not in world:
      pos = down_pos
      continue
    down_left_pos = (pos[0] - 1, pos[1] + 1)
    if down_left_pos not in world:
      pos = down_left_pos
      continue
    down_right_pos = (pos[0] + 1, pos[1] + 1)
    if down_right_pos not in world:
      pos = down_right_pos
      continue

  world[pos] = 'o'
  return (pos, True)

num_at_rest = 0
h = max([pos[1] for pos in world])
while True:
  result = drop_sand(world, source, h)
  if not result[1]:
    break
  num_at_rest += 1

for y in range(*bounds[1]):
  row = ''
  for x in range(*bounds[0]):
    if (x, y) in world:
      row += world[(x, y)]
    else:
      row += '.'
  print(row)
print(num_at_rest)
