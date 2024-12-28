import re
import math

def cheapest_combination(a_vector, b_vector, prize_coords):
  combinations = []
  for a_presses in range(101):
    for b_presses in range(101):
      if a_vector[0] * a_presses + b_vector[0] * b_presses == prize_coords[0] and a_vector[1] * a_presses + b_vector[1] * b_presses == prize_coords[1]:
        combinations.append((a_presses, b_presses))
  costs = [a_presses * 3 + b_presses for a_presses, b_presses in combinations]
  if len(costs) > 0:
    return min(costs)
  else:
    return 0

input_file = open('input.txt')

total = 0
while True:
  try:
    a_vector = list(map(int, re.match(r'Button A: X\+([0-9]+), Y\+([0-9]+)', input_file.readline()).groups()))
    b_vector = list(map(int, re.match(r'Button B: X\+([0-9]+), Y\+([0-9]+)', input_file.readline()).groups()))
    prize_coords = list(map(int, re.match(r'Prize: X=(\d+), Y=(\d+)\n', input_file.readline()).groups()))
    input_file.readline()
    total += cheapest_combination(a_vector, b_vector, prize_coords)
  except Exception as e:
    print(e)
    break

print(total)