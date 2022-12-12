from collections import deque

class Monkey:
  def __init__(self, start_items, op, test):
    self.items = deque(start_items)
    self.op = op
    self.test = test
    self.inspections = 0

monkeys = [
  Monkey([64], lambda x: x * 7, lambda x: 1 if x % 13 == 0 else 3),
  Monkey([60, 84, 84, 65], lambda x: x + 7, lambda x: 2 if x % 19 == 0 else 7),
  Monkey([52, 67, 74, 88, 51, 61], lambda x: x * 3, lambda x: 5 if x % 5 == 0 else 7),
  Monkey([67, 72], lambda x: x + 3, lambda x: 1 if x % 2 == 0 else 2),
  Monkey([80, 79, 58, 77, 68, 74, 98, 64], lambda x: x * x, lambda x: 6 if x % 17 == 0 else 0),
  Monkey([62, 53, 61, 89, 86], lambda x: x + 8, lambda x: 4 if x % 11 == 0 else 6),
  Monkey([86, 89, 82], lambda x: x + 2, lambda x: 3 if x % 7 == 0 else 0),
  Monkey([92, 81, 70, 96, 69, 84, 83], lambda x: x + 4, lambda x: 4 if x % 3 == 0 else 5)
]

# num_rounds = 20
num_rounds = 10_000
for _ in range(num_rounds):
  for monkey in monkeys:
    while len(monkey.items) > 0:
      monkey.inspections += 1
      worry = monkey.op(monkey.items.popleft())
      # worry //= 3
      worry %= 9_699_690
      target = monkey.test(worry)
      monkeys[target].items.append(worry)

active_monkeys = sorted([monkey.inspections for monkey in monkeys], reverse=True)
print(active_monkeys[0] * active_monkeys[1])