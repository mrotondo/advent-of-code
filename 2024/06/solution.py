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

def simulate_until_loop(grid, guard_pos, guard_dir, check_for_possible_loops):
  visited_positions = set()
  visited_orientations = set()
  loop_obstacle_locations = set()
  guard_still_in_grid = True
  while(guard_still_in_grid and (guard_pos, guard_dir) not in visited_orientations):
    visited_positions.add(guard_pos)
    visited_orientations.add((guard_pos, guard_dir))
    if check_for_possible_loops:
      obstacle_location = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
      if position_is_within_grid(grid, obstacle_location) and obstacle_location not in visited_positions:
        old_grid_value = grid[obstacle_location[1]][obstacle_location[0]]
        if old_grid_value == ".":
          grid[obstacle_location[1]][obstacle_location[0]] = "#"
          _, looped, _ = simulate_until_loop(grid, guard_pos, guard_dir, False)
          if looped:
            loop_obstacle_locations.add(obstacle_location)
          grid[obstacle_location[1]][obstacle_location[0]] = old_grid_value
    guard_pos, guard_dir = move_guard(grid, guard_pos, guard_dir)
    guard_still_in_grid = position_is_within_grid(grid, guard_pos)
  return visited_positions, (guard_pos, guard_dir) in visited_orientations, loop_obstacle_locations

f = open('input.txt')
grid = [list(line.strip()) for line in f.readlines()]
guard_pos, guard_dir = find_guard(grid)
visited_positions, looped, loop_obstacle_locations = simulate_until_loop(grid, guard_pos, guard_dir, True)
print(len(visited_positions))
print(len(loop_obstacle_locations))