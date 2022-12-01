
def read_grid(s):
  lines = [line for line in s.split("\n") if len(line) > 0]
  y = dict([(i, dict([(j, lines[i][j]) for j in range(len(lines[i]))])) for i in range(len(lines))])
  return y

def get_grid(grid, x, y, z):
  if z in grid:
    if y in grid[z]:
      if x in grid[z][y]:
        return (True, grid[z][y][x])
  return (False, '.')
  
def get_neighbors(grid, x, y, z):
  neighbors = []
  for z_off in [-1, 0, 1]:
    for y_off in [-1, 0, 1]:
      for x_off in [-1, 0, 1]:
        if x_off != 0 or y_off != 0 or z_off != 0:
          (good_coord, cell_value) = get_grid(grid, x + x_off, y + y_off, z + z_off)
          if good_coord:
            neighbors.append(cell_value)
  return neighbors

def maybe_apply_rule(cell_value, neighbors, rule):
  if rule[0](neighbors):
    return (True, rule[1])
  else:
    return (False, cell_value)

def update(grid, rules):
  new_grid = {}
  num_rule_applications = 0
  for z in range(min(grid) - 1, max(grid) + 2):
    new_z = {}
    for y in range(min(grid[0]) - 1, max(grid[0]) + 2):
      new_y = {}
      for x in range(min(grid[0][0]) - 1, max(grid[0][0]) + 2):
        (good_coord, cell_value) = get_grid(grid, x, y, z)
        neighbors = get_neighbors(grid, x, y, z)
        if cell_value in rules:
          rule = rules[cell_value]
          (rule_applied, new_cell_value) = maybe_apply_rule(cell_value, neighbors, rule)
          if rule_applied:
            num_rule_applications += 1
          new_y[x] = new_cell_value
        else:
          new_y[x] = cell_value
      new_z[y] = new_y
    new_grid[z] = new_z
  return (num_rule_applications, new_grid)

def count_live_in_row(row):
  return row.values().count('#')

def count_live_in_layer(layer):
  return sum(map(count_live_in_row, [layer[y] for y in layer.keys()]))

def count_live_in_grid(grid):
  return sum(map(count_live_in_layer, [grid[z] for z in grid.keys()]))

f = open('input.txt')
grid = {}
grid[0] = read_grid(f.read())
print(grid)
rules = {
          '#': (lambda neighbors: neighbors.count('#') < 2 or neighbors.count('#') > 3, '.'),
          '.': (lambda neighbors: neighbors.count('#') == 3, '#')
        }

for i in range(6):
  print(count_live_in_grid(grid))
  num_rule_applications, new_grid = update(grid, rules)
  # print(new_grid)
  print('--')
  grid = new_grid

# print(grid)
print(count_live_in_grid(grid))

# num_occupied = 0
# print(sum(map(lambda row: row.count('#'), grid)))