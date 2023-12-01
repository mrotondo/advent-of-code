from re import findall

f = open('input.txt')
lines = f.readlines()
sum = 0
for line in lines:
  digits = list(map(int, findall(r'\d', line)))
  number = digits[0] * 10 + digits[-1]
  sum += number

print(sum)
