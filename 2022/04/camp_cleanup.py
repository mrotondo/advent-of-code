def parse_assignment(assignment_string):
  a,b = assignment_string.split('-')
  return int(a), int(b)

def subsumes(t1, t2):
  return t1[0] <= t2[0] and t1[1] >= t2[1]

def spans_min(t1, t2):
  return t1[0] <= t2[0] and t1[1] >= t2[0]

f = open('input.txt')

total_subsumptions = 0
total_overlaps = 0
for line in f:
  assignments = list(map(parse_assignment, line.strip().split(',')))
  if subsumes(*assignments) or subsumes(*assignments[::-1]):
    total_subsumptions += 1
  if spans_min(*assignments) or spans_min(*assignments[::-1]):
    total_overlaps += 1

print(total_subsumptions)
print(total_overlaps)