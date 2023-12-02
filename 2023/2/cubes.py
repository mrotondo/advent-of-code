import re
from math import prod

f = open('input.txt')
lines = f.readlines()

def sample_string_to_amounts(sample_string):
  color_amount_tuples = re.findall(r'(\d+) ([a-z]+)', sample_string)
  return dict((color, int(amount)) for (amount, color) in color_amount_tuples)
  
def check_amounts(amounts, maxes):
  return [amount > maxes[color] for (color, amount) in amounts.items()]

def flatten(list_of_lists):
  return [x for sublist in list_of_lists for x in sublist]

def amounts_to_min_possible(sample_amounts):
  mins = {}
  for amounts in sample_amounts:
    for key, value in amounts.items():
      mins[key] = max(value, mins.setdefault(key, 0))
  return mins

def power(amounts):
  return prod(amounts.values())

sum_1 = 0
sum_2 = 0
maxes = {'red': 12, 'green': 13, 'blue': 14}
for line in lines:
  matches = re.search(r'Game (\d+): (.*)', line)
  id = int(matches.groups()[0])
  samples = matches.groups()[1].split(';')
  sample_amounts = list(map(sample_string_to_amounts, samples))
  more_than_maxes = flatten(map(lambda amounts: check_amounts(amounts, maxes), sample_amounts))
  min_possible = amounts_to_min_possible(sample_amounts)
  sum_2 += power(min_possible)
  if not any(more_than_maxes):
    sum_1 += id
  
print(sum_1)
print(sum_2)
