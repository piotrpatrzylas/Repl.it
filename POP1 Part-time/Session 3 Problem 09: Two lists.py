"""
Given two lists of numbers, print the numbers that are in the fist list but are not in the second. Print those numbers in the ascending order. (You can assume that the numbers in each of the two lists do not repeat.)

For example, on input
20 4 45 6 10
9 10 6 3
output must be
4 20 45
"""
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
res = []

for num in l1:
  if num not in l2:
    res += [num]
res.sort()
for num in res:
  print(num, end = " ")
