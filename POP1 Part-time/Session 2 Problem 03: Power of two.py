"""
 For a given integer N, find the greatest integer x where 2 to the power of x is less than or equal to N. Print the exponent value x and the result of 2 to the power of x.

For example, on input
20
output must be
4 16

Advise. Try not to use ** operator. This makes the problem a bit more challenging.
"""
num = int(input())
power = 1
n_power = 2

while n_power <= num:
  n_power *= 2
  power += 1
power -= 1
n_power /= 2
n_power = int(n_power)
  
print(power, n_power)
