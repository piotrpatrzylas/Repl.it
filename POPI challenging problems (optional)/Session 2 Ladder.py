"""
For given integer n = 9 print a ladder of n steps. The k-th step consists of the integers from 1 to k without spaces between them.

For example, on input
3
output must be
1
12
123
"""
num = int(input())

for i in range(1, num+1):
  print("")
  for j in range(1, i+1):
    print(j, end = " ")
