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

def count_border_neighbors(grid, region, coords_to_regions):
  height = len(grid)
  width = len(grid[0])
  
  border_neighbors = {}
  for x, y in region:
    neighbor_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x_offset, y_offset in neighbor_offsets:
      neighbor = (x + x_offset, y + y_offset)
      if neighbor not in coords_to_regions or coords_to_regions[neighbor] != region:
        border_neighbors[neighbor] = border_neighbors.setdefault(neighbor, 0) + 1
  
  return sum(border_neighbors.values())

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
for region in regions:
  x, y = region[0]
  plant = grid[y][x]
  area = len(region)
  perimeter = count_border_neighbors(grid, region, coords_to_regions)
  # print("{} ({} * {}): {}".format(plant, area, perimeter, area * perimeter))
  total += area * perimeter

print(total)