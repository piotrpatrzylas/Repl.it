"""
A sequence consists of integer numbers and ends with the number 0. Determine the largest element of the sequence. 

For example, on input
4
7
2
0
output must be
7
"""
first = int(input())

while True:
  another = int(input())
  if another == 0:
    break
  if another > first:
    first = another
  
print(first)
  

