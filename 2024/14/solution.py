import numpy as np
import re
from math import lcm 

robot_regex = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'

for i in range(10000):
  robot_count = {}
  grid_size = np.array([101, 103])
  sim_time = i
  for line in open('input.txt').readlines():
    p_x, p_y, v_x, v_y = map(int, re.match(robot_regex, line).groups())
    p = np.array([p_x, p_y])
    v = np.array([v_x, v_y])
    final_p = tuple((p + v * sim_time) % grid_size)
    robot_count[final_p] = robot_count.setdefault(final_p, 0) + 1

  middle_column = int(grid_size[0] / 2)
  middle_row = int(grid_size[1] / 2)
  nw_count = sum([count for p, count in robot_count.items() if p[0] < middle_column and p[1] < middle_row])
  ne_count = sum([count for p, count in robot_count.items() if p[0] > middle_column and p[1] < middle_row])
  sw_count = sum([count for p, count in robot_count.items() if p[0] < middle_column and p[1] > middle_row])
  se_count = sum([count for p, count in robot_count.items() if p[0] > middle_column and p[1] > middle_row])
  # print(nw_count * ne_count * sw_count * se_count)

  # if (middle_column, middle_row) in robot_count and \
  #   (middle_column - 1, middle_row - 1) in robot_count and \
  #   (middle_column - 1, middle_row + 1) in robot_count and \
  #   (middle_column + 1, middle_row - 1) in robot_count and \
  #   (middle_column + 1, middle_row + 1) in robot_count:
  if (i - 2) % 101 == 0:
    print("sim time is {}".format(i))
    for y in range(grid_size[1]):
      for x in range(grid_size[0]):
        if (x, y) in robot_count:
          print("#", end="", flush=False)
        else:
          print(".", end="", flush=False)
      print("", flush=False)
    print("", flush=True)
