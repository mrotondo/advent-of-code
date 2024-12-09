import re
f = open('input.txt')
grid = [list(line.strip()) for line in f.readlines()]
antenna_regex = re.compile("[0-9a-zA-Z]")

width = len(grid[0])
height = len(grid)

antenna_locations = {}
for y in range(len(grid)):
  for x in range(len(grid[0])):
    if re.match(antenna_regex, grid[y][x]):
      antenna_locations.setdefault(grid[y][x], []).append((x, y))

def locate_antinodes(antenna_locations, width, height, harmonics): 
  antinode_locations = set()
  for antenna, locations in antenna_locations.items():
    for location in locations:
      for other_location in locations:
        if location != other_location:
          for harmonic in harmonics:
            diff = (other_location[0] - location[0], other_location[1] - location[1])
            antinode_location = (location[0] + diff[0] * harmonic, location[1] + diff[1] * harmonic)
            if antinode_location[0] >= 0 and antinode_location[0] < width and antinode_location[1] >= 0 and antinode_location[1] < height:
              antinode_locations.add(antinode_location)
            else:
              break
  return antinode_locations

print(len(locate_antinodes(antenna_locations, width, height, [2])))
print(len(locate_antinodes(antenna_locations, width, height, range(10000))))
