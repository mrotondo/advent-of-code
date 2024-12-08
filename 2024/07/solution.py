import re

f = open('input.txt')
lines = f.readlines()
equations = [list(map(int, re.findall(r"\d+", line))) for line in lines]

def try_operators(goal, operands, operators):
  if len(operands) == 1:
    if operands[0] == goal:
      return 1
    else:
      return 0
  
  num_successes = 0
  for operator in operators:
    operand_1 = operands[0]
    operand_2 = operands[1]
    result = operator(operand_1, operand_2)
    num_successes += try_operators(goal, [result] + operands[2:], operators)
  return num_successes

def plus(a, b):
  return a + b

def multiply(a, b):
  return a * b

def concat(a, b):
  return int(str(a) + str(b))

total = 0
for equation in equations:
  if try_operators(equation[0], equation[1:], [plus, multiply]) > 0:
    total += equation[0]
print(total)

total = 0
for equation in equations:
  if try_operators(equation[0], equation[1:], [plus, multiply, concat]) > 0:
    total += equation[0]
print(total)