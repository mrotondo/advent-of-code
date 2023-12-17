import re

def count_possible_assignments(statuses, broken_group_sizes):
  # print('counting possible assignments with statuses {} and broken_group_sizes {}'.format(statuses, broken_group_sizes))
  if len(broken_group_sizes) == 0 and '#' not in statuses:
    # print('found a match with remaining statuses {} and broken_groups_sizes {}'.format(statuses, broken_group_sizes))
    return 1
  elif len(broken_group_sizes) == 0 or len(statuses) == 0:
    return 0
  elif statuses[0] == '.':
    # print('consuming dot')
    return count_possible_assignments(statuses[1:], broken_group_sizes)
  else:
    assignable_segment = re.match(r'^([\#\?]+).*', statuses).groups()[0]
    # print('assignable segment is {}'.format(assignable_segment))
    if len(assignable_segment) < broken_group_sizes[0]:
      if '#' in assignable_segment:
        return 0
      else:
        # print('skipping too-small assignable segment')
        return count_possible_assignments(statuses[len(assignable_segment):], broken_group_sizes)
    else:
      count_with_assignment = 0
      if len(statuses) == broken_group_sizes[0] or statuses[broken_group_sizes[0]] != '#':
        # print('trying with assignment')
        count_with_assignment = count_possible_assignments(statuses[broken_group_sizes[0] + 1:], broken_group_sizes[1:])
      count_without_assignment = 0
      if statuses[0] != '#':
        # print('trying without assignment')
        count_without_assignment = count_possible_assignments(statuses[1:], broken_group_sizes)
      return count_with_assignment + count_without_assignment

f = open('input.txt')
total_possible_assignments = 0
for line in f.readlines():
  statuses = re.search(r'[\?\.\#]+', line).group()
  broken_group_sizes = list(map(int, re.findall(r'\d+', line)))
  possible_assignments = count_possible_assignments(statuses, broken_group_sizes)
  # print(possible_assignments)
  total_possible_assignments += possible_assignments

print(total_possible_assignments)