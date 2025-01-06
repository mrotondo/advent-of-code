import numpy as np

UP = np.array([0, -1])
DOWN = np.array([0, 1])
LEFT = np.array([-1, 0])
RIGHT = np.array([1, 0])

def read_map(input_file):
  map_dict = {}
  position = None
  line = input_file.readline().strip()
  y = 0
  while line != "":
    x = 0
    for x, character in enumerate(line):
      if character == "@":
        map_dict[(x, y)] = "."
        position = np.array((x, y))
      else:
        map_dict[(x, y)] = character
    y += 1
    line = input_file.readline().strip()
  return map_dict, position

def read_map_2(input_file):
  map_dict = {}
  position = None
  line = input_file.readline().strip()
  y = 0
  while line != "":
    x = 0
    for x, character in enumerate(line):
      if character == "@":
        map_dict[(x*2, y)] = "."
        map_dict[(x*2+1, y)] = "."
        position = np.array((x*2, y))
      elif character == "O":
        map_dict[(x*2, y)] = "["
        map_dict[(x*2+1, y)] = "]"
      else:
        map_dict[(x*2, y)] = character
        map_dict[(x*2+1, y)] = character
    y += 1
    line = input_file.readline().strip()
  return map_dict, position

def print_map(map_dict, position):
  width = max(x for (x, _) in map_dict.keys())
  height = max(y for (_, y) in map_dict.keys())
  for y in range(height + 1):
    for x in range(width + 1):
      if (x, y) == tuple(position):
        print("@", end="")
      else:
        print(map_dict[(x, y)], end="")
    print("")

def can_move(position, direction, map_dict, checked_positions = None):
  if checked_positions is None:
    checked_positions = set()
  if tuple(position) in checked_positions:
    return []
  checked_positions.add(tuple(position))
  space_to_check = tuple(position + direction)
  try:
    match map_dict[space_to_check]:
      case "#":
        return [None]
      case "O":
        return [space_to_check] + can_move(space_to_check, direction, map_dict, checked_positions)
      case "[":
        if direction[1] != 0:
          return [space_to_check] \
            + can_move(position + RIGHT, direction, map_dict, checked_positions) \
            + can_move(space_to_check, direction, map_dict, checked_positions)
        else:
          return [space_to_check] + can_move(position + direction, direction, map_dict, checked_positions)
      case "]":
        if direction[1] != 0:
          return [space_to_check] \
            + can_move(position + LEFT, direction, map_dict, checked_positions) \
            + can_move(space_to_check, direction, map_dict, checked_positions)
        else:
          return [space_to_check] + can_move(space_to_check, direction, map_dict, checked_positions)
      case ".":
        return []
      case _:
        return [None]
  except KeyError:
    return [None]

def move(position, direction, map_dict):
  # print_map(map_dict, position)
  # print(direction)
  moveable_objects = can_move(position, direction, map_dict)
  # print(moveable_objects)
  if any([move is None for move in moveable_objects]):
    return position
  else:
    new_map_dict_overlay = {}
    for start in moveable_objects:
      new_map_dict_overlay[tuple(start + direction)] = map_dict[tuple(start)]
    
    move_starts = set(map(tuple, moveable_objects))
    move_ends = set([tuple(start + direction) for start in moveable_objects])
    only_starts = move_starts - move_ends
    for only_start in only_starts:
      new_map_dict_overlay[only_start] = "."

    for pos_to_overwrite, overwrite_character in new_map_dict_overlay.items():
      map_dict[pos_to_overwrite] = overwrite_character
    
    return position + direction

def run_commands(map_dict, position, input_file):
  for line in input_file.readlines():
    for command in line:
      match command:
        case "^":
          position = move(position, UP, map_dict)
        case "v":
          position = move(position, DOWN, map_dict)
        case "<":
          position = move(position, LEFT, map_dict)
        case ">":
          position = move(position, RIGHT, map_dict)
        case _:
          continue
  print_map(map_dict, position)

# input_file = open("test_input_2.txt")
# map_dict, position = read_map(input_file)
# run_commands(map_dict, position, input_file)

# total = 0
# for p, character in map_dict.items():
#   if character == "O":
#     total += 100 * p[1] + p[0]
# print(total)

input_file = open("input.txt")
map_dict, position = read_map_2(input_file)
run_commands(map_dict, position, input_file)

total = 0
for p, character in map_dict.items():
  if character == "[":
    total += 100 * p[1] + p[0]
print(total)