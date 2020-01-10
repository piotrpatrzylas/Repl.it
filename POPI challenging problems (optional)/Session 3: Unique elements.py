"""
 Given a list of numbers, find and print the elements that appear in the list only once. The elements must be printed in the order in which they occur in the original list. 

For example, on input
4 5 20 4 5 10
output must be
20 10
"""
inp = input()
lst = inp.split()
numlst = []
for el in lst:
  numlst += [int(el)]
newlst = []
for el in numlst:
  if numlst.count(el) == 1:
    newlst += [el]
    
for el in newlst:
  print(el, end = " ")

