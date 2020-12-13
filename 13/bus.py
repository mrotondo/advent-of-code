import functools

f = open('input.txt')
ls = f.readlines()

earliest_departure_time = int(ls[0])
bus_ids = list(map(int, [id for id in ls[1].split(',') if id != 'x']))
all_bus_ids = ls[1].split(',')

departure_time = earliest_departure_time
while (True):
  departure_time += 1
  buses_departing_at_time = list(filter(lambda id: departure_time % id == 0, bus_ids))
  if len(buses_departing_at_time) > 0:
    wait = departure_time - earliest_departure_time
    bus_id = buses_departing_at_time[0]
    print(wait * bus_id)
    break

# thanks to http://homepages.math.uic.edu/~leon/mcs425-s08/handouts/chinese_remainder.pdf

a = []
m = []
for i in range(len(all_bus_ids)):
  bus_id = all_bus_ids[i]
  if bus_id != 'x':
    bus_id = int(bus_id)
    a.append((bus_id - i) % bus_id)
    m.append(bus_id)

M = functools.reduce(lambda x, y: x * y, m)

print("a: " + str(a))
print("m: " + str(m))
print("M: " + str(M))

z = []
for i in range(len(m)):
  zi = 1
  for j in range(len(m)):
    if i != j:
      zi *= m[j]
  z.append(zi)

print("z: " + str(z))

y = []
for i in range(len(m)):
  for yi in range(m[i]):
    if (z[i] * yi) % m[i] == 1:
      y.append(yi)
      break

print("y: " + str(y))

w = [(y[i] * z[i]) % M for i in range(len(m))]

print("w: " + str(w))

x = sum([a[i] * w[i] for i in range(len(m))]) % M

print(x)