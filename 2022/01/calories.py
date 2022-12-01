def chunk_by_newlines(lines):
  sublist = []
  for line in lines:
    if line == "\n":
      yield sublist
      sublist =[]
      continue
    sublist.append(line)
  yield sublist

f = open('input.txt')
lines = f.readlines()
sums = []
for chunk in chunk_by_newlines(lines):
  calorie_counts = list(map(int, chunk))
  sums.append(sum(calorie_counts))

print(max(sums))

sorted_sums = sorted(sums, reverse=True)

print(sum(sorted_sums[0:3]))