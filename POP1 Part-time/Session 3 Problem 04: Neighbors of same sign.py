"""
Given a list of numbers, find and print the first adjacent elements which have the same sign. If there is no such pair, leave the output blank. 

For example, on input
-1 2 -3 -4 -5 1 2
output must be
-3 -4
"""
s = input().split()
s = list(map(int, s))

for i in range(1, len(s)):
  if s[i] >= 0 and s[i-1] >= 0:
    print(s[i-1], s[i])
    break
  elif s[i] < 0 and s[i-1] < 0:
    print(s[i-1], s[i])
    break
