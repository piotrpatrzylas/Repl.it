"""
For a given integer N, print all the squares of integer numbers where the square is less than or equal to N, in ascending order.

For example, on input
10
output must be
1 4 9
"""
number = int(input())
list1 = list(range(1, number+1))
list2 = [num**2 for num in list1 if num**2 <= max(list1)]
print(list2)
