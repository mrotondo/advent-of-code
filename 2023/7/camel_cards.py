import re
import functools
import operator
from collections import defaultdict

RANKED_COUNTS = ['5', '41', '32', '311', '221', '2111', '11111']
def hand_type(hand, jokers=False):
  counts = defaultdict(int)
  for card in hand:
    counts[card] += 1
  if jokers:
    if hand == 'JJJJJ':
      return 0
    if 'J' in counts:
      num_jokers = counts.pop('J')
      (best_card, current_count) = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)[0]
      counts[best_card] = current_count + num_jokers
  canonical_counts = ''.join(map(str, sorted(counts.values(), reverse=True)))
  return RANKED_COUNTS.index(canonical_counts)

# >0 if hand1 better, <0 if hand2 better, 0 if equal
CARD_ORDER_1 = 'AKQJT98765432'
CARD_ORDER_2 = 'AKQT98765432J'
def compare_hands(hand1, hand2, part_2=False):
  hand1_type = hand_type(hand1, jokers=part_2)
  hand2_type = hand_type(hand2, jokers=part_2)
  if hand1_type != hand2_type:
    return -hand1_type + hand2_type
  else:
    card_order = CARD_ORDER_2 if part_2 else CARD_ORDER_1
    for i in range(5):
      hand1_card_score = card_order.index(hand1[i])
      hand2_card_score = card_order.index(hand2[i])
      if hand1_card_score != hand2_card_score:
        return -hand1_card_score + hand2_card_score
  return 0

f = open('input.txt')
hands = []
for line in f.readlines():
  hand, bid = re.search(r'([AKQJT2-9]{5}) (\d+)', line).groups()
  hands.append((hand, int(bid)))

for part_2 in [False, True]:
  hands.sort(key=functools.cmp_to_key(lambda h1, h2: compare_hands(h1[0], h2[0], part_2=part_2)))
  total_winnings = 0
  for idx, (hand, bid) in enumerate(hands):
    total_winnings += bid * (idx + 1)
  print(total_winnings)
