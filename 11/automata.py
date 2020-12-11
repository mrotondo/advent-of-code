def read_grid(s):
  return [row for row in s.split("\n") if row]

def get_grid(grid, x, y):
  if (x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)):
    return (False, -1)
  return (True, grid[y][x])

def get_neighbors1(grid, x, y):
  neighbors = []
  for y_off in [-1, 0, 1]:
    for x_off in [-1, 0, 1]:
      if x_off != 0 or y_off != 0:
        (good_coord, cell_value) = get_grid(grid, x + x_off, y + y_off)
        if good_coord:
          neighbors += cell_value
  return neighbors

def mul_vec(v, i):
  return (v[0] * i, v[1] * i)

def get_neighbors2(grid, x, y):
  neighbors = []
  for y_off in [-1, 0, 1]:
    for x_off in [-1, 0, 1]:
      if x_off != 0 or y_off != 0:
        direction = (x_off, y_off)
        i = 1
        while (True):
          (x_vec, y_vec) = mul_vec(direction, i)
          i += 1
          (good_coord, cell_value) = get_grid(grid, x + x_vec, y + y_vec)
          if good_coord and (cell_value == 'L' or cell_value == '#'):
            neighbors += cell_value
            break
          elif not good_coord:
            break
  return neighbors

def maybe_apply_rule(cell_value, neighbors, rule):
  if rule[0](neighbors):
    return (True, rule[1])
  else:
    return (False, cell_value)

def update(grid, rules):
  new_grid = []
  num_rule_applications = 0
  for y in range(len(grid)):
    new_row = []
    for x in range(len(grid[y])):
      (good_coord, cell_value) = get_grid(grid, x, y)
      neighbors = get_neighbors2(grid, x, y)
      if cell_value in rules:
        rule = rules[cell_value]
        (rule_applied, new_cell_value) = maybe_apply_rule(cell_value, neighbors, rule)
        if rule_applied:
          num_rule_applications += 1
        new_row += new_cell_value
      else:
        new_row += cell_value
    new_grid.append(new_row)
  return (num_rule_applications, new_grid)

f = open('input.txt')
grid = read_grid(f.read())
rules1 = {
          'L': (lambda neighbors: neighbors.count('#') == 0, '#'),
          '#': (lambda neighbors: neighbors.count('#') >= 4, 'L')
        }
rules2 = {
          'L': (lambda neighbors: neighbors.count('#') == 0, '#'),
          '#': (lambda neighbors: neighbors.count('#') >= 5, 'L')
        }

while True:
  # print('\n'.join(map(str, grid)))
  # print('---')
  # print(get_grid(grid, 8, 1))
  # print(get_neighbors2(grid, 8, 1))
  num_rule_applications, new_grid = update(grid, rules2)
  # print(num_rule_applications)
  if num_rule_applications == 0:
    break
  grid = new_grid

num_occupied = 0
print(sum(map(lambda row: row.count('#'), grid)))