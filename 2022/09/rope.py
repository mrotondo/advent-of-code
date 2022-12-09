import re
from math import copysign

def vec2_add(v1, v2):
  return (v1[0] + v2[0], v1[1] + v2[1])

def vec2_abs_diff(v1, v2):
  return (abs(v1[0] - v2[0]), abs(v1[1] - v2[1]))

# Thanks https://stackoverflow.com/questions/22490366/how-to-use-cmp-in-python-3
def cmp(a, b):
    return (a > b) - (a < b) 

def move_tail(head, tail):
  x_diff = cmp(head[0] - tail[0], 0)
  y_diff = cmp(head[1] - tail[1], 0)
  return (tail[0] + x_diff, tail[1] + y_diff)

f = open('input.txt')

head = (0, 0)
tail = (0, 0)
tail_path = [tail]

moves = {'U': (0, 1), 'L': (-1, 0), 'D': (0, -1), 'R': (1, 0)}

for line in f:
  dir, times = re.search(r'([ULDR]) (\d+)', line).groups()
  times = int(times)
  for _ in range(times):
    head = vec2_add(head, moves[dir])
    diff = vec2_abs_diff(head, tail)
    if diff[0] > 1 or diff[1] > 1:
      tail = move_tail(head, tail)
      tail_path.append(tail)

print(len(set(tail_path)))

prev_rope = [(0,0)] * 10
tail_path = [prev_rope[-1]]
f.seek(0)
for line in f:
  dir, times = re.search(r'([ULDR]) (\d+)', line).groups()
  times = int(times)
  for _ in range(times):
    new_rope = [vec2_add(prev_rope[0], moves[dir])]
    for i in range(1, 10):
      knot = prev_rope[i]
      diff = vec2_abs_diff(new_rope[i-1], knot)
      if diff[0] > 1 or diff[1] > 1:
        knot = move_tail(new_rope[i-1], knot)
      new_rope.append(knot)
    tail_path.append(new_rope[-1])
    prev_rope = new_rope
  
print(len(set(tail_path)))