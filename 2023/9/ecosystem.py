import re
from math import lcm 

def get_deltas(values):
  return [b - a for (a, b) in zip(values, values[1:])]

def extrapolate(history):
  if all([x == 0 for x in history]):
    return history + [0]
  else:
    deltas = extrapolate(get_deltas(history))
    return history + [history[-1] + deltas[-1]]

def prextrapolate(history):
  if all([x == 0 for x in history]):
    return [0] + history
  else:
    deltas = prextrapolate(get_deltas(history))
    return [history[0] - deltas[0]] + history

f = open('input.txt')
last_values_sum = 0
first_values_sum = 0
for line in f.readlines():
  history = list(map(int, re.findall(r'-?\d+', line)))
  last_values_sum += extrapolate(history)[-1]
  first_values_sum += prextrapolate(history)[0]
print(last_values_sum)
print(first_values_sum)