
def check_word(word, grid, x, y, x_direction, y_direction, width, height):
  for i in range(len(word)):
    check_x = x + x_direction * i
    check_y = y + y_direction * i
    if check_x < 0 or check_x >= width or check_y < 0 or check_y >= height:
      return False
    if grid[check_y][check_x] != word[i]:
      return False
  return True

f = open('input.txt')
grid = [line.strip() for line in f.readlines()]

height = len(grid)
width = len(grid[0])

total = 0
for y in range(height):
  for x in range(width):
    for y_direction in [-1, 0, 1]:
      for x_direction in [-1, 0, 1]:
        if check_word("XMAS", grid, x, y, x_direction, y_direction, width, height):
          total += 1

print(total)

total = 0
for y in range(height - 2):
  for x in range(width - 2):
    if check_word("MAS", grid, x, y, 1, 1, width, height) or check_word("SAM", grid, x, y, 1, 1, width, height):
      if check_word("MAS", grid, x+2, y, -1, 1, width, height) or check_word("SAM", grid, x+2, y, -1, 1, width, height):
        total += 1

print(total)