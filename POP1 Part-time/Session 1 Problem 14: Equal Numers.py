"""
 Given three integers, determine how many of them are equal to each other. The program must print one of these numbers: 3 (if all are the same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different). 

For example, on input
4
5
4
output must be
2
"""
n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 == n2 == n3:
  print (3)
elif n1 == n2:
  print(2)
elif n1 == n3:
  print(2)
elif n2 == n3:
  print(2)
else:
  print (0)
