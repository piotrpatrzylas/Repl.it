"""
 Determine the average a of all elements of the sequence ending with the number 0. 

Note. Print only the integer part of a (ignore fractional part).

For example, on input
1
2
4
0
output must be
2
"""
sum = 0
counter = 0
while True:
  number = int(input())
  if number == 0:
    break
  sum += number
  counter += 1
  
print(sum // counter)
