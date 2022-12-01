def findSumOfTwo(sum, ns):
  ns = sorted(ns)
  for i in range(len(ns)):
    for j in range(i, len(ns)):
      x = ns[i]
      y = ns[j]
      if (x+y==sum):
        return (x, y)
      elif (x+y > sum):
        break

def findSumOfContiguous(sum, ns):
  for i in range(len(ns)):
    sum_from_i = 0
    for j in range(i, len(ns)):
      sum_from_i += ns[j]
      if (sum_from_i == sum):
        print((i, j, sum_from_i))
        return ns[i:j+1]
      elif (sum_from_i > sum):
        break

f = open('input.txt')
ls = f.readlines()
nums = list(map(int, ls))
window_size = 25
bad_sum = 0
for i in range(window_size, len(nums)):
  window = nums[i - window_size:i]
  num = nums[i]
  if not findSumOfTwo(num, window):
    bad_sum = num
print(bad_sum)
contiguous_sum_parts = findSumOfContiguous(bad_sum, nums)
print(sum(contiguous_sum_parts))
print(min(contiguous_sum_parts) + max(contiguous_sum_parts))