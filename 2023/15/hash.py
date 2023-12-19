import re
from collections import defaultdict

def hash(string):
  value = 0
  for char in string:
    value += ord(char)
    value *= 17
    value %= 256
  return value

f = open('input.txt')
line = f.readline().strip()
commands = line.split(",")

INSERT = 'insert'
REMOVE = 'remove'

boxes = defaultdict(list)
for command in commands:
  command_type = INSERT if '=' in command else REMOVE
  label = re.search(r'[a-z]+', command).group()
  focal_length = int(re.search(r'\d+', command).group()) if command_type == INSERT else None
  box_number = hash(label)
  if command_type == INSERT:
    box = boxes[box_number]
    found_label = False
    for i in range(len(box)):
      if box[i][0] == label:
        box[i] = (label, focal_length)
        found_label = True
        break
    if not found_label:
      box.append((label, focal_length))
  else:
    box = boxes[box_number]
    index_to_remove = -1
    for i in range(len(box)):
      if box[i][0] == label:
        index_to_remove = i
        break
    if index_to_remove >= 0:
      boxes[box_number] = box[:index_to_remove] + box[index_to_remove + 1:]

total = 0
for box_i, box in boxes.items():
  for lens_i, (label, focal_length) in enumerate(box):
    total += (box_i + 1) * (lens_i + 1) * focal_length

print(total)