from collections import Counter

f = open('input.txt')
lines = f.readlines()

string_pairs = [line.strip().split() for line in lines]

int_pairs = [map(int, pair) for pair in string_pairs]

l1, l2 = list(zip(*int_pairs))
l1 = sorted(list(l1))
l2 = sorted(list(l2))

ordered_pairs = zip(l1, l2)
differences = [abs(x - y) for [x, y] in ordered_pairs]

print(sum(differences))

occurrences_counter = Counter(l2)
similarity = sum([x * occurrences_counter[x] for x in l1])
print(similarity)