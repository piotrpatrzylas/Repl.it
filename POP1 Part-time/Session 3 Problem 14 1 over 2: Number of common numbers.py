"""
 Given two lists of numbers, count how many unique numbers occur in both of them. 

Hint. Use sets to solve this problem quickly.

For example, on input
5 3 3 10 40
40 3 40 1 2
output must be
2
"""
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

print(len(set(l1) & set(l2)))
