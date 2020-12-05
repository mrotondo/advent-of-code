import sys

def binary_search(bisections, low_key, high_key, row_min, row_max):
    if (row_min == row_max):
        return row_min
    bisection = bisections[0]
    if (bisection == low_key):
        return binary_search(bisections[1:], low_key, high_key, 
                        row_min,
                        row_max - (row_max - row_min) / 2 - 1)
    elif (bisection == high_key):
        return binary_search(bisections[1:], low_key, high_key,
                        row_min + (row_max - row_min) / 2 + 1,
                        row_max)

f = open('input.txt')
lines = f.readlines()
max_seat_id = 0
min_seat_id = sys.maxsize
seat_ids = set()
for line in lines:
    row = binary_search(line[:7], 'F', 'B', 0, 127)
    seat = binary_search(line[7:], 'L', 'R', 0, 7)
    seat_id = row * 8 + seat
    if (seat_id > max_seat_id):
        max_seat_id = seat_id
    if (seat_id < min_seat_id):
        min_seat_id = seat_id
    seat_ids.add(seat_id)
print(max_seat_id)
for i in range(min_seat_id, max_seat_id):
    if (i not in seat_ids):
        print(i)