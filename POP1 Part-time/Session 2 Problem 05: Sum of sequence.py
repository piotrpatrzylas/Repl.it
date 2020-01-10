"""
 Determine the sum of all elements in the sequence, ending with the number 0. 

For example, on input
1
2
3
0
output must be
6
"""
sum = 0

while True:
  num = int(input())
  if num == 0:
    break
  sum += num
  
print(sum)
