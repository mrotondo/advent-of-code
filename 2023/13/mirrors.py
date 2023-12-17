f = open('input.txt')

def find_reflection(pattern):
  # try to find a vertical reflection
  for reflection_col_i in range(1, len(pattern[0])):
    # reflection_col_i is the first row after the possible reflection line
    reflection_found = True
    for check_col_i in range(0, reflection_col_i):
      low_check_col_i = reflection_col_i - check_col_i - 1
      high_check_col_i = reflection_col_i + check_col_i
      if low_check_col_i < 0 or high_check_col_i >= len(pattern[0]):
        break
      if [row[low_check_col_i] for row in pattern] != [row[high_check_col_i] for row in pattern]:
        reflection_found = False
        break
    if reflection_found:
      return (reflection_col_i, 'vertical')
  # try to find a horizontal reflection
  for reflection_row_i in range(1, len(pattern)):
    # reflection_row_i is the first row after the possible reflection line
    reflection_found = True
    for check_row_i in range(0, reflection_row_i):
      low_check_row_i = reflection_row_i - check_row_i - 1
      high_check_row_i = reflection_row_i + check_row_i
      if low_check_row_i < 0 or high_check_row_i >= len(pattern):
        break
      if pattern[low_check_row_i] != pattern[high_check_row_i]:
        reflection_found = False
        break
    if reflection_found:
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