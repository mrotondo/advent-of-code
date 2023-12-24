import re

f = open('test_input.txt')

def scan_for_wall(row_i, col_i, row_inc, col_inc, platform):
  row_to_check = row_i
  col_to_check = col_i
  while row_to_check > -1 and row_to_check < len(platform) and col_to_check > -1 and col_to_check < len(platform[0]) and platform[row_to_check][col_to_check] != '#':
    row_to_check += row_inc
    col_to_check += col_inc
  return (row_to_check, col_to_check)

def find_nearest_walls(platform):
  nearest_walls = {}
  for row_i in range(len(platform)):
    for col_i in range(len(platform[0])):
      if platform[row_i][col_i] != '#':
        nearest_walls_from_here = {'north': scan_for_wall(row_i, col_i, -1, 0, platform),
                                   'west': scan_for_wall(row_i, col_i, 0, -1, platform),
                                   'south': scan_for_wall(row_i, col_i, 1, 0, platform),
                                   'east': scan_for_wall(row_i, col_i, 0, 1, platform),}
        nearest_walls[(row_i, col_i)] = nearest_walls_from_here
  return nearest_walls

def find_rocks(from_direction):
  if from_direction == 'north':
    for row_i in range(len(platform)):
      for col_i in range(len(platform[0])):
        if platform[row_i][col_i] == 'O':
          yield (row_i, col_i)
  elif from_direction == 'west':
    for col_i in range(len(platform[0])):
      for row_i in range(len(platform)):
        if platform[row_i][col_i] == 'O':
          yield (row_i, col_i)
  elif from_direction == 'south':
    for row_i in range(len(platform) - 1, -1, -1):
      for col_i in range(len(platform[0])):
        if platform[row_i][col_i] == 'O':
          yield (row_i, col_i)
  elif from_direction == 'east':
    for row_i in range(len(platform[0]) - 1, -1, -1):
      for col_i in range(len(platform)):
        if platform[row_i][col_i] == 'O':
          yield (row_i, col_i)

DIRECTION_INCREMENTS = {'north': (-1, 0),
                        'west': (0, -1),
                        'south': (1, 0),
                        'east': (0, 1)}
def tilt(tilt_direction, platform, nearest_walls):
  row_inc, col_inc = DIRECTION_INCREMENTS[tilt_direction]
  for (rock_row, rock_col) in find_rocks(tilt_direction):
    # print('looking for nearest walls for rock at {}, {}'.format(rock_row, rock_col))
    (wall_row, wall_col) = nearest_walls[(rock_row, rock_col)][tilt_direction]
    # print('nearest wall is at {}, {}'.format(wall_row, wall_col))
    if wall_row - row_inc == rock_row and wall_col - col_inc == rock_col:
      # print('already against the wall, not moving')
      continue
    while (wall_row != rock_row or wall_col != rock_col) and platform[wall_row - row_inc][wall_col - col_inc] == 'O':
      # print('but there is already a rock at {}, {}'.format(wall_row - row_inc, wall_col - col_inc))
      wall_row -= row_inc
      wall_col -= col_inc
    if wall_row == rock_row and wall_col == rock_col:
      # print('already in a stack of rocks that is against a wall, not moving')
      continue
    # print('moving to new location {}, {}'.format(wall_row - row_inc, wall_col - col_inc))
    platform[wall_row - row_inc][wall_col - col_inc] = 'O'
    if wall_row - row_inc != rock_row or wall_col - col_inc != rock_col:
      # print('setting old location to empty')
      platform[rock_row][rock_col] = '.'

platform = []
for line in f.readlines():
  platform.append(list(line.strip()))

nearest_walls = find_nearest_walls(platform)
for i in range(1000000000):
  if i % 1000 == 0:
    print(i)
  tilt('north', platform, nearest_walls)
  tilt('west', platform, nearest_walls)
  tilt('south', platform, nearest_walls)
  tilt('east', platform, nearest_walls)

print('\n'.join(map(lambda row: ''.join([x for x in row]), platform)))

total = 0
for row_i, row in enumerate(platform):
  total += sum(1 if x == 'O' else 0 for x in row) * (len(platform) - row_i)
print(total)