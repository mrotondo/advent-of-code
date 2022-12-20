class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None
    self.moved = False

  def __repr__(self):
    return str(self.value)

  def next(self):
    return self.next

  def prev(self):
    return self.prev

  def pop(self):
    self.prev.next = self.next
    self.next.prev = self.prev
    self.next = None
    self.prev = None
  
  def insert_after(self, other):
    # print(f'inserting {self.value} between {other.value} and {other.next.value}')
    # print(f'other.next is {other.next}')
    self.next = other.next
    self.next.prev = self
    self.prev = other
    other.next = self

def print_nodes(start):
  print(start)
  cur = start.next
  while cur != start:
    print(cur)
    cur = cur.next

# key = 1
key = 811589153
f = open('test_input.txt')
nodes = []
for line in f:
  i = int(line.strip())
  nodes.append(Node(i * key))

for i in range(len(nodes)):
  nodes[i].next = nodes[(i+1) % len(nodes)]
  nodes[i].prev = nodes[(i-1) % len(nodes)]


start_node = nodes[0]
zero_node = start_node
while zero_node.value != 0:
  zero_node = zero_node.next

print('here we go')
print_nodes(zero_node)
print('done')

for i in range(1, 11):
  current_node = start_node
  next_to_move = start_node
  num_moved = 0
  while num_moved < len(nodes):
    next_to_move = current_node.next
    if not current_node.moved:
      to_move = current_node.value
      to_move %= len(nodes) - 1
      move_dir = 1
      move_func = Node.next
      if to_move < 0:
        move_func = Node.prev
        move_dir = -1
      target_node = current_node.prev
      current_node.pop()
      for _ in range(0, to_move, move_dir):
        target_node = move_func(target_node)
      # print(f'trying to insert {current_node} after {target_node}')
      if target_node != current_node:
        current_node.insert_after(target_node)
        current_node.moved = True
      num_moved += 1

    current_node = next_to_move
  
  print(f'after {i} rounds of mixing...')
  print_nodes(zero_node)
  print('---')
  for node in nodes:
    node.moved = False

current_node = zero_node
checks = [1000, 2000, 3000]
sum = 0
for i in range(1, 3001):
  current_node = current_node.next
  if i in checks:
    print(f'i is {i}, adding {current_node.value}')
    sum += current_node.value
print(sum)

