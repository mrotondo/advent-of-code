def find_guard(grid):
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == "^":
        return (x, y), (0, -1)
      
def position_is_within_grid(grid, pos):
  return pos[0] >= 0 and pos[0] < len(grid[0]) and pos[1] >= 0 and pos[1] < len(grid)

def turn_right(dir):
  return (-dir[1], dir[0])

def move_guard(grid, guard_pos, guard_dir):
  move_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
  if position_is_within_grid(grid, move_pos) and grid[move_pos[1]][move_pos[0]] == "#":
    return guard_pos, turn_right(guard_dir)
  else:
    return move_pos, guard_dir

f = open('input.txt')
grid = [line.strip() for line in f.readlines()]

guard_pos, guard_dir = find_guard(grid)
visited_positions = set()
guard_still_in_grid = True
while(guard_still_in_grid):
  visited_positions.add(guard_pos)
  guard_pos, guard_dir = move_guard(grid, guard_pos, guard_dir)
  guard_still_in_grid = position_is_within_grid(grid, guard_pos)

print(len(visited_positions))