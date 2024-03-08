import re
import sys

# order: nesw
directions = {'|': {'x': [], 'y': [-1, 1]},
              '-': {'x': [-1, 1], 'y': []},
              'L': {'x': [1], 'y': [-1]},
              'J': {'x': [-1], 'y': [-1]},
              '7': {'x': [-1], 'y': [1]},
              'F': {'x': [1], 'y': [1]},
              '.': {'x': [], 'y': []},
              'S': {'x': [-1, 1], 'y': [-1, 1]}}

def get_connected_pipes(pos, map_connectivity):
  connected_pipes = [pos]
  while True:
    directions_to_check = map_connectivity[pos]
    pipes_to_check = []
    for x_delta in directions_to_check['x']:
      pos_to_check = (pos[0] + x_delta, pos[1])
      if pos_to_check in map_connectivity and -x_delta in map_connectivity[pos_to_check]['x']:
        if pos_to_check not in connected_pipes:
          pipes_to_check.append(pos_to_check)
    for y_delta in directions_to_check['y']:
      pos_to_check = (pos[0], pos[1] + y_delta)
      if pos_to_check in map_connectivity and -y_delta in map_connectivity[pos_to_check]['y']:
        if pos_to_check not in connected_pipes:
          pipes_to_check.append(pos_to_check)
    if len(pipes_to_check) == 0:
      break
    pos = pipes_to_check[0]
    connected_pipes.append(pos)
  return connected_pipes

f = open('test_input_3.txt')
map_connectivity = {}
start = None
for line_index, line in enumerate(f.readlines()):
  for symbol_index, map_symbol in enumerate(line.strip()):
    pos = (symbol_index, line_index)
    if map_symbol == 'S':
      start = pos
    map_connectivity[pos] = directions[map_symbol]

connected_pipes = get_connected_pipes(start, map_connectivity)
print(len(connected_pipes) // 2)