import re
f = open('input.txt')
s = f.read()

chunks = s.split("\n\n")

total = 0
for chunk in chunks:
  unique_answers = set(re.sub(r"\s", "", chunk))
  total += len(unique_answers)
print(total)

total_2 = 0
for chunk in chunks:
  chunk = chunk.strip()
  answer_sets = [set(answers) for answers in chunk.split("\n")]
  intersection = set.intersection(*answer_sets)
  total_2 += len(intersection)
print(total_2)