import sys

f = open('input.txt')


def adjust_bounds(bounds, point):
    bounds[0][0] = min(bounds[0][0], point[0])
    bounds[0][1] = max(bounds[0][1], point[0])
    bounds[1][0] = min(bounds[1][0], point[1])
    bounds[1][1] = max(bounds[1][1], point[1])


walls = []
bounds = [[sys.maxsize, 0], [sys.maxsize, 0]]
for line in f:
    point_strings = line.split(' -> ')
    points = list(map(lambda s: tuple(map(int, s.split(','))), point_strings))
    for point in points:
        adjust_bounds(bounds, point)
    pairs = zip(points, points[1:])
    walls.extend(pairs)

source = (500, 0)
adjust_bounds(bounds, source)

# part 1: allow room for sand to fall past outermost wall pixels
bounds[0][0] -= 1
bounds[0][1] += 1

# part 2: floor
# min_x -= 200
# max_x += 200
# walls.append([(min_x, max_y + 2), (max_x, max_y + 2)])
# max_y += 2

w = bounds[0][1] - bounds[0][0] + 1
h = bounds[1][1] - bounds[1][0] + 1
map = [['.' for _ in range(w)] for _ in range(h)]

for wall in walls:
    a = wall[0]
    b = wall[1]
    x_diff = b[0] - a[0]
    y_diff = b[1] - a[1]
    dist = max(abs(x_diff), abs(y_diff))
    x_inc = x_diff // abs(x_diff) if x_diff != 0 else 0
    y_inc = y_diff // abs(y_diff) if y_diff != 0 else 0
    x_start = a[0] - bounds[0][0]
    y_start = a[1] - bounds[1][0]
    x = x_start
    y = y_start
    for i in range(dist + 1):
        map[y][x] = '#'
        x += x_inc
        y += y_inc


def drop_sand(map, source):
    # part 2 source obscured check
    if map[source[1]][source[0]] == 'o':
        return (source, False)

    h = len(map)
    pos = source
    prev_pos = None
    while prev_pos != pos:
        prev_pos = pos
        if map[pos[1] + 1][pos[0]] == '.':
            pos = (pos[0], pos[1] + 1)
        elif map[pos[1] + 1][pos[0] - 1] == '.':
            pos = (pos[0] - 1, pos[1] + 1)
        elif map[pos[1] + 1][pos[0] + 1] == '.':
            pos = (pos[0] + 1, pos[1] + 1)
        if pos[1] == h - 1:
            return (pos, False)

    map[pos[1]][pos[0]] = 'o'
    return (pos, True)


num_at_rest = 0
while True:
    result = drop_sand(
        map, (source[0] - bounds[0][0], source[1] - bounds[1][0]))
    if not result[1]:
        break
    num_at_rest += 1

# print(f'bounds:{min_x}, {min_y} - {max_x}, {max_y}')
# for row in map:
#     print(row)
print(num_at_rest)
