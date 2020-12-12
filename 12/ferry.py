import math

def read_instructions(s):
  ls = [l for l in s.split('\n') if l]
  return list(map(lambda l: (l[0], int(l[1:])), ls))

def do_instruction(instruction, orientation):
  actions = {
    'N': lambda amount, xya: (xya[0], xya[1] + amount, xya[2]),
    'S': lambda amount, xya: (xya[0], xya[1] - amount, xya[2]),
    'E': lambda amount, xya: (xya[0] + amount, xya[1], xya[2]),
    'W': lambda amount, xya: (xya[0] - amount, xya[1], xya[2]),
    'L': lambda amount, xya: (xya[0], xya[1], xya[2] + amount),
    'R': lambda amount, xya: (xya[0], xya[1], xya[2] - amount),
    'F': lambda amount, xya: (xya[0] + math.cos(math.radians(xya[2])) * amount, xya[1] + math.sin(math.radians(xya[2])) * amount, xya[2])
  }
  return actions[instruction[0]](instruction[1], current)

f = open('input.txt')
instructions = read_instructions(f.read())
print(instructions)

current = (0, 0, 0)
for instruction in instructions:
  current = do_instruction(instruction, current)
  print(current)

print(current)

print(abs(current[0]) + abs(current[1]))
