from collections import Counter

def count_gaps(ratings):
  # ratings must be sorted
  gaps = Counter()
  prev_rating = 0
  for rating in ratings:
    gaps[rating - prev_rating] += 1
    prev_rating = rating
  gaps[3] += 1
  return gaps

memoized_combos = {}

def count_combos(prev_rating, i, ratings):
  # ratings must be sorted
  if i == len(ratings):
    return 1

  total_combos = 0
  for j in range(i, len(ratings)):
    new_rating = ratings[j]
    if (new_rating <= prev_rating + 3):
      if j not in memoized_combos:
        memoized_combos[j] = count_combos(new_rating, j + 1, ratings)
      total_combos += memoized_combos[j]
    else:
      break

  return total_combos

f = open('test_input3.txt')
ratings = sorted(map(int, f.readlines()))

gaps = count_gaps(ratings)
print(gaps[1] * gaps[3])

print(count_combos(0, 0, ratings))