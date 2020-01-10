"""
Implement a function my_sum(lst) that given a list lst of interger numbers, returns the sum of them.

In this exercise, do not use the standard sum function and no loop of any kind. Implement the function recursively using the following idea:

- if the list contains one element, the sum of the list is equal to this element
- if the list contains more elements, the sum of the list is equal to the first element plus the sum of the remaining list

For example, on input:
print(my_sum([1,2,3]))
output must be:
6
"""
def my_sum(lst):
  if len(lst) == 1:
    return lst[0]
  else:
    return lst[0] + my_sum(lst[1:])

