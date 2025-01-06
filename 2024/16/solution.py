from enum import Enum
import math
import heapq

class Node:
  def __init__(self, x, y, direction):
    self.transitions = []
    self.x = x
    self.y = y
    self.direction = direction
    self.label = "{}, {}: {}".format(x, y, direction)
  
  def __repr__(self):
    return self.label
  
  def __lt__(self, other):
    return self.x < other.x

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

def search(node, goal_nodes):
  goal_x, goal_y = goal_nodes[0].x, goal_nodes[0].y
  heuristic = lambda node: abs(node.x - goal_x) + abs(node.y - goal_y) + node.direction.value * 0.1
  
  frontier = []
  heapq.heappush(frontier, (heuristic(node), 0, [node]))

  lowest_path_cost_to_nodes = {node: 0}
  lowest_path_cost_to_goal = math.inf
  shortest_paths_to_goal = []
  
  while len(frontier) > 0:
    _, path_cost, path = heapq.heappop(frontier)
    node = path[-1]
    if path_cost > lowest_path_cost_to_goal:
      continue
    elif node in goal_nodes:
      if path_cost == lowest_path_cost_to_goal:
        shortest_paths_to_goal.append(path)
      elif path_cost < lowest_path_cost_to_goal:
        shortest_paths_to_goal = [path]
        lowest_path_cost_to_goal = path_cost
    elif node in lowest_path_cost_to_nodes and lowest_path_cost_to_nodes[node] < path_cost:
      continue
    else:
      lowest_path_cost_to_nodes[node] = path_cost
      for transition_cost, transition_destination in node.transitions:
        cost_to_destination = path_cost + transition_cost
        heapq.heappush(frontier, (heuristic(transition_destination), cost_to_destination, path + [transition_destination]))
  return lowest_path_cost_to_goal, shortest_paths_to_goal

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

cost, shortest_paths = search(start_node, end_nodes)
print(cost)

tiles_in_shortest_paths = [(node.x, node.y) for path in shortest_paths for node in path]
print(len(set(tiles_in_shortest_paths)))