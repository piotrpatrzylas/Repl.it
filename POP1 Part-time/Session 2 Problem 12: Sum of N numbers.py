"""
N numbers are given in the input. Read them and print their sum.

The first line of input contains the integer N, which is the number of integers to follow. Each of the next N lines contains one integer. Print the sum of these N integers.

Recommendation. Use for loops.

For example, on input
4
7
10
15
3
output must be
35
"""
first = int(input())
total = 0

for i in range(0, first):
  num = int(input())
  total += num
  
print(total)
