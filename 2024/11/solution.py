import math

def num_digits(x):
  return math.floor(math.log10(x)) + 1

def split_in_half(x):
  length = num_digits(x)
  first_half = int(x / pow(10, length / 2))
  second_half = int(x - first_half * pow(10, length / 2))
  return [first_half, second_half]

def transform(stone):
  if stone == 0:
    return [1]
  elif num_digits(stone) % 2 == 0:
    return split_in_half(stone)
  else:
    return [stone * 2024]

def flatten(xss):
  return [x for xs in xss for x in xs]

def blink(stones):
  return flatten([transform(stone) for stone in stones])

input_file = open('input.txt')
stones = list(map(int, input_file.read().strip().split(" ")))

for i in range(25):
  stones = blink(stones)

print(len(stones))