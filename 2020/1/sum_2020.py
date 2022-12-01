# def findSumOfTwo(sum, ns):
#     ns = sorted(ns)
#     for i in range(len(ns)):
#         for j in range(i, len(ns)):
#             x = ns[i]
#             y = ns[j]
#             if (x+y==sum):
#                 return (x, y)
#             elif (x+y > sum):
#                 break
# def findSumOfThree(sum, ns):
#     ns = sorted(ns)
#     for i in range(len(ns)):
#         for j in range(i, len(ns)):
#             for k in range(j, len(ns)):
#                 x = ns[i]
#                 y = ns[j]
#                 z = ns[k]
#                 if (x+y+z==sum):
#                     return (x, y, z)
#                 elif (x+y+z > sum):
#                     break


def findSumOfN(sum, n, ns, start_i = 0):
    # ns MUST BE SORTED
    if (n == 0 or ns is None):
        return (0, [])
    for i in range(start_i, len(ns)):
        x = ns[i]
        something = findSumOfN(sum - x, n - 1, ns, i + 1)
        (subSum, xs) = something
        if (x + subSum == sum):
            return (sum, [x] + xs)
        elif (x + subSum > sum):
            return (0, [])


f = open('input.txt')
lines = f.readlines()
nums = sorted([int(l) for l in lines])

print(findSumOfN(2020, 2, nums))
print(findSumOfN(2020, 3, nums))
print(findSumOfN(2020, 4, nums))
print(findSumOfN(2020, 5, nums))
print(findSumOfN(2020, 100, nums))
# print(findSumOfTwo(2020, nums))
# print(findSumOfThree(2020, nums))
