def priority(item):
  priority = ord(item) - 96
  if priority < 0:
    priority += 58
  return priority

f = open('input.txt')
lines = f.readlines()
total_priority = 0
for line in lines:
  line = line.strip()
  num_compartment_items = int(len(line)/2)
  compartments = [set(line[:num_compartment_items]), set(line[num_compartment_items:])]
  shared = compartments[0].intersection(compartments[1]).pop()
  total_priority += priority(shared)

print(total_priority)

total_badge_priority = 0
num_groups = int(len(lines)/3)
f.seek(0)
for i in range(num_groups):
  group = [f.readline().strip(), f.readline().strip(), f.readline().strip()]
  badge = set.intersection(*list(map(set,group))).pop()
  total_badge_priority += priority(badge)

print(total_badge_priority)