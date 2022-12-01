import re

def parse_rules(rule_lines):
  rules = {}
  for rule_line in rule_lines:
    rule_name = re.search(r'(.*):', rule_line).groups()[0]
    rule_range_strings = re.findall(r'(\d*)-(\d*)', rule_line)
    rule_ranges = [range(int(a), int(b) + 1) for (a, b) in rule_range_strings]
    rules[rule_name] = rule_ranges
  return rules

def parse_ticket(ticket_line):
  return list(map(int, ticket_line.split(',')))

def possible_fields_for_value(value, rules):
  possible_fields = set()
  for (rule_name, rule) in rules.items():
    valid = False
    for range in rule:
      if value in range:
        valid = True
    if valid:
      possible_fields.add(rule_name)
  return possible_fields

def check_ticket1(ticket, rules):
  for value in ticket:
    possible_fields = possible_fields_for_value(value, rules)
    if len(possible_fields) == 0:
      return (False, value)
  return (True, 0)

f = open('input.txt')
ls = f.read()
chunks = ls.split('\n\n')
rule_lines = [l for l in chunks[0].split('\n') if len(l) > 0]
my_ticket_line = chunks[1].split('\n')[1]
nearby_ticket_lines = [l for l in chunks[2].split('\n')[1:] if len(l) > 0]

rules = parse_rules(rule_lines)
my_ticket = parse_ticket(my_ticket_line)
nearby_tickets = list(map(parse_ticket, nearby_ticket_lines))

bad_val_sum = 0
possible_fields = [set(rules) for i in range(len(my_ticket))]
for ticket in nearby_tickets:
  (good_ticket, bad_val) = check_ticket1(ticket, rules)
  if not good_ticket:
    bad_val_sum += bad_val
  else:
    for i in range(len(ticket)):
      possible_fields[i] = set.intersection(possible_fields[i], possible_fields_for_value(ticket[i], rules))
for smallest_possible_field_set in sorted(possible_fields, key=len):
  for possible_field_set in possible_fields:
    if possible_field_set is not smallest_possible_field_set:
      possible_field_set.difference_update(smallest_possible_field_set)

print(bad_val_sum)
fields = map(lambda s: list(s)[0], possible_fields)
product = 1
for i in range(len(my_ticket)):
  if fields[i].startswith('departure'):
    product *= my_ticket[i]
print(product)