from math import pow

def parse_snafu(snafu):
  total = 0
  non_int_muls = {'=': -2, '-': -1}
  for i, c in enumerate(snafu[::-1]):
    mul = non_int_muls[c] if c in non_int_muls else int(c)
    total += int(pow(5, i)) * mul
  return total

def gen_snafu(decimal):
  i = 0
  while pow(5, i) < decimal:
    i += 1
  i -= 1
  print(f'5^{i} ({pow(5,i)}) is less than {decimal}')
  s = ''
  while i >= 0:


f = open('test_input.txt')
decimals = map(parse_snafu, map(str.strip, f))
gen_snafu(sum(decimals))