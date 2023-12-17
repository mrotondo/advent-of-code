import re

def insert_row(after_i, image):
  width = len(image[0])
  image.insert(after_i + 1, ['.'] * width)

def insert_col(after_i, image):
  for row in image:
    row.insert(after_i + 1, '.')

f = open('input.txt')
image = []

for line in f.readlines():
  row = list(line.strip())
  image.append(row)

for row_i, row in reversed(list(enumerate(image))):
  if all([x == '.' for x in row]):
    insert_row(row_i, image)

width = len(image[0])
for col_i in [x - 1 for x in range(width, 0, -1)]:
  if all([x == '.' for row in image for x in row[col_i]]):
    insert_col(col_i, image)

galaxies = set()
for row_i, row in enumerate(image):
  for col_i, pixel in enumerate(row):
    if pixel == '#':
      galaxies.add((col_i, row_i))

total_distance = 0
while len(galaxies) > 0:
  galaxy = galaxies.pop()
  for other_galaxy in galaxies:
    total_distance += abs(other_galaxy[0] - galaxy[0]) + abs(other_galaxy[1] - galaxy[1])

print(total_distance)