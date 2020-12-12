import math

def read_instructions(s):
  ls = [l for l in s.split('\n') if l]
  return list(map(lambda l: (l[0], int(l[1:])), ls))

def north(amount, pos, waypoint):
  return (pos, (waypoint[0], waypoint[1] + amount))

def south(amount, pos, waypoint):
  return (pos, (waypoint[0], waypoint[1] - amount))

def east(amount, pos, waypoint):
  return (pos, (waypoint[0] + amount, waypoint[1]))

def west(amount, pos, waypoint):
  return (pos, (waypoint[0] - amount, waypoint[1]))

def rotate(vec, amount):
  angle = math.degrees(math.atan2(vec[1], vec[0]))
  mag = math.sqrt(math.pow(vec[0], 2) + math.pow(vec[1], 2))
  new_angle = angle + amount
  return (math.cos(math.radians(new_angle)) * mag, math.sin(math.radians(new_angle)) * mag)

def left(amount, pos, waypoint):
  return (pos, rotate(waypoint, amount))

def right(amount, pos, waypoint):
  return (pos, rotate(waypoint, -amount))

def forward(amount, pos, waypoint):
  return ((pos[0] + waypoint[0] * amount, pos[1] + waypoint[1] * amount), waypoint)

def do_instruction(instruction, pos, waypoint):
  actions = {
    'N': north,
    'S': south,
    'E': east,
    'W': west,
    'L': left,
    'R': right,
    'F': forward
  }

  return actions[instruction[0]](instruction[1], pos, waypoint)

f = open('input.txt')
instructions = read_instructions(f.read())
print(instructions)

pos = (0, 0)
waypoint = (10, 1)
for instruction in instructions:
  (pos, waypoint) = do_instruction(instruction, pos, waypoint)
  print((pos, waypoint))

print((pos, waypoint))

print(abs(pos[0]) + abs(pos[1]))
