from enum import Enum
import math
import sys

sys.setrecursionlimit(15000)

class Node:
  def __init__(self, x, y, direction):
    self.transitions = []
    self.x = x
    self.y = y
    self.direction = direction
    self.label = "{}, {}: {}".format(x, y, direction)
  
  def __repr__(self):
    return self.label

class Direction(Enum):
  NORTH = 0
  EAST = 1
  SOUTH = 2
  WEST = 3

DIRECTION_OFFSETS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

class Tile:
  def __init__(self, x, y):
    self.direction_facing_nodes = [Node(x, y, Direction.NORTH), Node(x, y, Direction.EAST), Node(x, y, Direction.SOUTH), Node(x, y, Direction.WEST)]

    for i in range(4):
      counterclockwise_node = self.direction_facing_nodes[i - 1]
      clockwise_node = self.direction_facing_nodes[i - 3]
      self.direction_facing_nodes[i].transitions.append((1000, counterclockwise_node))
      self.direction_facing_nodes[i].transitions.append((1000, clockwise_node))
  
  def connect_to_tile(self, neighbor_tile, direction):
    departure_start_node = self.direction_facing_nodes[direction]
    departure_end_node = neighbor_tile.direction_facing_nodes[direction]
    return_start_node = neighbor_tile.direction_facing_nodes[direction - 2]
    return_end_node = self.direction_facing_nodes[direction - 2]

    departure_start_node.transitions.append((1, departure_end_node))
    return_start_node.transitions.append((1, return_end_node))

def search(node, goal_nodes, visited_nodes, cost_so_far=0):
  if node in goal_nodes:
    return (cost_so_far, [[node]])
  elif node in visited_nodes and visited_nodes[node] < cost_so_far:
    return (math.inf, [[]])
  else:
    visited_nodes[node] = cost_so_far
    paths = []
    for transition_cost, to_node in node.transitions:
      cost, all_shortest_paths = search(to_node, goal_nodes, visited_nodes, cost_so_far + transition_cost)
      for path in all_shortest_paths:
        paths.append((cost, [node] + path))
    if len(paths) > 0:
      min_cost = min([cost for cost, _ in paths])
      shortest_paths = [path for cost, path in paths if cost == min_cost]
      return (min_cost, shortest_paths)
    else:
      return (math.inf, [[]])

input_file = open("input.txt")
grid = [line.strip() for line in input_file.readlines()]

start_node = None
end_nodes = None

tiles = {}

height = len(grid)
width = len(grid[0])

for y in range(height):
  for x in range(width):
    tile_character = grid[y][x]
    if tile_character == "." or tile_character == "S" or tile_character == "E":
      tile = Tile(x, y)
      tiles[(x, y)] = tile
      for direction in range(4):
        offset = DIRECTION_OFFSETS[direction]
        neighbor_coords = (x + offset[0], y + offset[1])
        if neighbor_coords in tiles:
          tile.connect_to_tile(tiles[neighbor_coords], direction)
      if tile_character == "S":
        start_node = tile.direction_facing_nodes[Direction.EAST.value]
      elif tile_character == "E":
        end_nodes = tile.direction_facing_nodes

cost, all_shortest_paths = search(start_node, end_nodes, {})
print(cost)
for node in all_shortest_paths[0]:
  print(node)
tiles_in_shortest_paths = [(node.x, node.y) for path in all_shortest_paths for node in path]
print(len(set(tiles_in_shortest_paths)))