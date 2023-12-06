import re
from math import prod

f = open('input.txt')

time_line = f.readline()
distance_line = f.readline()

# part 1
# times = map(int, re.findall(r'\d+', time_line))
# distances = map(int, re.findall(r'\d+', distance_line))

# part 2
times = map(int, re.findall(r'\d+', time_line.replace(" ", "")))
distances = map(int, re.findall(r'\d+', distance_line.replace(" ", "")))

records = list(zip(times, distances))

all_record_beaters = []
for (race_duration, record_distance) in records:
  num_record_beaters = 0
  for time_held in range(race_duration):
    distance_traveled = time_held * (race_duration - time_held)
    if distance_traveled > record_distance:
      num_record_beaters += 1
  all_record_beaters.append(num_record_beaters)

print(prod(all_record_beaters))