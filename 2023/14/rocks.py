import re

f = open('test_input.txt')

platform = []
for line in f.readlines():
  platform.append(list(line.strip()))

def tilt_north():
  for row_max in range(1, len(platform)):
    for row_i in range(row_max, 0, -1):
      for col_i in range(len(platform[0])):
        if platform[row_i][col_i] == 'O' and platform[row_i - 1][col_i] == '.':
          platform[row_i - 1][col_i] = 'O'
          platform[row_i][col_i] = '.'

def tilt_west():
  for col_max in range(1, len(platform[0])):
    for col_i in range(col_max, 0, -1):
      for row_i in range(len(platform)):
        if platform[row_i][col_i] == 'O' and platform[row_i][col_i - 1] == '.':
          platform[row_i][col_i - 1] = 'O'
          platform[row_i][col_i] = '.'

def tilt_south():
  for row_min in range(len(platform), 0, -1):
    for row_i in range(row_min - 1, len(platform) - 1):
      for col_i in range(len(platform[0])):
        if platform[row_i][col_i] == 'O' and platform[row_i + 1][col_i] == '.':
          platform[row_i + 1][col_i] = 'O'
          platform[row_i][col_i] = '.'

def tilt_east():
  for col_min in range(len(platform[0]), 0, -1):
    for col_i in range(col_min - 1, len(platform[0]) - 1):
      for row_i in range(len(platform)):
        if platform[row_i][col_i] == 'O' and platform[row_i][col_i + 1] == '.':
          platform[row_i][col_i + 1] = 'O'
          platform[row_i][col_i] = '.'

for i in range(1000000000):
  if i % 1000 == 0:
    print(i)
  tilt_north()
  tilt_west()
  tilt_south()
  tilt_east()

print('\n'.join(map(lambda row: ''.join([x for x in row]), platform)))

total = 0
for row_i, row in enumerate(platform):
  total += sum(1 if x == 'O' else 0 for x in row) * (len(platform) - row_i)
print(total)