from collections import deque

def find_bounds(elves):
  min_x = min(elves.keys(), key=lambda elf: elf[0])[0]
  min_y = min(elves.keys(), key=lambda elf: elf[1])[1]
  max_x = max(elves.keys(), key=lambda elf: elf[0])[0]
  max_y = max(elves.keys(), key=lambda elf: elf[1])[1]
  return ((min_x, min_y), (max_x, max_y))

def print_elves(elves):
  bounds = find_bounds(elves)
  for y in range(bounds[0][1], bounds[1][1] + 1):
    s = ''
    for x in range(bounds[0][0], bounds[1][0] + 1):
      if (x, y) in elves:
        s += '#'
      else:
        s += '.'
    print(s)

f = open('input.txt')

elves = {}
for y, line in enumerate(f):
  for x, char in enumerate(line.strip()):
    if char == '#':
      elves[(x,y)] = (x,y)

moves = deque([(0,-1), (0,1), (-1,0), (1,0)])
round = 0
while True:
  round += 1
  # print(round)
  # print_elves(elves)
  # print(len(elves))
  # print('----')
  num_moves = 0
  for elf in elves.keys():
    any_neighbors = False
    for y in [-1,0,1]:
      for x in [-1,0,1]:
        check_pos = (elf[0] + x, elf[1] + y)
        if not (x == 0 and y == 0) and check_pos in elves:
          # print(f'neighbor at {check_pos}')
          any_neighbors = True
    if not any_neighbors:
      # print(f'elf {elf} does not need to move')
      continue

    num_moves += 1
    # print(f'elf {elf} considering moves...')
    for move in moves:
      # print(f'considering {move}...')
      zero_index = move.index(0)
      can_move = True
      for scan_offset in [-1,0,1]:
        scan = list(move)
        scan[zero_index] = scan_offset
        scan_pos = (elf[0] + scan[0], elf[1] + scan[1])
        # print(f'scanning at {tuple(scan_pos)}...')
        if tuple(scan_pos) in elves:
          # print(f'Elf there!')
          can_move = False
      if can_move:
        # print(f'Looks good!')
        elves[elf] = (elf[0] + move[0], elf[1] + move[1])
        break

  if num_moves == 0:
    break
  # else:
  #   print(num_moves)

  moves.append(moves.popleft())
  new_elves = {}

  num_elves_per_dest = {}
  for elf, dest in elves.items():
    num_elves = num_elves_per_dest.setdefault(dest, 0)
    num_elves_per_dest[dest] = num_elves + 1

  for elf, dest in elves.items():
    # print(f'elf at {elf} trying to move to {dest}')
    if num_elves_per_dest[dest] == 1:
      # print(f'moving elf {elf} by {move}')
      new_elves[dest] = dest
    else:
      new_elves[elf] = elf
  elves = new_elves

bounds = find_bounds(elves)
# print(bounds)
w = bounds[1][0] - bounds[0][0] + 1
h = bounds[1][1] - bounds[0][1] + 1
# print(f'{w}x{h}')
print_elves(elves)
print(round)
print(w*h - len(elves))