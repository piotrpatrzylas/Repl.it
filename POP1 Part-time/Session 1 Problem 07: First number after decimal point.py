"""
 Given a positive real number, print its first digit to the right of the decimal point.

For example, on input
56.8945
output should be
8
"""
n = float(input())
x = round(n, 1)
z = int(x)
print(int((x-z)*10))
