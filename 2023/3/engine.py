import re
from math import prod

f = open('input.txt')
lines = f.readlines()

components = {}
for line_index, line in enumerate(lines):
  component_matches = re.finditer(r'[^0-9\.\n]', line)
  for component_match in component_matches:
    components[(line_index, component_match.start())] = {'component': component_match.group(), 'numbers': []}
  
f.seek(0)
lines = f.readlines()
sum_1 = 0
for line_index, line in enumerate(lines):
  number_matches = re.finditer(r'[0-9]+', line)
  for number_match in number_matches:
    next_to_component = False
    for component_line_index in range(line_index - 1, line_index + 2):
      for component_char_index in range(number_match.start() - 1, number_match.end() + 1):
        component_key = (component_line_index, component_char_index)
        if component_key in components:
          next_to_component = True
          components[component_key]['numbers'].append(int(number_match.group()))
    if next_to_component:
      sum_1 += int(number_match.group())

print(sum_1)

sum_2 = 0
for component in components.values():
  if component['component'] == '*' and len(component['numbers']) == 2:
    sum_2 += prod(component['numbers'])

print(sum_2)
