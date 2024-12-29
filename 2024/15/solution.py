import numpy as np

def read_map(input_file):
  map = {}
  position = None
  line = input_file.readline().strip()
  y = 0
  while line != "":
    x = 0
    for x, character in enumerate(line):
      if character == "@":
        map[(x, y)] = "."
        position = np.array((x, y))
      else:
        map[(x, y)] = character
    y += 1
    line = input_file.readline().strip()
  return map, position

def print_map(map, position):
  width = max(x for (x, _) in map.keys())
  height = max(y for (_, y) in map.keys())
  for y in range(height + 1):
    for x in range(width + 1):
      if (x, y) == tuple(position):
        print("@", end="")
      else:
        print(map[(x, y)], end="")
    print("")

  
def move(position, direction, map):
  blank_space = None
  spaces_checked = 1
  space_to_check = tuple(position + direction * spaces_checked)
  while space_to_check in map:
    if map[space_to_check] == ".":
      blank_space = space_to_check
      break
    elif map[space_to_check] == "#":
      break
    else:
      spaces_checked += 1
      space_to_check = tuple(position + direction * spaces_checked)
  if blank_space:
    for i in range(spaces_checked - 1, 0, -1):
      map[tuple(blank_space)] = map[tuple(blank_space - direction)]
      map[tuple(blank_space - direction)] = "."
      blank_space -= direction
    return position + direction
  else:
    return position

UP = np.array([0, -1])
DOWN = np.array([0, 1])
LEFT = np.array([-1, 0])
RIGHT = np.array([1, 0])
input_file = open("input.txt")
map, position = read_map(input_file)
for line in input_file.readlines():
  for command in line:
    match command:
      case "^":
        position = move(position, UP, map)
      case "v":
        position = move(position, DOWN, map)
      case "<":
        position = move(position, LEFT, map)
      case ">":
        position = move(position, RIGHT, map)
      case _:
        continue

total = 0
for p, character in map.items():
  if character == "O":
    total += 100 * p[1] + p[0]
print(total)

# print_map(map, position)