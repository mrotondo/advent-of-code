f = open('input.txt')
lines = f.readlines()

def check_increasing(differences):
  return [difference > 0 for difference in differences]

def check_decreasing(differences):
  return [difference < 0 for difference in differences]

def check_in_range(differences):
  return [abs(difference) >= 1 and abs(difference) <= 3 for difference in differences]

def is_safe(report):
  differences = [y - x for [x, y] in zip(report, report[1:])]
  same_direction = all(check_increasing(differences)) or all(check_decreasing(differences))
  all_in_range = all(check_in_range(differences))
  return same_direction and all_in_range

def is_damped_safe(report):
  return is_safe(report) or any([is_safe(report[0:i] + report[i+1:len(report)]) for i in range(len(report))])

reports = [list(map(int, line.strip().split())) for line in lines]

safety = [is_safe(report) for report in reports]
print(safety.count(True))

damped_safety = [is_damped_safe(report) for report in reports]
print(damped_safety.count(True))