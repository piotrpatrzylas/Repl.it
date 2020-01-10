"""
 A sequence consists of integer numbers and ends with the number 0. Determine the index of the largest element of the sequence. If the largest element is not unique, print the index of the first of them. 

Assume that indexing starts with 0, i.e., the first element in the sequence has index 0, the following element has index 1, etc.

For example, on input
2
8
12
9
12
0
output must be
2
"""
list1 = []
while True:
  num = int(input())
  if num == 0:
    break
  list1 = list1 + [num]
  
print(list1.index(max(list1)))
