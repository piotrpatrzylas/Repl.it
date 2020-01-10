"""
 In mathematics, the factorial of an integer n, denoted by n! is the following product 1 x 2 x ... x n

 For the given integer n calculate the value of n!

Recommendation. Use for loops.

For example, on input
4
output must be
24  
"""
num = int(input())
res = 1
for i in range(1, num+1):
  res *= i  
  
print(res)
