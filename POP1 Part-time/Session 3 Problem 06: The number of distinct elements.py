"""
Implement a function numb_of_distinct(L) that given a list L of numbers with all of its elements in ascending order, returns the quantity of distinct elements in it.

For example, the result of
Lst = [1,1,2,3,3]
print(numb_of_distinct(Lst))
must be
3
"""
#implement the required function

def numb_of_distinct(L):
  return len(set(L))

Lst = [1,1,2,3,3]
print(numb_of_distinct(Lst))
