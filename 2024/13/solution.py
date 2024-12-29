import re

def cheapest_combination(a_vector, b_vector, prize_coords):
  a = b_vector[1] / a_vector[1]
  b = b_vector[0] / a_vector[0]
  c = prize_coords[0] / a_vector[0]
  d = prize_coords[1] / a_vector[1]

  b_presses = round((d - c) / (a - b))
  a_presses = round((-b_presses * b_vector[0] + prize_coords[0]) / a_vector[0])
  if a_presses * a_vector[0] + b_presses * b_vector[0] == prize_coords[0] and a_presses * a_vector[1] + b_presses * b_vector[1] == prize_coords[1]:
    return round(a_presses) * 3 + round(b_presses)
  else:
    return 0

input_file = open('input.txt')

total = 0
while True:
  try:
    a_vector = list(map(int, re.match(r'Button A: X\+([0-9]+), Y\+([0-9]+)', input_file.readline()).groups()))
    b_vector = list(map(int, re.match(r'Button B: X\+([0-9]+), Y\+([0-9]+)', input_file.readline()).groups()))
    prize_coords = list(map(int, re.match(r'Prize: X=(\d+), Y=(\d+)\n', input_file.readline()).groups()))
    prize_coords = (prize_coords[0] + 10000000000000, prize_coords[1] + 10000000000000)
    input_file.readline()
    total += cheapest_combination(a_vector, b_vector, prize_coords)
  except Exception as e:
    print(e)
    break

print(total)