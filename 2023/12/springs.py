import re

memo = {}

def count_possible_assignments(statuses, broken_group_sizes):
  key = (statuses, tuple(broken_group_sizes))
  if key in memo:
    return memo[key]
  count = 0
  if len(broken_group_sizes) == 0 and '#' not in statuses:
    count = 1
  elif len(broken_group_sizes) == 0 or len(statuses) == 0:
    count = 0
  elif statuses[0] == '.':
    count = count_possible_assignments(statuses[1:], broken_group_sizes)
  else:
    assignable_segment = re.match(r'^([\#\?]+).*', statuses).groups()[0]
    if len(assignable_segment) < broken_group_sizes[0]:
      if '#' in assignable_segment:
        count = 0
      else:
        count = count_possible_assignments(statuses[len(assignable_segment):], broken_group_sizes)
    else:
      count_with_assignment = 0
      if len(statuses) == broken_group_sizes[0] or statuses[broken_group_sizes[0]] != '#':
        count_with_assignment = count_possible_assignments(statuses[broken_group_sizes[0] + 1:], broken_group_sizes[1:])
      count_without_assignment = 0
      if statuses[0] != '#':
        count_without_assignment = count_possible_assignments(statuses[1:], broken_group_sizes)
      count = count_with_assignment + count_without_assignment
  memo[key] = count
  return count

f = open('input.txt')
total_possible_assignments = 0
for line in f.readlines():
  statuses = re.search(r'[\?\.\#]+', line).group()
  broken_group_sizes = list(map(int, re.findall(r'\d+', line)))

  # part 2
  statuses = '?'.join([statuses] * 5)
  broken_group_sizes = broken_group_sizes * 5

  possible_assignments = count_possible_assignments(statuses, broken_group_sizes)
  total_possible_assignments += possible_assignments

print(total_possible_assignments)