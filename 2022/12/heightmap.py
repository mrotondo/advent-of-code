import copy
import sys

def vec2_add(a, b):
  return (a[0] + b[0], a[1] + b[1])

def bounds_check(pos, h, w):
  return pos[0] >= 0 and pos[0] < w and pos[1] >= 0 and pos[1] < h

def traversable(a, b):
  a = a.replace('S', 'a').replace('E', 'z')
  b = b.replace('S', 'a').replace('E', 'z')
  return abs(ord(a) - ord(b)) <= 1

def find(height_map, char):
  h = len(height_map)
  w = len(height_map[0])
  for y in range(h):
    for x in range(w):
      if height_map[y][x] == char:
        return (x, y)

moves = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def search(height_map, pos, goal, path, visited):
  path.append(pos)
  visited.add(pos)
  if pos == goal:
    return len(path)
  h = len(height_map)
  w = len(height_map[0])
  paths = []
  height = height_map[pos[1]][pos[0]]
  for move in moves:
    new_pos = vec2_add(pos, move)
    if bounds_check(new_pos, h, w):
      new_height = height_map[new_pos[1]][new_pos[0]]
      if (traversable(height, new_height) and new_pos not in path):
        paths.append(search(height_map, new_pos, goal, copy.copy(path), visited))
  return min(paths) if len(paths) > 0 else sys.maxsize

f = open('input.txt').readlines()
height_map = list(map(str.strip, f))
start = find(height_map, 'S')
goal = find(height_map, 'E')

print(start)
print(goal)

print(search(height_map, start, goal, [], set()) - 1)