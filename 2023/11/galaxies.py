import re

f = open('input.txt')
image = []

for line in f.readlines():
  row = list(line.strip())
  image.append(row)

expansion_amount = 999999
empty_rows = set()
empty_cols = set()

for row_i, row in enumerate(image):
  if all([x == '.' for x in row]):
    empty_rows.add(row_i)

width = len(image[0])
for col_i in range(width):
  if all([x == '.' for row in image for x in row[col_i]]):
    empty_cols.add(col_i)

galaxies = set()
for row_i, row in enumerate(image):
  for col_i, pixel in enumerate(row):
    if pixel == '#':
      galaxies.add((col_i, row_i))

total_distance = 0
while len(galaxies) > 0:
  galaxy = galaxies.pop()
  for other_galaxy in galaxies:
    x_span = (min(other_galaxy[0], galaxy[0]), max(other_galaxy[0], galaxy[0]))
    y_span = (min(other_galaxy[1], galaxy[1]), max(other_galaxy[1], galaxy[1]))
    spanned_empty_cols = list(filter(lambda x: x in range(x_span[0] + 1, x_span[1]), empty_cols))
    spanned_empty_rows = list(filter(lambda y: y in range(y_span[0] + 1, y_span[1]), empty_rows))

    distance = x_span[1] - x_span[0] + y_span[1] - y_span[0]
    
    distance += expansion_amount * len(spanned_empty_cols) + expansion_amount * len(spanned_empty_rows)
    total_distance += distance

print(total_distance)