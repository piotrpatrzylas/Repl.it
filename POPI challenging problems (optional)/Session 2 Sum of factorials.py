"""
Given an integer n, print the sum 1!+2!+3!+...+n! (where m! is the factorial of m given by the product 1 x 2 x ... x m)

This problem has a solution with only one loop, so try to discover it. And don't use the math library.

For example, on input
3
output must be
9
"""
num = int(input())
fac = 1
total = 0

for i in range(1, num+1):
  fac *= i
  total += fac

print(total)

