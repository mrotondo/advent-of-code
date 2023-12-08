import re
from math import lcm 

f = open('input.txt')

instructions = f.readline().strip()
_ = f.readline()

connections = {}
for line in f.readlines():
  (room, left, right) = re.search(r'([0-9A-Z]{3}) = \(([0-9A-Z]{3}), ([0-9A-Z]{3})\)', line).groups()
  connections[room] = (left, right)

directions = {'L': 0, 'R': 1}

memo_steps = {}

# part 1
# current_room = 'AAA'
# steps = 0
# while current_room != 'ZZZ':
#   for instruction in instructions:
#     current_room = connections[current_room][directions[instruction]]
#     steps += 1
# print(steps)

# part 2
current_rooms = list(filter(lambda room: room.endswith('A'), connections.keys()))
all_steps = []
for current_room in current_rooms:
  steps = 0
  while not current_room.endswith('Z'):
    for instruction in instructions:
      current_room = connections[current_room][directions[instruction]]
      steps += 1
  all_steps.append(steps)
print(lcm(*all_steps))