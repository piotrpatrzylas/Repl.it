"""
Given a sequence of non-negative integers, where each number is written in a separate line. Determine the length of the sequence, where the sequence ends when the integer is equal to 0. Print the length of the sequence (not counting the integer 0). 

For example, on input
3
2
7
0
output should be
3
"""
counter = 0

while True:
  num = int(input())
  if num == 0:
    break
  counter += 1

print(counter)
