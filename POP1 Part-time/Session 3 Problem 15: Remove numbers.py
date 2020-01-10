"""
Input is a sequence of lines where the first line indicates which numbers are in the set initially. The second line indicates which numbers are removed from the set (if present). The third line indicates which numbers are added to the set (if not present already). The fourth line indicates which numbers are removed, the fifth indicates which numbers are added, and so on. The process stops when the line 

END

was entered. Print the current contents of the set in the acending order.

For example, on input
1 9 2 8 3 7 4 6
10 7 3
5 8 
1 9
END
output must be
2 4 5 6 8
"""
init = set(list(map(int, input().split())))

while True:
  rem = input()
  if rem == "END":
    break
  rem = set(list(map(int, rem.split())))
  init = init.difference(rem)
  add = input()
  if add == "END":
    break
  add = set(list(map(int, add.split())))
  init = init.union(add)

init = list(init)
init.sort()

for el in init:
  print(el, end = " ")
