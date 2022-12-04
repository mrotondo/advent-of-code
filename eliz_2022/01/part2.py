f = open('eliz_input.txt')
lines = f.readlines()

largest_total = 0
second_largest_total = 0
third_largest_total = 0

current_total = 0
for line in lines:
  if line == '\n':
    if current_total > largest_total:
      third_largest_total = second_largest_total
      second_largest_total = largest_total
      largest_total = current_total
    elif current_total > second_largest_total:
      third_largest_total = second_largest_total
      second_largest_total = current_total
    elif current_total > third_largest_total:
      third_largest_total = current_total
    current_total = 0
  else:
    calories = int(line)
    current_total = calories + current_total

print(largest_total + second_largest_total + third_largest_total)