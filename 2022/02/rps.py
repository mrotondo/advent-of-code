def translate(abcs):
  xyzs = {'X': 'A', 'Y': 'B', 'Z': 'C'}
  return xyzs[abcs]

def fight(them, us):
  score = 0
  
  points = {'A': 1, 'B': 2, 'C': 3}
  score += points[us]
  
  beats = {'A': 'C', 'B': 'A', 'C': 'B'}
  if them == us:
    score += 3
  elif beats[us] == them:
    score += 6

  return score

def throw(them, us):
  lose = {'A': 'C', 'B': 'A', 'C': 'B'}
  draw = {'A': 'A', 'B': 'B', 'C': 'C'}
  win = {'A': 'B', 'B': 'C', 'C': 'A'}
  strats = {'X': lose, 'Y': draw, 'Z': win}
  return strats[us][them]

f = open('input.txt')
lines = f.readlines()
total_score = 0
total_throw_score = 0
for match in lines:
  them, us = match.split()
  total_score += fight(them, translate(us))
  total_throw_score += fight(them, throw(them, us))

print(total_score)

print(total_throw_score)