import re

f = open('input.txt')

platform = []
for line in f.readlines():
  platform.append(list(line.strip()))
  for row_i in range(len(platform) - 1, 0, -1):
    for col_i in range(len(platform[0])):
      if platform[row_i][col_i] == 'O' and platform[row_i - 1][col_i] == '.':
        platform[row_i - 1][col_i] = 'O'
        platform[row_i][col_i] = '.'

print('\n'.join(map(lambda row: ''.join([x for x in row]), platform)))

total = 0
for row_i, row in enumerate(platform):
  total += sum(1 if x == 'O' else 0 for x in row) * (len(platform) - row_i)
print(total)