def is_valid(update, ordering_rules):
  for before, after in ordering_rules:
    if before in update and after in update:
      if update.index(before) > update.index(after):
        return False
  return True

def fix_invalid_pages(update, ordering_rules):
  made_changes = False
  for before, after in ordering_rules:
    if before in update and after in update:
      if update.index(before) > update.index(after):
        made_changes = True
        update.insert(update.index(after), update.pop(update.index(before)))
  return made_changes

f = open('input.txt')
lines = [line.strip() for line in f.readlines()]

ordering_rules = [list(map(int, line.split("|"))) for line in lines if "|" in line]

updates = [list(map(int, line.split(","))) for line in lines if "," in line]

total = 0
for update in updates:
  if is_valid(update, ordering_rules):
    total += update[int(len(update) / 2)]
print(total)

total = 0
for update in updates:
  if not is_valid(update, ordering_rules):
    made_changes = fix_invalid_pages(update, ordering_rules)
    while made_changes:
      made_changes = fix_invalid_pages(update, ordering_rules)
    total += update[int(len(update) / 2)]
print(total)
