import math

transformations = {}

def num_digits(x):
  return math.floor(math.log10(x)) + 1

def split_in_half(x):
  length = num_digits(x)
  first_half = int(x / pow(10, length / 2))
  second_half = int(x - first_half * pow(10, length / 2))
  return [first_half, second_half]

def transform_one_step(stone):
  transformation = None
  if stone == 0:
    transformation = [1]
  elif num_digits(stone) % 2 == 0:
    transformation =  split_in_half(stone)
  else:
    transformation =  [stone * 2024]
  return transformation

def transform(stone, steps):
  if steps == 0:
    return 1
  elif (stone, steps) in transformations:
    return transformations[(stone, steps)]
  else:
    transformation = transform_one_step(stone)
    result = sum([transform(x, steps - 1) for x in transformation])
    transformations[(stone, steps)] = result
    return result

def flatten(xss):
  return [x for xs in xss for x in xs]

input_file = open('input.txt')
stones = list(map(int, input_file.read().strip().split(" ")))

stones = [(stone, 75) for stone in stones]

result = 0
for stone, steps in stones:
  result += transform(stone, steps)

print(result)