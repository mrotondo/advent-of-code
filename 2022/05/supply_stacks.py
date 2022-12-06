import re
import copy

def execute_command(stacks, times, from_col, to_col):
  for _ in range(times):
    stacks[to_col].append(stacks[from_col].pop())

def execute_command_2(stacks, times, from_col, to_col):
  substack = []
  for _ in range(times):
    substack.append(stacks[from_col].pop())
  stacks[to_col].extend(substack[::-1])

f = open('input.txt')
line = f.readline().rstrip('\n')
num_stacks = (len(line) + 1) // 4
stacks = [list() for _ in range(num_stacks)]

while '[' in line:
  for stack_i in range(num_stacks):
    stack_item = line[stack_i * 4 + 1]
    if stack_item != ' ':
      stacks[stack_i].insert(0, stack_item)
  line = f.readline().rstrip('\n')

stacks_2 = copy.deepcopy(stacks)

# advance to commands
f.readline()

command_re = re.compile(r'move (\d*) from (\d*) to (\d*)')
for command_line in f:
  command_line = command_line.strip()
  times, from_col, to_col = command_re.search(command_line).groups()
  times, from_col, to_col = int(times), int(from_col) - 1, int(to_col) -1
  execute_command(stacks, times, from_col, to_col)
  execute_command_2(stacks_2, times, from_col, to_col)

tops_1 = ''.join([stack[-1] for stack in stacks])
print(tops_1)

tops_2 = ''.join([stack[-1] for stack in stacks_2])
print(tops_2)
