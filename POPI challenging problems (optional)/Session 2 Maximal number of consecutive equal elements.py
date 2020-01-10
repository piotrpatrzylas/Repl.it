"""
 Given a sequence of integer numbers ending with the number 0. Determine the length of the widest fragment where all the elements are equal to each other. 

For example, on input
5
3
4
4
5
5
6
4
4
4
0
output must be
3
"""
num1 = int(input())
results = 1
final = 1

while True:
  num2 = int(input())
  if num2 == 0:
    break
  if num2 == num1:
    results += 1
    if final <= results:
      final += 1
  else:
    results = 0
  num1 = num2
  
print(final)
