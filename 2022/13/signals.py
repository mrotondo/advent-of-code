import ast
from enum import Enum

class Comparison(Enum):
  CORRECT = 1
  UNKNOWN = 2
  INCORRECT = 3

def compare(left, right):
  print(f'Compare {left} vs {right}')
  while len(left) > 0 and len(right) > 0:
    if isinstance(left[0], int) and isinstance(right[0], int):
      # print(f'both ints!')
      if left[0] < right[0]:
        # print(f'returning correct')
        return Comparison.CORRECT
      elif left[0] > right[0]:
        # print(f'returning incorrect')
        return Comparison.INCORRECT
    elif isinstance(left[0], list) and isinstance(right[0], list):
      # print(f'both lists!')
      sublist_comparison = compare(left[0], right[0])
      if sublist_comparison != Comparison.UNKNOWN:
        return sublist_comparison
    else:
      if isinstance(left[0], int):
        # print(f'left int!')
        sublist_comparison = compare([left[0]], right[0])
        if sublist_comparison != Comparison.UNKNOWN:
          return sublist_comparison
      elif isinstance(right[0], int):
        # print(f'right int!')
        sublist_comparison = compare(left[0], [right[0]])
        if sublist_comparison != Comparison.UNKNOWN:
          return sublist_comparison
    left.pop(0)
    right.pop(0)
  if len(left) > 0:
    print(f'right list ended first - returning incorrect')
    return Comparison.INCORRECT
  else:
    print(f'left list ended first - returning unknown')
    return Comparison.UNKNOWN


f = open('input.txt')

lines = f.readlines()
lists = list(map(ast.literal_eval, map(str.strip, [line for line in lines if line != '\n'])))
pairs = zip(lists[::2], lists[1::2])
results = list(map(lambda pair: compare(pair[0], pair[1]), pairs))

print(results)

correct_indices = [i + 1 for i in range(len(results)) if results[i] == Comparison.CORRECT or results[i] == Comparison.UNKNOWN]

print(sum(correct_indices))