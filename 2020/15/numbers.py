nums = [9, 6, 0, 10, 18, 2, 1]
# end = 2020
end = 30000000

# nums = [0,3,6]
# end = 10

last_said_times = dict((nums[i], i) for i in range(len(nums) - 1))
print(last_said_times)

i = len(nums)
last_said_num = nums[-1]
while (True):
  age = 0
  if last_said_num in last_said_times:
    age = i - 1 - last_said_times[last_said_num]
  last_said_times[last_said_num] = i - 1
  # print('i: {0}. last_said_num: {1}. age: {2}'.format(i, last_said_num, age))

  if i % 1000000 == 0:
    print(i)
  if i == end:
    print(last_said_num)
    break

  i += 1
  last_said_num = age
