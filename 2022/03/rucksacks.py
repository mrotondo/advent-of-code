def priority(item):
  priority = ord(item) - 96
  if priority < 0:
    priority += 58
  return priority

f = open('input.txt')
total_priority = 0
for line in f:
  num_items = len(line)//2
  compartments = line[:num_items], line[num_items:]
  shared = set.intersection(*map(set, compartments)).pop()
  total_priority += priority(shared)

print(total_priority)

total_badge_priority = 0
f.seek(0)
lines = f.readlines()
num_groups = len(lines)//3
for i in range(num_groups):
  group = map(set, map(str.strip, lines[i*3:i*3+3]))
  badge = set.intersection(*group).pop()
  total_badge_priority += priority(badge)

print(total_badge_priority)