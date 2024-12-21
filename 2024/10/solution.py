f = open('input.txt')
grid = [list(map(int, line.strip())) for line in f.readlines()]

height = len(grid)
width = len(grid[0])

reachable_peaks = {}
ratings = {}

total_trailhead_scores = 0
total_trailhead_ratings = 0

for i in range(9, -1, -1):
  for x in range(width):
    for y in range(height):
      elevation = grid[y][x]
      reachable_peaks_from_here = set()
      rating = 0
      if elevation == i:
        if elevation == 9:
          reachable_peaks_from_here = set([(x, y)])
          rating = 1
        else:
          for neighbor_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_x = x + neighbor_offset[0]
            neighbor_y = y + neighbor_offset[1]
            if neighbor_x >= 0 and neighbor_x < width and neighbor_y >= 0 and neighbor_y < height:
              neighbor_elevation = grid[neighbor_y][neighbor_x]
              if neighbor_elevation == elevation + 1:
                reachable_peaks_from_here = reachable_peaks_from_here.union(reachable_peaks[(neighbor_x, neighbor_y)])
                rating += ratings[(neighbor_x, neighbor_y)]
        reachable_peaks[(x, y)] = reachable_peaks_from_here
        ratings[(x, y)] = rating
        if elevation == 0:
          total_trailhead_scores += len(reachable_peaks_from_here)
          total_trailhead_ratings += rating

print(total_trailhead_scores)
print(total_trailhead_ratings)