import re
import sys

def monkey_eval(monkeys, name):
  # print(f'evaluating monkey {name}, it yells {monkeys[name]}')
  if isinstance(monkeys[name], int):
    return monkeys[name]
  else:
    op, a, b = monkeys[name]
    expression = f'{monkey_eval(monkeys, a)} {op} {monkey_eval(monkeys, b)}'
    if op == '==':
      print(f'evaluating expr: {expression}')
    return int(eval(expression))

f = open('input.txt')
monkeys = {}
for line in f:
  if match := re.search(r'([a-z]+): ([a-z]+) ([+-/*]) ([a-z]+)', line):
    name, a, op, b = match.groups()
    monkeys[name] = (op, a, b)
  elif match := re.search(r'([a-z]+): (\d+)', line):
    name, n = match.groups()
    monkeys[name] = int(n)

print(monkey_eval(monkeys, 'root'))

op, a, b = monkeys['root']
monkeys['root'] = ('>', a, b)

lower = int(-(sys.maxsize / 2))
upper = int(sys.maxsize / 2)

while lower != upper - 1:
  print(f'lower: {lower}, upper: {upper}')
  monkeys['humn'] = lower
  f_lower = monkey_eval(monkeys, 'root')
  monkeys['humn'] = upper
  f_upper = monkey_eval(monkeys, 'root')
  mid = int(lower + (upper - lower) / 2)
  monkeys['humn'] = mid
  f_mid = monkey_eval(monkeys, 'root')

  if f_lower != f_mid:
    upper = mid
  else:
    lower = mid

op, a, b = monkeys['root']
monkeys['root'] = ('==', a, b)

monkeys['humn'] = mid
print(f'lower is {lower}, mid is {lower + 1}')
print(monkey_eval(monkeys, 'root'))
