f = open('input.txt')
lines = [line.strip() for line in f.readlines()]

ordering_rules = [list(map(int, line.split("|"))) for line in lines if "|" in line]

updates = [list(map(int, line.split(","))) for line in lines if "," in line]

total = 0
for update in updates:
  valid = True
  for before, after in ordering_rules:
    if before in update and after in update:
      if update.index(before) > update.index(after):
        valid = False
  if valid:
    total += update[int(len(update) / 2)]
print(total)

