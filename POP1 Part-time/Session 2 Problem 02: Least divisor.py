"""
 Given an integer not less than 2. Print its smallest integer divisor greater than 1. 

For example, on input
9
output must be
3
"""
num = int(input())

for i in range(2, num+1):
  if num % i == 0:
    print(i)
    break
