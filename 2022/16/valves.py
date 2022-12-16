import re

line_re = re.compile('^Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)$')

f = open('input.txt')
valves = {}
for line in f:
  valve, rate, dests = line_re.match(line.strip()).groups()
  rate = int(rate)
  dests = dests.split(', ')
  open_valve_name = valve.lower()
  valves[valve] = {'rate': 0, 'dests': dests + [open_valve_name]}
  valves[open_valve_name] = {'rate': rate, 'dests': dests}

# part 1
# def search(valves, paths, path, minutes_left, depth):
#   dests = valves[path[-2:]]['dests']
#   score_so_far = paths[path]
#   if depth == 0:
#     return
#   for dest in dests:
#     if not (dest.islower() and dest in path):  # make sure we don't open the same valve twice
#       new_path = path + dest
#       if new_path not in paths:
#         rate_at_dest = valves[dest]['rate']
#         new_score = score_so_far + rate_at_dest * (minutes_left - 1)
#         paths[new_path] = new_score
#         search(valves, paths, new_path, minutes_left - 1, depth - 1)

# path_start = 'AA'
# minutes_left = 30
# minute_increments = 1
# num_paths_to_continue = 2000  # arbitrary and bound to fail me somehow
# paths = {path_start: 0}

# while minutes_left > 0:
#   depth = min(minute_increments, minutes_left)
#   best_paths = sorted(paths, key=paths.get, reverse=True)[:num_paths_to_continue]
#   paths = {path: paths[path] for path in best_paths}
#   for path in list(paths.keys()):
#     search(valves, paths, path, minutes_left, depth)
#   minutes_left -= minute_increments
  
# best_paths = sorted(paths, key=paths.get, reverse=True)[:num_paths_to_continue]
# print(paths[best_paths[0]])

# part 2
def search_2(valves, paths, path, minutes_left, depth):
  if depth == 0:
    return
  my_path = path[0]
  elephant_path = path[1]
  my_dests = valves[my_path[-2:]]['dests']
  elephant_dests = valves[elephant_path[-2:]]['dests']
  score_so_far = paths[path]
  for my_dest in my_dests:
    for elephant_dest in elephant_dests:
      my_dest_is_open_and_in_either_path = my_dest.islower() and (my_dest in my_path or my_dest in elephant_path)
      elephant_dest_is_open_and_in_either_path = elephant_dest.islower() and (elephant_dest in my_path or elephant_dest in elephant_path)
      if not (my_dest == elephant_dest
              or my_dest_is_open_and_in_either_path
              or elephant_dest_is_open_and_in_either_path):  # make sure we don't open the same valve twice
        new_path = (my_path + my_dest, elephant_path + elephant_dest)
        if new_path not in paths:
          rate_at_my_dest = valves[my_dest]['rate']
          rate_at_elephant_dest = valves[elephant_dest]['rate']
          new_score = score_so_far + rate_at_my_dest * (minutes_left - 1) + rate_at_elephant_dest * (minutes_left - 1)
          paths[new_path] = new_score
          search_2(valves, paths, new_path, minutes_left - 1, depth - 1)

path_start = ('AA', 'AA')
minutes_left = 26
minute_increments = 1
num_paths_to_continue = 16000  # arbitrary and bound to fail me somehow
paths = {path_start: 0}

while minutes_left > 0:
  depth = min(minute_increments, minutes_left)
  best_paths = sorted(paths, key=paths.get, reverse=True)[:num_paths_to_continue]
  paths = {path: paths[path] for path in best_paths}
  for path in list(paths.keys()):
    search_2(valves, paths, path, minutes_left, depth)
  minutes_left -= minute_increments
  
best_paths = sorted(paths, key=paths.get, reverse=True)[:num_paths_to_continue]
print(best_paths[0])
print(paths[best_paths[0]])
