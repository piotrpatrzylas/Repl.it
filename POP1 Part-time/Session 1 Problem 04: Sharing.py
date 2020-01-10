"""
N students take K pens and distribute them among each other evenly. The remaining (the undivisible) part remains in the box. How many pencisl will each single student get? How many pens will remain in the box?

The program reads the numbers N and K. It should print the two answers for the questions above.

For examle, on input
5
17
output should be
3
2
"""
n = int(input())
k = int(input())

print(k // n)
print(k % n)
