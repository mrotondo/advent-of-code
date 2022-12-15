import sys

f = open('input.txt')

walls = []
min_x = sys.maxsize
min_y = sys.maxsize
max_x = 0
max_y = 0
for line in f:
    point_strings = line.split(' -> ')
    points = list(map(lambda s: tuple(map(int, s.split(','))), point_strings))
    for point in points:
        min_x = min(min_x, point[0])
        max_x = max(max_x, point[0])
        min_y = min(min_y, point[1])
        max_y = max(max_y, point[1])
    pairs = zip(points, points[1:])
    walls.extend(pairs)

source = (500, 0)
min_x = min(min_x, source[0])
max_x = max(max_x, source[0])
min_y = min(min_y, source[1])
max_y = max(max_y, source[1])

# part 1: allow room for sand to fall past outermost wall pixels
min_x -= 1
max_x += 1

# part 2: floor
# min_x -= 200
# max_x += 200
# walls.append([(min_x, max_y + 2), (max_x, max_y + 2)])
# max_y += 2

w = max_x - min_x + 1
h = max_y - min_y + 1
map = [['.' for _ in range(w)] for _ in range(h)]

for wall in walls:
    a = wall[0]
    b = wall[1]
    x_diff = b[0] - a[0]
    y_diff = b[1] - a[1]
    dist = max(abs(x_diff), abs(y_diff))
    x_inc = x_diff // abs(x_diff) if x_diff != 0 else 0
    y_inc = y_diff // abs(y_diff) if y_diff != 0 else 0
    x_start = a[0] - min_x
    y_start = a[1] - min_y
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
    result = drop_sand(map, (source[0] - min_x, source[1] - min_y))
    if not result[1]:
        break
    num_at_rest += 1

# print(f'bounds:{min_x}, {min_y} - {max_x}, {max_y}')
# for row in map:
#     print(row)
print(num_at_rest)
