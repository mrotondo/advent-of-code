import sys

def binary_search(bisections, low_key, high_key, min, max):
    if (min == max):
        return min
    bisection = bisections[0]
    half_range = (max - min) // 2 + 1
    if (bisection == low_key):
        return binary_search(bisections[1:], low_key, high_key, min, max - half_range)
    elif (bisection == high_key):
        return binary_search(bisections[1:], low_key, high_key, min + half_range, max)

f = open('input.txt')
lines = f.readlines()
seat_ids = set()
for line in lines:
    row = binary_search(line[:7], 'F', 'B', 0, 127)
    seat = binary_search(line[7:], 'L', 'R', 0, 7)
    seat_id = row * 8 + seat
    seat_ids.add(seat_id)
print(max(seat_ids))
for i in seat_ids:
    if (i+1 not in seat_ids and i+2 in seat_ids):
        print(i+1)