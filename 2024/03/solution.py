import re
f = open('input.txt')
text = f.read()

mul_command_regex = re.compile("mul\(([0-9]{0,3}),([0-9]{0,3})\)")

matches = re.findall(mul_command_regex, text)

print(sum([int(x) * int(y) for [x, y] in matches]))

do_regex = re.compile("(do\(\))")
dont_regex = re.compile("(don\'t\(\))")

combo_regex = re.compile("(?:{}|{}|{})".format(mul_command_regex.pattern, do_regex.pattern, dont_regex.pattern))

do_mul = True
total = 0
for match in re.finditer(combo_regex, text):
  if match[0] == "do()":
    do_mul = True
  elif match[0] == "don't()":
    do_mul = False
  else:
    x, y = match.groups()[0:2]
    if do_mul:
      total += int(x) * int(y)

print(total)