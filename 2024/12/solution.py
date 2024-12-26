def flood_fill_region(grid, x, y, plant, region, coords_to_regions):
  height = len(grid)
  width = len(grid[0])
  
  if x < 0 or y < 0 or x >= width or y >= height:
    return
  if (x, y) in coords_to_regions:
    return
  plant_at_coordinates = grid[y][x]
  if plant_at_coordinates == plant:
    region.append((x, y))
    coords_to_regions[(x, y)] = region
    neighbor_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x_offset, y_offset in neighbor_offsets:
      flood_fill_region(grid, x + x_offset, y + y_offset, plant, region, coords_to_regions)

def detect_border_neighbors(grid, region, coords_to_regions):
  height = len(grid)
  width = len(grid[0])
  
  border_neighbors = set()
  for x, y in region:
    neighbor_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for neighbor_offset in neighbor_offsets:
      neighbor = (x + neighbor_offset[0], y + neighbor_offset[1])
      if neighbor not in coords_to_regions or coords_to_regions[neighbor] != region:
        border_neighbors.add((neighbor, neighbor_offset))
  
  return border_neighbors

def detect_sides(border_neighbors):
  sides = []
  for neighbor_coords, neighbor_direction in border_neighbors:
    sides_added_to = []
    for side in sides:
      _, side_example_direction = list(side)[0]
      if neighbor_direction != side_example_direction:
        continue
      adjacent_to_side = False
      for side_neighbor_coords, side_neighbor_direction in side:
        x_distance = abs(side_neighbor_coords[0] - neighbor_coords[0])
        y_distance = abs(side_neighbor_coords[1] - neighbor_coords[1])
        if x_distance + y_distance == 1:
          adjacent_to_side = True
          break
      if not adjacent_to_side:
        continue
      side.add((neighbor_coords, neighbor_direction))
      sides_added_to.append(side)
    if len(sides_added_to) == 0:
      side = set([(neighbor_coords, neighbor_direction)])
      sides.append(side)
      sides_added_to.append(side)
    if len(sides_added_to) > 1:
      new_side = set.union(*sides_added_to)
      for side_added_to in sides_added_to:
        sides.remove(side_added_to)
      sides.append(new_side)
  return sides

f = open('input.txt')
grid = [line.strip() for line in f.readlines()]

height = len(grid)
width = len(grid[0])

regions = []
coords_to_regions = {}

for y in range(height):
  for x in range(width):
    if (x, y) in coords_to_regions:
      continue
    else:
      plant = grid[y][x]
      region = []
      regions.append(region)
      flood_fill_region(grid, x, y, plant, region, coords_to_regions)

total = 0
total_2 = 0
for region in regions:
  x, y = region[0]
  plant = grid[y][x]
  area = len(region)
  border_neighbors = detect_border_neighbors(grid, region, coords_to_regions)
  sides = detect_sides(border_neighbors)
  perimeter = len(border_neighbors)
  # print("{} ({} * {}, {}): {} / {}".format(plant, area, perimeter, len(sides), area * perimeter, area * len(sides)))
  total += area * perimeter
  total_2 += area * len(sides)

print(total)
print(total_2)