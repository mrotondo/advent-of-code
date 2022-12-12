import copy
import sys

def vec2_add(a, b):
  return (a[0] + b[0], a[1] + b[1])

def bounds_check(pos, h, w):
  return pos[0] >= 0 and pos[0] < w and pos[1] >= 0 and pos[1] < h

def ascendable(height_a, height_b):
  height_a = height_a.replace('S', 'a').replace('E', 'z')
  height_b = height_b.replace('S', 'a').replace('E', 'z')
  return ord(height_b) <= ord(height_a) + 1

def descendable(height_a, height_b):
  height_a = height_a.replace('S', 'a').replace('E', 'z')
  height_b = height_b.replace('S', 'a').replace('E', 'z')
  return ord(height_b) >= ord(height_a) - 1

def reachable(height_map, pos_a, pos_b, traversal_check):
  h = len(height_map)
  w = len(height_map[0])
  height_a = height_map[pos_a[1]][pos_a[0]]
  if bounds_check(pos_b, h, w):
    height_b = height_map[pos_b[1]][pos_b[0]]
    return traversal_check(height_a, height_b)
  return False

def find_char(height_map, char):
  h = len(height_map)
  w = len(height_map[0])
  for y in range(h):
    for x in range(w):
      if height_map[y][x] == char:
        return (x, y)

def djikstra(height_map, start, traversal_check):
  dist = {start: 0}
  unvisited = set([start])
  visited = set()

  while len(unvisited) > 0:
    closest_unvisited = sorted(unvisited, key=dist.get)[0]
    unvisited.remove(closest_unvisited)
    visited.add(closest_unvisited)

    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for move in moves:
      neighbor = vec2_add(closest_unvisited, move)        
      if (neighbor not in visited and reachable(height_map, closest_unvisited, neighbor, traversal_check)):
        unvisited.add(neighbor)
        new_dist = dist[closest_unvisited] + 1
        if neighbor not in dist or new_dist < dist[neighbor]:
          dist[neighbor] = new_dist

  return dist

f = open('input.txt').readlines()
height_map = list(map(str.strip, f))
start = find_char(height_map, 'S')
goal = find_char(height_map, 'E')

# part 1
dist = djikstra(height_map, start, ascendable)
print(dist[goal])

# part 2
dist = djikstra(height_map, goal, descendable)
min_dist = sys.maxsize
h = len(height_map)
w = len(height_map[0])
for y in range(h):
  for x in range(w):
    if height_map[y][x] == 'a' and (x, y) in dist and dist[(x, y)] < min_dist:
      min_dist = dist[(x, y)]

print(min_dist)