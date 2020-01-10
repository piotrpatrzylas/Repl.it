"""
A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are equal to its largest element. 

For example, on input
3
2
5
1
3
5
4
5
0
output must be 
3
"""
num1 = int(input())
mlist = [num1]

while True:
  num2 = int(input())
  if num2 == 0:
    break
  mlist += [num2]
  
print(mlist.count(max(mlist)))
