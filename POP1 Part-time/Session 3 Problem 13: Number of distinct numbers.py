"""
Implement a function distinct_nums(L) that, given a list of integers, L, returns how many distinct numbers there are in L.

Note. This task can be solved very quickly using sets.

For example, the result of
print(distinct_nums([5,3,2,3,2,4]))
must be
4
"""
def distinct_nums(L):
  return len(set(L))
