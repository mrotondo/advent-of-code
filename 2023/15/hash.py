import re

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

total = 0
for command in commands:
  total += hash(command)

print(total)