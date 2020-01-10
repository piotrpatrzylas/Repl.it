"""
Given a list of numbers, swap adjacent items in pairs (A[0] with A[1], A[2] with A[3], etc.). Print the resulting list. If a list has an odd number of elements, leave the last element in place.

For example, on input:
1 3 2 6 7
output must be
3 1 6 2 7
"""
s = list(map(int, input().split()))
lst = []
if len(s) % 2 == 0:
  for el in range(0, len(s)):   
    if el % 2 != 0:
      lst = lst + [s[el]] +[s[el-1]]
elif len(s) % 2 != 0:
  for el in range(0, len(s)-1):   
    if el % 2 != 0:
      lst = lst + [s[el]] +[s[el-1]]
  lst += [s[-1]]

for num in lst:
  print(num, end = " ")
