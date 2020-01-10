"""
A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are greater than their neighbours above. 

For example, on input
3
2
3
1
4
4
3
0
output must be
2
"""
counter = 0

num1 = int(input())
while True:
  num2 = int(input())
  if num2 == 0:
    break
  if num2 > num1:
    counter += 1
  num1 = num2

print(counter)
