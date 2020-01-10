"""
Given a list of unique numbers, swap the minimal and maximal elements of this list. Print the resulting list. 

For example, on input:
5 7 3 2 1 6
output must be
5 1 3 2 7 6 
"""
lst = list(map(int, input().split()))
minN = min(lst)
maxN = max(lst)

for el in lst:
  if el == minN:
    el = maxN
  elif el == maxN:
    el = minN
  print(el, end = " ")
    

