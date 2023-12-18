f = open('input.txt')

def find_reflection(pattern):
  num_differences_target = 0
  #part 2
  num_differences_target = 1
  # try to find a vertical reflection
  for reflection_col_i in range(1, len(pattern[0])):
    # reflection_col_i is the first col after the possible reflection line
    num_differences = 0
    for check_col_i in range(0, reflection_col_i):
      low_check_col_i = reflection_col_i - check_col_i - 1
      high_check_col_i = reflection_col_i + check_col_i
      if low_check_col_i < 0 or high_check_col_i >= len(pattern[0]):
        break
      low_col = [row[low_check_col_i] for row in pattern]
      high_col = [row[high_check_col_i] for row in pattern]
      num_differences += sum([1 if low_col[i] != high_col[i] else 0 for i in range(len(pattern))])
    if num_differences == num_differences_target:
      return (reflection_col_i, 'vertical')
  # try to find a horizontal reflection
  for reflection_row_i in range(1, len(pattern)):
    # reflection_row_i is the first row after the possible reflection line
    num_differences = 0
    for check_row_i in range(0, reflection_row_i):
      low_check_row_i = reflection_row_i - check_row_i - 1
      high_check_row_i = reflection_row_i + check_row_i
      if low_check_row_i < 0 or high_check_row_i >= len(pattern):
        break
      low_row = pattern[low_check_row_i]
      high_row = pattern[high_check_row_i]
      num_differences += sum([1 if low_row[i] != high_row[i] else 0 for i in range(len(pattern[0]))])
    if num_differences == num_differences_target:
      return (reflection_row_i, 'horizontal')

total = 0
pattern = []
for line in f.readlines():
  if len(line.strip()) == 0:
    reflection_info = find_reflection(pattern)
    total += reflection_info[0] if reflection_info[1] == 'vertical' else reflection_info[0] * 100
    pattern = []
  else:
    pattern.append(line.strip())

print(total)