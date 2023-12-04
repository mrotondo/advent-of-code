import re
from math import prod

f = open('input.txt')
lines = f.readlines()

total_points = 0

copies = {}

for line_index, line in enumerate(lines):
  (card_number_string, numbers_string) = line.split(':')
  (winning_numbers_string, numbers_i_have_string) = numbers_string.split('|')
  winning_numbers = set(map(int, re.findall(r'\d+', winning_numbers_string)))
  numbers_i_have = map(int, re.findall(r'\d+', numbers_i_have_string))
  points = 0
  matches = 0
  for number_i_have in numbers_i_have:
    if number_i_have in winning_numbers:
      points = points + 1 if points == 0 else points * 2
      matches += 1
  total_points += points
  num_copies_to_add = copies.setdefault(line_index, 1)
  for i in range(1, matches + 1):
    line_to_copy = line_index + i
    copies[line_to_copy] = copies.setdefault(line_to_copy, 1) + num_copies_to_add

print(total_points)

print(sum(copies.values()))