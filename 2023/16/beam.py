from collections import defaultdict
import sys

sys.setrecursionlimit(3000)

def process_beam(prev_pos, movement, grid, grid_size, traversed_locations):
  new_pos = (prev_pos[0] + movement[0], prev_pos[1] + movement[1])
  if new_pos[0] < 0 or new_pos[0] > grid_size[0] or new_pos[1] < 0 or new_pos[1] > grid_size[1]:
    return
  if movement in traversed_locations[new_pos]:
    return
  traversed_locations[new_pos][movement] += 1
  processing_element = grid[new_pos]
  if processing_element == '.':
    process_beam(new_pos, movement, grid, grid_size, traversed_locations)
  elif processing_element == '/':
    process_beam(new_pos, (-movement[1], -movement[0]), grid, grid_size, traversed_locations)
  elif processing_element == '\\':
    process_beam(new_pos, (movement[1], movement[0]), grid, grid_size, traversed_locations)
  elif processing_element == '-':
    if movement[1] == 0:
      process_beam(new_pos, movement, grid, grid_size, traversed_locations)
    else:
      process_beam(new_pos, (-1, 0), grid, grid_size, traversed_locations)
      process_beam(new_pos, (1, 0), grid, grid_size, traversed_locations)
  elif processing_element == '|':
    if movement[0] == 0:
      process_beam(new_pos, movement, grid, grid_size, traversed_locations)
    else:
      process_beam(new_pos, (0, -1), grid, grid_size, traversed_locations)
      process_beam(new_pos, (0, 1), grid, grid_size, traversed_locations)

f = open('input.txt')

grid = {}
max_row_i = 0
max_col_i = 0
for row_i, line in enumerate(f.readlines()):
  max_row_i = max(max_row_i, row_i)
  for col_i, element in enumerate(line.strip()):
    max_col_i = max(max_col_i, col_i)
    grid[(col_i, row_i)] = element

max_energized_tiles = 0
for col_i in range(max_col_i + 1):
  traversed_locations = defaultdict(lambda: defaultdict(int))
  process_beam((col_i, -1), (0, 1), grid, (max_col_i, max_row_i), traversed_locations)
  max_energized_tiles = max(max_energized_tiles, len(traversed_locations))

  traversed_locations = defaultdict(lambda: defaultdict(int))
  process_beam((col_i, max_row_i + 1), (0, -1), grid, (max_col_i, max_row_i), traversed_locations)
  max_energized_tiles = max(max_energized_tiles, len(traversed_locations))

for row_i in range(max_row_i + 1):
  traversed_locations = defaultdict(lambda: defaultdict(int))
  process_beam((-1, row_i), (1, 0), grid, (max_col_i, max_row_i), traversed_locations)
  max_energized_tiles = max(max_energized_tiles, len(traversed_locations))

  traversed_locations = defaultdict(lambda: defaultdict(int))
  process_beam((max_col_i + 1, row_i), (-1, 0), grid, (max_col_i, max_row_i), traversed_locations)
  max_energized_tiles = max(max_energized_tiles, len(traversed_locations))

print(max_energized_tiles)