"""
Given a list of numbers, find and print all the elements that are greater than the previous element. 

For example, on input
10 6 11 13 10 10 23
output must be
11 13 23
"""
s = input().split()

s = list(map(int, s))

lst = []
for el in range(1, len(s)):
  if s[el] > s[el-1]:
    print(s[el], end = " ")
