import re

def vec3_add(a, b):
  return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

f = open('input.txt')
scan = set()
for line in f:
  x,y,z = map(int, re.search('(\d+),(\d+),(\d+)', line).groups())
  scan.add((x,y,z))

directions = [(1,0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
total_open_sides = 0
open_sides_and_direction = {}
for cube in scan:
  open_sides = 6
  for direction in directions:
    neighbor = vec3_add(cube, direction)
    if neighbor in scan:
      open_sides -= 1
  total_open_sides += open_sides

print(total_open_sides)

max_x = max([cube[0] for cube in scan])
max_y = max([cube[1] for cube in scan])
max_z = max([cube[2] for cube in scan])

air_visited = set()
air_to_visit = set([(-1,-1,-1)])
sides_encountered = 0
while len(air_to_visit) > 0:
  next_air = air_to_visit.pop()
  for direction in directions:
    neighbor = vec3_add(next_air, direction)
    if neighbor in scan:
      sides_encountered += 1
    elif (neighbor not in air_visited 
          and neighbor[0] >= -1 and neighbor[0] <= max_x + 1
          and neighbor[1] >= -1 and neighbor[1] <= max_y + 1
          and neighbor[2] >= -1 and neighbor[2] <= max_z + 1):
      air_to_visit.add(neighbor)
  air_visited.add(next_air)
print(sides_encountered)