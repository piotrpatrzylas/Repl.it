"""
Given a list of numbers, determine and print the quantity of elements that are greater than both of their neighbors.

The first and the last items of the list shouldn't be considered because they don't have two neighbors.

For example, on input
1 2 3 2 8 7 6 9 5
output must be
3
"""
s = input().split()
s = list(map(int, s))
counter = 0
for i in range(1, len(s)-1):
  if s[i-1] < s[i] and s[i+1] < s[i]:
    counter += 1
    
print(counter)
