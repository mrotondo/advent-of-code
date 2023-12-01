import re

def number_word_to_int(word):
  try:
    return int(word)
  except ValueError:
    return ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'].index(word) + 1

def line_to_number(line):
  number_words = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  all_matches = []
  for word in number_words:
    all_matches.extend(list(re.finditer(word, line)))
  sorted_matches = sorted(all_matches, key=lambda match: match.start())
  return number_word_to_int(sorted_matches[0].group()) * 10 + number_word_to_int(sorted_matches[-1].group())
  
f = open('input.txt')
lines = f.readlines()
sum = 0
for line in lines:
  number = line_to_number(line)
  sum += number

print(sum)