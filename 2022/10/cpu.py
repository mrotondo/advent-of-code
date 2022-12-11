import re

f = open('input.txt')
cycle = 0
regX = 1
cycles_of_interest = list(range(20, 220+1, 40))
total = 0
for line in f:
  new_cycle = cycle
  noop = re.search(r'noop', line)
  addx = re.search(r'addx (\-?\d+)', line)
  
  new_cycle += 1
  if new_cycle >= cycles_of_interest[0]:
    total += new_cycle * regX
    cycles_of_interest.pop(0)
    if len(cycles_of_interest) == 0:
      break

  if addx:
    new_cycle += 1
    if new_cycle >= cycles_of_interest[0]:
      total += new_cycle * regX
      cycles_of_interest.pop(0)
      if len(cycles_of_interest) == 0:
        break
    regX += int(addx.group(1))

  cycle = new_cycle

print(total)

f.seek(0)
cycle = 0
pixel_pos = 0
regX = 1
pixels = []
for line in f:
  new_cycle = cycle
  noop = re.search(r'noop', line)
  addx = re.search(r'addx (\-?\d+)', line)

  new_cycle += 1
  # during
  if abs((pixel_pos % 40) - regX) <= 1:
    pixels.append('#')
  else:
    pixels.append('.')
  pixel_pos += 1
  # end during
  # after
  # end after
  if addx:
    new_cycle += 1
    # during
    if abs((pixel_pos % 40) - regX) <= 1:
      pixels.append('#')
    else:
      pixels.append('.')
    pixel_pos += 1
    # end during
    # after
    regX += int(addx.group(1))

    # end after
  cycle = new_cycle

print(''.join(pixels[0:39]))
print(''.join(pixels[40:79]))
print(''.join(pixels[80:119]))
print(''.join(pixels[120:159]))
print(''.join(pixels[160:199]))
print(''.join(pixels[200:239]))