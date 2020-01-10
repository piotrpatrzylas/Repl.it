"""
 Given a list of numbers, print all elements that are an even number in the original order.

For example, on input:
3 2 6 55 7 13 10
output must be
2 6 10
"""
s = input().split()
for el in s:
  if int(el) % 2 ==0:
    print(el, end = " ")
